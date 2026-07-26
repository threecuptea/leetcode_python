from dotenv import load_dotenv
import os
import asyncio
import aiohttp
from aiohttp import ClientTimeout
import random
import orjson
from typing import Any

site_journal_lookup = {
    'acsjournals.onlinelibrary.wiley.com': 'CA: A Cancer Journal for Clinicians',
    'annalsofoncology.org': 'Annals of Oncology',
}
load_dotenv(override=True)
serper_api_key = os.getenv('SERPER_API_KEY')

def retrieve_link_meta_from_rawdata(raw_data, cancer) -> dict[str, dict[str, Any]]:
    d = dict(orjson.loads(raw_data))
    links = {}
    if 'organic' in d:
        for item in d['organic']:
            # item is dict
            if 'link' in item:
                url =str(item['link'])
                # filter out pdf until I have time to figure out where to find the embedded pdf links
                if url.find('pdf') != -1:
                    continue
                for site, journal in site_journal_lookup.items():
                    if url.find(site) == -1:
                        continue
                    else:
                        links[url] = {'cancer': cancer, 'journal': journal, 'title': item.get('title', ''), 'date': item.get('date', '')}
    return links

sites = ['acsjournals.onlinelibrary.wiley.com', 'annalsofoncology.org']
cancers = ['pancreatic cancer', 'lung cancer', 'breast cancer', 'colorectal cancer', 'prostate cancer', 'liver cancer', 'lymphoma', 'glioblastoma']
q_d = {
    "q": "",
    "page": 1,
    "tbs": "qdr:y",
} #
headers = {
    'X-API-KEY': serper_api_key,
    'Content-Type': 'application/json'
}
agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Chrome/144.0.0.0",
    "Safari/537.36",
]

serper_url = "https://google.serper.dev/search"
async def send_serper_request(session: aiohttp.ClientSession , payload, cancer, retries=2) -> dict[str, dict[str, Any]] | None:
    for attempt in range(retries + 1):
        headers["User-Agent"] = random.choice(agents)
        try:
            # it returns _RequestContextManager
            # async with an object of ContextManager that implements __aenter__ and __aexit__ method.   ContextManager
            # can suspend the operation and return control to Event Loop
            # aiohttp.ClientSession.get/ post ... all return a ContextManager
            async with session.post(serper_url, data=payload, headers=headers, timeout=ClientTimeout(total=30)) as r:
                print(f'serper_url= {serper_url}, payload= {payload}, headers={headers}, status={r.status}')
                if r.status == 200:
                    content = await r.text()
                    # need this step to have separate thread to run a sync function; otherwise the whole flow become sync
                    # The form is func and args
                    return await asyncio.to_thread(retrieve_link_meta_from_rawdata, content, cancer)
                if r.status in (503, 429):
                    await asyncio.sleep((attempt + 1) * 2)
        except Exception:
            if attempt == retries:
                return None
    return None


async def find_all_target_urls(concurrency=300, num_pages=4) -> dict[str, dict[str, Any]]:
    sem = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, ttl_dns_cache=300)
    # async with syntax aiohttp.ClientSession is ContextManager because it implements __aenter__ and __aexit__ method
    async with aiohttp.ClientSession(connector=connector) as session:
        async def worker(payload, cancer):
            async with sem:
                return await send_serper_request(session, payload, cancer)
        tasks = []
        for site in sites:
            for cancer in cancers:
                for page_num in range(1, num_pages + 1):
                    query = q_d.copy()
                    query['page'] = page_num
                    query['q'] = f'"{cancer}" site:{site}'
                    payload = orjson.dumps(query)
                    tasks.append(worker(payload, cancer))
        results = {}
        lst_of_dict = await asyncio.gather(*tasks)
        for subdict in lst_of_dict:
            if subdict:
                results.update(subdict)
        return results
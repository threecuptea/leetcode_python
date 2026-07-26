# Practice async web crawling
import asyncio
import aiohttp
from aiohttp import ClientTimeout
import random
class MassiveScraper:
    def __init__(self, concurrency=300):
        self.concurrency = concurrency
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ]

    async def fetch(self, session, url, retries=2):
        for attempt in range(1, retries + 1):
            agent_choice = random.choice(self.user_agents)
            headers = {'User-Agent': random.choice(self.user_agents)}
            async with session.get(url, headers=headers, timeout=ClientTimeout(total = 10)) as res:
                try:
                    if res.status == 200:
                        return await res.text()
                    if res.status in (429, 503):
                        await asyncio.sleep(2 * attempt)
                except Exception:
                    if attempt == retries:
                        return None
                return None
    async def process_batch(self, urls):
        sem = asyncio.Semaphore(self.concurrency)
        connector = aiohttp.TCPConnector(limit=self.concurrency, ttl_dns_cache=300)
        async with aiohttp.ClientSession(connector=connector) as session:
            async def worker(url):
                async with sem:
                    return await self.fetch(session, url)
            tasks = [worker(url) for url in urls]
            return await asyncio.gather(*tasks)

    async def run(self, all_urls, batch_size=5000):
        result = []
        for start in range(0, len(all_urls), batch_size):
            batch = all_urls[start:(start + batch_size)]
            result.extend(await self.process_batch(batch))
            print(f"Batch {start//batch_size+1} done: {start+len(batch)}/{len(all_urls)}")
        return result
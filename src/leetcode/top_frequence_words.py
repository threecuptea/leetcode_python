from collections import Counter
from typing import List
import time
from datetime import datetime, timezone, timedelta
####
# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/description/
###
def topKFrequent(words: List[str], k: int) -> List[str]:
    c = Counter(words)
    return [x for x, _ in sorted(c.items(), key=lambda item: (-item[1], item[0]))[:k]]

def test_top_k_frequent_words():
    words = ["i","love","leetcode","i","love","coding"]
    assert  topKFrequent(words, 2) == ['i', 'love']

def main():
    date_str = "2026-06-04 15:30:00"
    test_time = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print(date_str)
    print(f'year={test_time.tm_year}')
    print(f'month={test_time.tm_mon}')
    print(f'date={test_time.tm_mday}')
    print(f'weekday={test_time.tm_wday}')
    print(test_time.tm_hour)
    print(test_time.tm_min)
    print(test_time.tm_sec)

    now = datetime.now()
    f_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f_date)
    now_utc = datetime.now(timezone.utc)
    # default using 'T'
    print(now_utc.isoformat())
    print(now_utc.isoformat(' ', timespec='seconds'))
    print((now_utc + timedelta(weeks=1)).isoformat())

    test_top_k_frequent_words()

if __name__ == '__main__':
    main()
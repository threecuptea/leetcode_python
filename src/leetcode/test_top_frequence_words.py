import pytest
from src.leetcode.top_frequence_words import topKFrequent

@pytest.mark.parametrize("words, k,  expected", [
    (["i","love","leetcode","i","love","coding"], 2, ['i', 'love']),
    (["the","is","sunny","the","the","the","is","is", "day"], 3, ['the', 'is', 'day'])
])
def test_multiple_top_k_frequent_words(words, k, expected):
    assert topKFrequent(words, k) == expected






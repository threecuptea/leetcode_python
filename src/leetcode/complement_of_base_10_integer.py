# https://leetcode.com/problems/complement-of-base-10-integer/
def bitwiseComplement(self, n: int) -> int:
    # n = 0 edge case because its bit_length == 0
    if n == 0:
        return 1
    # 5, 101, the complement: 010 = 2, they XOR should 111
    # bit_length = 3
    bit_length = n.bit_length()
    # a XOR b = c, a XOR c = b
    # the mask should be 111
    # 101
    # 111
    # ---------
    # 010 = 2
    # to create the mask of bit_length = 3
    # 1 shift-left 3: append 3 0 at the right: 1000 then -1
    mask = (1 << bit_length) - 1
    return n ^ mask
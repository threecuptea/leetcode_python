
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/compare-bsts-equal-values-different-structure/problem
def verifySameMultisetDifferentStructure(root1, root2):
    # Write your code here
    null_value = 100001

    def not_null(num):
        return num != null_value

    same_multiset = \
        sorted(list(filter(not_null, root1))) == sorted(list(filter(not_null, root2)))
    if not same_multiset:
        return False

    same_len = len(root1) == len(root2)
    if same_multiset and not same_len:
        return True

    def null_pattern(root):
        root_null_pattern = []
        idx = 0
        while True:
            try:
                new_idx = root.index(null_value, idx)
                root_null_pattern.append(new_idx)
                if new_idx + 1 < len(root):
                    idx = new_idx + 1
                else:
                    break
            except ValueError:
                break
        return root_null_pattern

    same_null_pattern = null_pattern(root1) == null_pattern(root2)
    if same_multiset and same_len and not same_null_pattern:
        return True
    return False

# O(n) solution of one pass solution
def fuzzy_search(sub, super_str):
    sub_idx = len(sub) - 1
    char_list = list(super_str)
    # starting from the back
    while True:
        # if exhaust all super_set before exhaust all sub
        if not char_list:
            return False
        ch = char_list.pop()
        if ch == sub[sub_idx]:
            sub_idx -= 1
            # exhaust all characters in sub, 'Done'
            if sub_idx == -1:
                return True

def main():
    to_match = "car"
    char_set = "carutils"
    print(f'Match= {fuzzy_search(to_match, char_set)}')
    to_match = "carpool"
    char_set = "carpool"
    print(f'Match= {fuzzy_search(to_match, char_set)}')
    to_match = "cwhel"
    char_set = "carwheel"
    print(f'Match= {fuzzy_search(to_match, char_set)}')
    to_match = "le"
    char_set = "carwheel"
    print(f'Match= {fuzzy_search(to_match, char_set)}')

if __name__ == "__main__":
    main()





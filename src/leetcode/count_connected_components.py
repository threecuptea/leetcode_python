from collections import defaultdict
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-connected-components-in-network
# Leetcode has another implementation for complete connected components that has stricter rule: No. of edges are
# n * (n -1) // 2
# It is less messy to use Union Find since links are undirect (bi-direct)
def countIsolatedCommunicationGroups(links, n):
    # Write your code here
    new_group_idx = 1
    # Keep groups and pc_groups in sync when one vertex take the other one's group index
    groups = defaultdict(list)  # group index: all member belongs to that group
    pc_group = {}  # Record the mapping: pc -> group idx
    in_links = set()  # record all vertices in links (edges) so that we can count isolated PC

    # they both join but belong to different groups, Take one or the other and migrate members
    def migrate(from_idx, to_idx):
        for mem in groups[from_idx]:
            pc_group[mem] = to_idx
        groups[to_idx].extend(groups[from_idx])
        del groups[from_idx]

    # for the scenario that one of them join the group, the one not in a group will take the group idx of the one in a group
    def join_group(v, g_idx):
        pc_group[v] = g_idx
        groups[g_idx].append(v)

    for v1, v2 in links:
        in_links.add(v1)
        in_links.add(v2)
        # they do not join any group yet
        if v1 not in pc_group and v2 not in pc_group:
            pc_group[v1], pc_group[v2] = new_group_idx, new_group_idx
            groups[new_group_idx].extend([v1, v2])
            new_group_idx += 1
        # Only one of them join the group, the one not in a group will take the group idx of the one in a group
        elif v1 not in pc_group or v2 not in pc_group:
            if v1 in pc_group:
                join_group(v2, pc_group[v1])
            else:
                join_group(v1, pc_group[v2])
        # they both join but belong to different groups
        elif pc_group[v1] != pc_group[v2]:
            g_idx1, g_idx2 = pc_group[v1], pc_group[v2]
            if len(groups[g_idx1]) >=  len(groups[g_idx2]):
                migrate(g_idx2, g_idx1)
            else:
                migrate(g_idx1, g_idx2)
        # no need to do anything if they are in the same groups
    # Don't forget to include isolated components which have no link to any other one.
    cnt_isolated_vertex = 0
    for i in range(n):
        if i not in in_links:
            cnt_isolated_vertex += 1

    return  len(groups) + cnt_isolated_vertex
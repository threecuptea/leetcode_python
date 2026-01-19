from collections import defaultdict
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-connected-components-in-network
# Use Union find.  It is less messy since its undirected graph
def countIsolatedCommunicationGroups(links, n):
    # Write your code here
    new_group_idx = 1
    groups = defaultdict(list)
    pc_group = {}
    in_links = set()

    def migrate(from_idx, to_idx):
        for mem in groups[from_idx]:
            pc_group[mem] = to_idx
        groups[to_idx].extend(groups[from_idx])
        del groups[from_idx]

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
        # Only one of them join the group
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
    cnt_isolated_vertex = 0
    for i in range(n):
        if i not in in_links:
            cnt_isolated_vertex += 1

    return  len(groups) + cnt_isolated_vertex
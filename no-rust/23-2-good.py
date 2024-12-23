from collections import defaultdict
lines = open("../input/23.in").read().strip().split('\n')
# lines = open("test").read().strip().split('\n')

g = defaultdict(bool)
h = defaultdict(set)
ver = set()

for line in lines:
    a, b = line.split('-')
    h[a].add(b)
    h[b].add(a)
    ver.add(a)
    ver.add(b)

# https://www.altcademy.com/blog/discover-the-largest-complete-subgraph/
def bron_kerbosch(graph, r=set(), p=None, x=set()):
    if p is None:
        p = set(graph.keys())

    if not p and not x:
        yield r
    else:
        u = next(iter(p | x))  # Choose a pivot vertex
        for v in p - graph[u]:
            yield from bron_kerbosch(graph, r | {v}, p & graph[v], x & graph[v])
            p.remove(v)
            x.add(v)

def find_largest_complete_subgraph(graph):
    cliques = list(bron_kerbosch(graph))
    return max(cliques, key=len)

s = find_largest_complete_subgraph(h)
print(','.join(sorted(list(s))))
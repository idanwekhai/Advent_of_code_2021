from igraph import *
with open('input.txt') as f:
    edges = f.readlines()

def make_input(seq):
    edges = []
    vertices = []
    for edge in seq:
        ed = edge.strip('\n').split("-")
        edges.append(ed)
        vertices.extend(ed)
    return edges, set(vertices)

def make_graph(edges, vertices):
    g = Graph()

    for v in vertices:
        g.add_vertices(v)
        
    for edge in edges:
        g.add_edges([(edge[0], edge[1])])
    return g, g.get_all_simple_paths("start", "end", mode="all"), g.get_all_simple_paths("end", "start", mode="all")#, g.get_adjacency()


def solve(graph, curr_node="start", visited=None, level=1):

    if curr_node =="end":
        return 1
    if visited is None:
        visited = set()
    else:
        visited = visited.copy()

    if curr_node.islower():
        visited.add(curr_node)
        
    count = 0
    nb = graph.neighbors(curr_node)
    neighbors = [graph.vs[i]["name"] for i in nb]
    for neighbor in neighbors:
        if neighbor in visited and level==2 and neighbor != "start":
            count += solve(graph, neighbor, visited, 1)
        elif neighbor not in visited:
            count += solve(graph, neighbor, visited, level)
    return count

def solve2(graph, curr_node="start", visited=None, level=2):

    if curr_node =="end":
        return 1
    if visited is None:
        visited = []
    else:
        visited = visited.copy()

    if curr_node.islower():
        visited.append(curr_node)
        
    count = 0
    nb = graph.neighbors(curr_node)
    neighbors = [graph.vs[i]["name"] for i in nb]
    for neighbor in neighbors:
        if neighbor in visited and level==2 and neighbor != "start":
            count += solve2(graph, neighbor, visited, 1)
        elif neighbor not in visited:
            count += solve2(graph, neighbor, visited, level)
    return count


g_edges, g_vertices = make_input(edges)

ans = make_graph(g_edges, g_vertices)

print(solve(ans[0]))
print(solve2(ans[0]))

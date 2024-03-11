'''• Дана структура типа бинарное дерево. Все вершины
пронумерованы от 1 до n. Дерево задано в виде списка кортежей:
[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
• Каждый кортеж (a,b) показывает, что вершина a соединена с
вершиной b.
• По определению в дереве невозможны циклы.
• Найти максимальную длину от вершины (1) до конечной
вершины.'''

def build_adj_list(edges):
    adj_list = {}
    for a, b in edges:
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []
        adj_list[a].append(b)
        adj_list[b].append(a)
    return adj_list

def dfs(node, parent, depth, adj_list):
    max_depth = depth
    for neighbor in adj_list[node]:
        if neighbor != parent:
            max_depth = max(max_depth, dfs(neighbor, node, depth + 1, adj_list))
    return max_depth

def find_max_length(edges):
    adj_list = build_adj_list(edges)
    return dfs(1, None, 0, adj_list)

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
max_length = find_max_length(edges)
print("Максимальная длина от вершины до конечной вершины(1):", max_length)

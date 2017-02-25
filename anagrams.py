file = open('words.txt')
dictionary = {}

        
for word in file:
    key = tuple(sorted(word))
    if key in dictionary:
        list.append(word[:len(word)-1])
        dictionary[key] = list
        print dictionary[key]
    else:
        list = [word[:len(word)-1]]
        dictionary[key] = list
    









#     visited = []
#     queue = collections.deque([root])
#     dfs
    
# def dfs(graph, start):
# visited, stack = set(), [start]
# while stack:
#     vertex = stack.pop()
#     if vertex not in visited:
#         visited.add(vertex)
#         stack.extend(graph[vertex] - visited)
# return visited



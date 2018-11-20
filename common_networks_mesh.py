#mesh network
from collections import defaultdict


input_stream = """INTERNET,A
INTERNET,C
A,INTERNET
A,B
A,G
B,A
B,E
C,INTERNET
C,F
D,E
E,D
E,B
E,F
F,E
F,C
F,G
G,F
H,I
I,H"""

#expected output
##INTERNET,A
##INTERNET,A,B
##INTERNET,A,B,E
##INTERNET,A,B,E,D
##INTERNET,C
##INTERNET,C,F
##INTERNET,C,F,G



def create_graph_dict(input_stream):
    node_dict = defaultdict(list)
    for i in input_stream.strip().split('\n'):
        node, neighbor = i.split(',')[0], i.split(',')[1]
        node_dict[node].append(neighbor)
    #remove instances where edges are unidirectional
    for node, neighbors in node_dict.copy().items():
        for neighbor in neighbors:
            if node not in node_dict[neighbor]:
                node_dict[node].remove(neighbor)
    return node_dict
#use BFS to find shortest path from node to node(internet)
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]
        if path.count(node) > 3: #cycled
            return None
        if node == end:
            return path
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return path

def main():
    graph = create_graph_dict(input_stream)
    network_arr = []
    for k, v in graph.items():
        shortest_path = bfs(graph,"INTERNET",k)
        if shortest_path and k != "INTERNET":
            network_arr.append("".join(x+","for x in (shortest_path)))
            
    network_arr.sort(key = lambda x : x[1:]) #sort by node after internet
    for na in network_arr:
        print (na[:-1]) #remove comma

        
if __name__ == "__main__":
    main()

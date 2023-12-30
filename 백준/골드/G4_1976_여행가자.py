import sys
from collections import deque

def find_connected_components_bfs(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    components = []

    for node in range(1, num_nodes + 1):
        if not visited[node - 1]:
            component = []
            queue = deque()
            queue.append(node)
            visited[node - 1] = True

            while queue:
                current_node = queue.popleft()
                component.append(current_node)

                for neighbor, is_connected in enumerate(graph[current_node - 1]):
                    if is_connected == 1 and not visited[neighbor]:
                        queue.append(neighbor + 1)
                        visited[neighbor] = True

            components.append(component)

    return components
def find_key_by_value(mapping_dict, value_to_find):
    for key, value_list in mapping_dict.items():
        if value_to_find in value_list:
            return key
    return None
connect_dict={}

N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())
CityGraph=[]
for i in range(N):
    CityGraph.append(list(map(int,sys.stdin.readline().rstrip().rsplit())))

connected_City = find_connected_components_bfs(CityGraph)
for i, component in enumerate(connected_City, start=1):
    connect_dict[i]=component
dest_list=list(map(int,sys.stdin.readline().rstrip().rsplit()))
answer="YES"
bas_CityGroup=find_key_by_value(connect_dict,dest_list[0])
for i in range(len(dest_list)):
    if find_key_by_value(connect_dict,dest_list[i])!=bas_CityGroup:
        answer="NO"
        break
print(answer)

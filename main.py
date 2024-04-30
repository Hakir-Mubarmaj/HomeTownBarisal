import folium
import webview
import networkx as nx

# Define the coordinates for Barisal city
latitude = 22.7010
longitude = 90.3669

# Create a map centered around Barisal city
map_barisal = folium.Map(location=[latitude, longitude], zoom_start=13)


# Convert custom_nodes to a dictionary
custom_nodes_dict = {
    'a': (22.7127, 90.3656),
    'b': (22.7110, 90.3626),
    'c': (22.7148, 90.3490),
    'd': (22.7079, 90.3711),
    'e': (22.7010, 90.3533),
    'f': (22.7013, 90.3648),
    'g': (22.6976, 90.3695),
    'h': (22.6941, 90.3641),
    'i': (22.6888, 90.3569),
    'j': (22.6786, 90.3470),
    'k': (22.6599, 90.3624),
    # Add more nodes as needed
}

# Create a NetworkX graph
G = nx.Graph()

# Add custom nodes to the graph
for node, coord in custom_nodes_dict.items():
    G.add_node(node, pos=coord)

# Add edges with weights
G.add_edge('a', 'b', weight=8)  # Example weight
G.add_edge('b', 'c', weight=6)
G.add_edge('b', 'd', weight=5)
G.add_edge('b', 'f', weight=7)
G.add_edge('c', 'e', weight=6)
G.add_edge('e', 'f', weight=6)
G.add_edge('d', 'g', weight=10)
G.add_edge('g', 'h', weight=4)
G.add_edge('f', 'h', weight=5)
G.add_edge('h', 'i', weight=5)
G.add_edge('e', 'i', weight=7)
G.add_edge('i', 'j', weight=11)
G.add_edge('j', 'k', weight=8)

# Add custom nodes to the map
for node, coord in custom_nodes_dict.items():
    folium.Marker(location=coord, popup=node).add_to(map_barisal)

# Define BFS algorithm
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    folium.PolyLine(locations=[custom_nodes_dict[vertex], custom_nodes_dict[neighbor]], color='red').add_to(map_barisal)
                    queue.append(neighbor)
    return visited

# Run BFS
bfs_path = bfs(G, 'a')

# Define DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            # Color the edge blue on the map
            folium.PolyLine(locations=[custom_nodes_dict[start], custom_nodes_dict[neighbor]], color='blue').add_to(map_barisal)
            dfs(graph, neighbor, visited)
    return visited

# Run DFS
#dfs_path = dfs(G, 'a')

# Save the map to an HTML file
map_barisal.save('barisal_map.html')

# Create a webview window that displays the map
webview.create_window('Barisal Map', 'barisal_map.html')

# Run the webview
webview.start()

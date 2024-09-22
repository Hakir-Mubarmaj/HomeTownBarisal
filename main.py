import folium
import webview
from graph import custom_nodes_dict, map_barisal, areas
from backtracing import area_color_assignment


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
#bfs_path = bfs(G, 'a')

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

def add_colored_areas_to_map(color_assignment):
    color_map = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00'}
    
    for area, boundary in areas.items():
        if area in color_assignment:
            folium.Polygon(
                locations=boundary,
                color=color_map[color_assignment[area]],
                fill=True,
                fill_color=color_map[color_assignment[area]],
                fill_opacity=0.5
            ).add_to(map_barisal)

# Choose which color assignment to visualize
add_colored_areas_to_map(area_color_assignment)

# Run DFS
#dfs_path = dfs(G, 'a')

# Save the map to an HTML file
map_barisal.save('barisal_map.html')

# Create a webview window that displays the map
webview.create_window('Barisal Map', 'barisal_map.html')

# Run the webview
webview.start()

import folium
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
}
area_a_boundary = [custom_nodes_dict['a'], custom_nodes_dict['b'], custom_nodes_dict['c']]
area_b_boundary = [custom_nodes_dict['a'], custom_nodes_dict['b'], custom_nodes_dict['d']]
area_c_boundary = [custom_nodes_dict['b'], custom_nodes_dict['c'], custom_nodes_dict['e'], custom_nodes_dict['f']]
area_d_boundary = [custom_nodes_dict['b'], custom_nodes_dict['d'], custom_nodes_dict['g'], custom_nodes_dict['f']]
area_e_boundary = [custom_nodes_dict['e'], custom_nodes_dict['f'], custom_nodes_dict['g'], custom_nodes_dict['h']]
area_f_boundary = [custom_nodes_dict['e'], custom_nodes_dict['h'], custom_nodes_dict['i']]
area_g_boundary = [custom_nodes_dict['e'], custom_nodes_dict['i'], custom_nodes_dict['j']]
area_h_boundary = [custom_nodes_dict['i'], custom_nodes_dict['j'], custom_nodes_dict['k']]
area_i_boundary = [custom_nodes_dict['i'], custom_nodes_dict['k'], custom_nodes_dict['h']]
area_j_boundary = [custom_nodes_dict['h'], custom_nodes_dict['k'], custom_nodes_dict['g']]

areas = {
    'A': area_a_boundary,
    'B': area_b_boundary,
    'C': area_c_boundary,
    'D': area_d_boundary,
    'E': area_e_boundary,
    'F': area_f_boundary,
    'G': area_g_boundary,
    'H': area_h_boundary,
    'I': area_i_boundary,
    'J': area_j_boundary
}

# Create a NetworkX graph for areas
area_graph = nx.Graph()

# Add areas as nodes
for area in areas:
    area_graph.add_node(area)

# Manually add edges based on shared boundaries (you can automate this if needed)
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'),
    ('D', 'E'), ('E', 'F'), ('E', 'J'), ('F', 'G'), ('F', 'I'),
    ('G', 'H'), ('H', 'I'), ('G', 'H'), ('I', 'J')
]

area_graph.add_edges_from(edges)



# Create a NetworkX graph
G = nx.Graph()

# Add custom nodes to the graph
for node, coord in custom_nodes_dict.items():
    G.add_node(node, pos=coord)

# Add edges with weights
G.add_edge('a', 'b', weight=8) 
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

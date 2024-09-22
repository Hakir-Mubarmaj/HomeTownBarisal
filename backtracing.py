from graph import area_graph

# Define possible colors
colors = ['red', 'green', 'blue', 'yellow']

# Define the function to check if the current color assignment is safe
def is_safe_area(area, color, assignment, graph):
    for neighbor in graph.neighbors(area):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking_coloring_areas(graph, colors, assignment={}, area_index=0):
    areas = list(graph.nodes)
    if area_index == len(areas):
        return assignment
    
    current_area = areas[area_index]
    for color in colors:
        if is_safe_area(current_area, color, assignment, graph):
            assignment[current_area] = color
            result = backtracking_coloring_areas(graph, colors, assignment, area_index + 1)
            if result:
                return result
            assignment.pop(current_area)
    return None

# Run backtracking for areas
area_color_assignment = backtracking_coloring_areas(area_graph, colors)
print("Backtracking Color Assignment for Areas:", area_color_assignment)

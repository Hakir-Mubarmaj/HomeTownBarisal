from graph import area_graph
from backtracing import is_safe_area, colors

# Forward checking function to maintain domain consistency
def forward_checking_areas(graph, colors, assignment={}, area_index=0, domains=None):
    if domains is None:
        domains = {area: list(colors) for area in graph.nodes}
    
    areas = list(graph.nodes)
    if area_index == len(areas):
        return assignment
    
    current_area = areas[area_index]
    for color in domains[current_area]:
        if is_safe_area(current_area, color, assignment, graph):
            assignment[current_area] = color
            
            new_domains = {area: list(dom) for area, dom in domains.items()}
            for neighbor in graph.neighbors(current_area):
                if color in new_domains[neighbor]:
                    new_domains[neighbor].remove(color)
            
            result = forward_checking_areas(graph, colors, assignment, area_index + 1, new_domains)
            if result:
                return result
            assignment.pop(current_area)
    return None

# Run forward checking for areas
area_color_assignment_fc = forward_checking_areas(area_graph, colors)
print("Forward Checking Color Assignment for Areas:", area_color_assignment_fc)

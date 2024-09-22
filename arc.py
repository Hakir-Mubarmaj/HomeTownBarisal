from collections import deque
from graph import area_graph 
from backtracing import is_safe_area, colors

def ac3_areas(graph, domains):
    queue = deque([(xi, xj) for xi in graph.nodes for xj in graph.neighbors(xi)])
    
    while queue:
        xi, xj = queue.popleft()
        if revise(graph, domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in graph.neighbors(xi):
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(graph, domains, xi, xj):
    revised = False
    for x in domains[xi][:]:
        if not any([x != y for y in domains[xj]]):
            domains[xi].remove(x)
            revised = True
    return revised


def arc_consistency_coloring_areas(graph, colors):
    domains = {area: list(colors) for area in graph.nodes}
    ac3_areas(graph, domains)
    assignment = {}
    
    def backtrack(area_index=0):
        areas = list(graph.nodes)
        if area_index == len(areas):
            return assignment
        
        current_area = areas[area_index]
        for color in domains[current_area]:
            if is_safe_area(current_area, color, assignment, graph):
                assignment[current_area] = color
                result = backtrack(area_index + 1)
                if result:
                    return result
                assignment.pop(current_area)
        return None

    return backtrack()

# Run arc consistency for areas
area_color_assignment_ac = arc_consistency_coloring_areas(area_graph, colors)
print("Arc Consistency Color Assignment for Areas:", area_color_assignment_ac)

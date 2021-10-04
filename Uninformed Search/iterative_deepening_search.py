# Author: Matt Williams
# Version:  9/16/2021 
from read_graph import read_graph
from depth_limited_search import depth_limited_search

# recursive method to calculate and return the deepest depth in the given directed graph. 
# graph: the directed graph in question as either an adjacency matrix or list.
# is_Matrix: boolean value telling the method which type the graph variable is. 
# cur_node: the current node the algorithm is on. 
# cur_depth: the current depth at the current node.

def calculate_deepest_depth(graph, is_Matrix, cur_node, cur_depth):

    deepest_depth = cur_depth
    row = graph[ord(cur_node) - ord('a')]

    if is_Matrix: 
        for i in range(len(row)):
            if row[i] == 1:
                new_cur_node = chr(i + ord('a'))
                new_depth = calculate_deepest_depth(graph, is_Matrix, new_cur_node, cur_depth + 1)
                if new_depth > deepest_depth:
                    deepest_depth = new_depth
        
        return deepest_depth
    
    #if adjacency list
    for neighbor in row: 
        new_depth = calculate_deepest_depth(graph, is_Matrix, neighbor, cur_depth + 1)
        if new_depth > deepest_depth: 
            deepest_depth = new_depth
    
    return deepest_depth

# This method runs the iterative Deepening Search Algorithm. 
# graph: The given directed graph as either an adjacency matrix or adjacency list. 
# is_Matrix: boolean value telling the method which type the graph variable is.
# start: Where should the algorithm start the search. 
# end: Where is the destination of the search. 
# returns a list of nodes, or an empty list if no path is found.
def iterative_deepening_search(graph, is_Matrix, start, end):
    if start == end: 
        return [start]

    deepest_depth = calculate_deepest_depth(graph, is_Matrix, start, 0)
    cur_depth_limit = 1
    found = False
    path = []
    while not found:
        path = depth_limited_search(graph, is_Matrix, start, end, cur_depth_limit)
        if len(path) == 0 and cur_depth_limit < deepest_depth: 
            cur_depth_limit += 1
        else: 
            found = True
    
    
    return path


#main method to test the iterative deepening search method. 
if __name__ == "__main__":
    #print(iterative_deepening_search(read_graph(True),True,'a','n'))
    #print(iterative_deepening_search(read_graph(False), False,'a','n'))

    print(calculate_deepest_depth(read_graph(True), True, 'a', 0))
    print(calculate_deepest_depth(read_graph(False), False, 'a', 0))
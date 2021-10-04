# Author: Matt Williams
# Version: 09/15/21

from read_graph import read_graph




# Depth Limited Search Algorithm
# returns a list of nodes, or an empty list if no path exists. 

# graph: The given directed graph as either an adjacency matrix or adjacency list. 
# is_Matrix: boolean value telling the method which type the graph variable is.
# start: Where should the algorithm start the search. 
# end: Where is the destination of the search. 
# depth_limit: the depth limit of the search (inclusive). 
def depth_limited_search(graph, is_Matrix, start, end, depth_limit):
    if start == end: 
        return [start]

    if depth_limit == 0:
        return []    

    if is_Matrix:
        return dls_with_matrix_util(graph, start,end, depth_limit, 0, [])

    return dls_with_list_util(graph, start, end, depth_limit, 0, [])

   
    
# Recursive Utility function for Depth Limited Search using an adjacency list.
# This function returns a list of nodes, or an empty list if no path exists. 

# adj_list: The given directed graph as an adjacency list. 
# start: Where should the algorithm start the search. 
# end: Where is the destination of the search. 
# depth_limit: the depth limit of the search (inclusive).
# cur_depth: The depth at the current iteration. 
# path: The path taken up to the current iteration.  
def dls_with_list_util(adj_list, start, end, depth_limit, cur_depth, path):
    

    if cur_depth > depth_limit:
        return []
    
    if start == end: 

        path.append(end)
        return path
    

    path.append(start)
    neighbors = adj_list[ord(start) - ord('a')]
    
    for n in neighbors:
        updated_path = dls_with_list_util(adj_list, n, end, depth_limit, cur_depth + 1, path.copy())
        
        if len(updated_path) != 0: 
            return updated_path


    return []

# Recursive Utility function for Depth Limited Search using an adjacency matrix.
# This function returns a list of nodes, or an empty list if no path exists. 

# adj_mat The given directed graph as an adjacency matrix. 
# start: Where should the algorithm start the search? 
# end: Where is the destination of the search?
# depth_limit: the depth limit of the search (inclusive).
# cur_depth: The depth at the current iteration. 
# path: The path taken up to the current iteration.  
def dls_with_matrix_util(adj_mat, start, end, depth_limit, cur_depth, path):

    if cur_depth > depth_limit:
        return []
    
    if start == end: 
        path.append(end)
        return path

    

    path.append(start)
    adj_row = adj_mat[ord(start) - ord('a')]
    
    for i in range(len(adj_row)):
        if adj_row[i] == 1: 
            new_start = chr(i + ord('a'))
            updated_path = dls_with_matrix_util(adj_mat, new_start, end, depth_limit, cur_depth + 1, path.copy())

            if len(updated_path) != 0:
                return updated_path


    return []

# main method to test depth limited search methods above
if __name__ == "__main__":

    print(depth_limited_search(read_graph(False), False, 'a', 'n', 2))
    #used to test if increasing depth gives us a different result (which it should)
    print(depth_limited_search(read_graph(False), False, 'a', 'n', 4))

    print(depth_limited_search(read_graph(True), True, 'a', 'n', 2))
    #used to test if increasing depth gives us a diffedrent result (which it should)
    print(depth_limited_search(read_graph(True), True, 'a', 'n', 4))


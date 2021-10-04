# Auther: Matt Williams
# Version: 9/15/2021


from iterative_deepening_search import iterative_deepening_search
from depth_limited_search import depth_limited_search
from read_graph import read_graph


DLS, ADJ_MAT = '1', '1'
IDS, ADJ_LIST = '2', '2'

# A method used to print the path found by the chosen algorithm. 
# If no path was found, the method will print that no path was found. 
def print_graph(path):

    if len(path) >= 1:
        start = path[0]
        end = path[len(path) - 1]

        path_str = start

        for i in range(1,len(path)):
            path_str += "->" + path[i]



        print("The Path from", start, "to", end, "is:")
        print(path_str)



    else: 
        print("No path was found with the given input.")


# The main method of the assignment. 
# The driver will first ask you which search algorithm you would like to run, then ask if you are entering an
# adjacency matrix or list. The driver will then take in the appropriate input based on which algorithm was chosen. 
# The driver gives the user the option to run another search with new inputs if the user wants to. 
if __name__ == "__main__":

    stop = False

    while not stop:
        search_algo = 0
        while search_algo != DLS and search_algo != IDS:
            print("Which Search Algorithm would you like to run?")
            print("Type 1 for Depth Limited Search.")
            print("Type 2 for Iterative Deepending Search.")
            search_algo = input()

        input_type = 0
        while input_type != ADJ_MAT and input_type != ADJ_LIST:
            print("Would you like to use an Adjacency Matrix or Adjacency List?")
            print("Type 1 for Adjacency Matrix.")
            print("Type 2 for Adjacency List.")
            input_type = input()


        is_Matrix = True if input_type == ADJ_MAT else False

        print("Please Enter the Adjacency Matrix/List.")
        graph = input()
        graph = read_graph(is_Matrix)

        print("Where would you like to start the search?")
        start = input()

        print ("What is the destination for this search?")
        end = input()

        if search_algo == DLS: 
            print("You Have Chosen Depth Limited Search. Please Enter the depth limit.")
            depth_limit = int(input())

            print_graph(depth_limited_search(graph, is_Matrix, start, end, depth_limit))
            
        else: 
            print_graph(iterative_deepening_search(graph, is_Matrix, start, end))

        print("Would you like to do another search?")
        print("Type 1 for yes, type anything else for no.")
        ans = input()

        if ans == '1':
            stop = True





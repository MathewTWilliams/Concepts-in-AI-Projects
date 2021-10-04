#Author: Matt Williams
#Version: 9/15/2021


# The file mentioned below is formatted as follows: 
# Current Node:nodes that can be reached from the Current Node
# each node that can be reached is separated by a comma (,) 
file_Name = "Search_Input.txt"
next_Line_Character = '\n'

# A method used to read in the graph data from "Search_Input.txt".
# The method returns an adjacency list or matrix, depending on the boolean value
# passed in to the method. 

# return_Matrix: a boolean value to determine the return value of the method. 
def read_graph(return_Matrix):
    
    data = []
    with open(file_Name, "r+") as file:
        lines = file.readlines()

        for i in range(len(lines)):
            data.append([])


        if return_Matrix: 
            for i in range(len(lines)):
                for j in range(len(lines)):
                    data[i].append(0)
            

        for line in lines:
            contents = line.split(":")
            currentNode = contents[0]
            connectedNodes = contents[1].split(",")

            #need to remove the end of line character from the last node in the list of connected nodes
            last_Index = len(connectedNodes) - 1
            connectedNodes[last_Index] = connectedNodes[last_Index].replace(next_Line_Character,'') 



            # if there is only 1 element and it is a empty string, move to the next line
            if len(connectedNodes) == 1 and connectedNodes[0] == '':
                continue

            row_num = ord(currentNode) - ord('a')

            if return_Matrix:
                for node in connectedNodes:
                    column_num = ord(node) - ord('a')
                    data[row_num][column_num] = 1

            else: 
                data[row_num] = connectedNodes


    return data

            
            
# main function to test the Read_Graph Method
if __name__ == "__main__":
    adj_matrix = read_graph(True)
    adj_list = read_graph(False)

    print("adj_matrix:")
    for row in adj_matrix:
        print(row)

    print("------------------------------------------")
    print("adj_list:")
    for row in adj_list:
        print(row)
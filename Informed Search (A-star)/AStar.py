#Author: Matt Williams
#Version: 9/24/2021


from constants import *

# built in python library that allows us to use min heap queue functions on python lists.
# https://docs.python.org/3/library/heapq.html 
import heapq


# The AStar class holds the implementation of the A* pathfinding algorithm. 
class AStar(): 

    # Constructor
    def __init__(self, board, start_x, start_y, end_x, end_y, diagonal_allowed):
        self.board = board
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.diagonal_allowed = diagonal_allowed

    # Given an x and y position, return True if that position represents a valid neighbor. 
    # Otherwise, return False. 
    def is_valid_neighbor(self, x_pos, y_pos): 

        if x_pos < 0 or y_pos < 0 or x_pos >= grid_size_x or y_pos >= grid_size_y:
            return False 

        return self.board[x_pos][y_pos] not in [obstacle_char, start_char]

    # Given an x and y position, return a list of all valid neighbors around the given position. 
    # The method returns a list of 2-tuples. Where each tuple represents the x and y coordinate of a valid neighbor. 
    def find_valid_neighbors(self, x_pos, y_pos):
        valid_neighbors = []

        possible_valid_neighbors = [(x_pos + 1, y_pos), (x_pos-1, y_pos), (x_pos, y_pos+1), (x_pos, y_pos-1)]

        if self.diagonal_allowed: 
            possible_valid_neighbors.append((x_pos+1, y_pos+1))
            possible_valid_neighbors.append((x_pos+1, y_pos-1))
            possible_valid_neighbors.append((x_pos-1, y_pos+1))
            possible_valid_neighbors.append((x_pos-1, y_pos-1))

        for x,y in possible_valid_neighbors:
            if self.is_valid_neighbor(x,y):
                valid_neighbors.append((x,y))

        return valid_neighbors


    # Given 2 x,y coordinate pairs, this method returns the cost it would take to 
    # move from one position to another. 
    def get_move_cost(self, cur_x, cur_y, next_x, next_y):
        x_diff = abs(next_x - cur_x)
        y_diff = abs(next_y - cur_y)

        if x_diff == 0 and y_diff == 0:
            return 0

        if x_diff == 1 and y_diff == 1: 
            return diag_move_cost
        
        return reg_move_cost

    #given 2 x,y coordinate pairs, this method returns the manhattan distance between them.
    def get_manhattan_distance(self, x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

    # This method runs the A* star algorithm.
    # This method returns a list of 2-tuples, where each tuple represents
    # a x,y coordinate pair of a position to traverse.  
    def run_algorithm(self):
        cur_x = self.start_x
        cur_y = self.start_y
        prev_g_cost = 0
        cur_path = []

        # each item in the queue will be a 5-tuple (f_cost, 1/g_cost, x_pos, y_pos, cur_path)
        # heapq functions will sort tuples based on first element, then the second and so on.
        # we use the reciprocal of the g_cost so that paths that have traveled the furthest
        # from the start position are prioritized first, give us DFS like behavoir. 
        priority_queue = []

        while cur_x != self.end_x or cur_y != self.end_y:
            
            valid_neighbors = self.find_valid_neighbors(cur_x, cur_y)

            for x_pos, y_pos in valid_neighbors: 
                g_cost = prev_g_cost + self.get_move_cost(cur_x, cur_y, x_pos, y_pos)
                h_cost = self.get_manhattan_distance(x_pos, y_pos, self.end_x, self.end_y)
                f_cost = g_cost + h_cost

                updated_path = cur_path.copy()
                updated_path.append((x_pos, y_pos))

                
                queue_tuple = (f_cost, 1/g_cost, x_pos, y_pos, updated_path)
                heapq.heappush(priority_queue, queue_tuple)

            # ___ meaning we don't need to store the f-score value in the tuple
            __, prev_g_cost, cur_x, cur_y, cur_path = heapq.heappop(priority_queue)

            #undo the reciprocal to get original g_cost
            prev_g_cost = 1/prev_g_cost

        
        #return the entire cur_path except for the last element, which is the goal location
        return cur_path[:len(cur_path) - 1]


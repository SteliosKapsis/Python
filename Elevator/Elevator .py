#!/usr/bin/env python
# coding: utf-8

# In[2]:


import copy
import sys
import numpy

sys.setrecursionlimit(10**6) #limit gia anadromh sunarthsewn 

CUR_FLOOR = 0
TENANTS_FLOOR_1 = 1
TENANTS_FLOOR_2 = 2
TENANTS_FLOOR_3 = 3
TENANTS_FLOOR_4 = 4
ELEVATOR_SIZE = 5
ELEVATOR_MAX_SIZE = 10

def display(List):

	array = numpy.array(List)
	print(array, "\n")

def displayState(state):
	if not state ==  None:
		print("Floor: ", state[CUR_FLOOR], \
			" [1: ", state[TENANTS_FLOOR_1], \
			"] [2: ", state[TENANTS_FLOOR_2], \
			"] [3: ", state[TENANTS_FLOOR_3], \
			"] [4: ", state[TENANTS_FLOOR_4], \
			"] elevator size: ", state[ELEVATOR_SIZE], \
			sep = '')
	else:
		print("Not accepted state")

#Operators
def GoToFloor1(state):
	if state[ELEVATOR_SIZE] < ELEVATOR_MAX_SIZE and state[TENANTS_FLOOR_1]>0:
		if state[TENANTS_FLOOR_1] > ELEVATOR_MAX_SIZE - state[ELEVATOR_SIZE]:
			new_state = [1] + \
			[state[TENANTS_FLOOR_1] + state[ELEVATOR_SIZE] - ELEVATOR_MAX_SIZE] + \
			[state[TENANTS_FLOOR_2]] + \
			[state[TENANTS_FLOOR_3]] + \
			[state[TENANTS_FLOOR_4]] + \
			[10]
		else:
			new_state = [1] + \
			[0] + \
			[state[TENANTS_FLOOR_2]] + \
			[state[TENANTS_FLOOR_3]] + \
			[state[TENANTS_FLOOR_4]] + \
			[state[TENANTS_FLOOR_1] + state[ELEVATOR_SIZE]]

		return new_state


def GoToFloor2(state):
	if state[ELEVATOR_SIZE] < ELEVATOR_MAX_SIZE and state[TENANTS_FLOOR_2]>0:
		if state[TENANTS_FLOOR_2] > ELEVATOR_MAX_SIZE - state[ELEVATOR_SIZE]:
			new_state = [2] + \
			[state[TENANTS_FLOOR_1]] + \
			[state[TENANTS_FLOOR_2] + state[ELEVATOR_SIZE] - ELEVATOR_MAX_SIZE] + \
			[state[TENANTS_FLOOR_3]] + \
			[state[TENANTS_FLOOR_4]] + \
			[10]
		else:
			new_state = [2] + \
			[state[TENANTS_FLOOR_1]] + \
			[0] + \
			[state[TENANTS_FLOOR_3]] + \
			[state[TENANTS_FLOOR_4]] + \
			[state[TENANTS_FLOOR_2] + state[ELEVATOR_SIZE]]

		return new_state

def GoToFloor3(state):
	if state[ELEVATOR_SIZE] < ELEVATOR_MAX_SIZE and state[TENANTS_FLOOR_3]>0:
		if state[TENANTS_FLOOR_3] > ELEVATOR_MAX_SIZE - state[ELEVATOR_SIZE]:
			new_state = [3] + \
			[state[TENANTS_FLOOR_1]] + \
			[state[TENANTS_FLOOR_2]] + \
			[state[TENANTS_FLOOR_3] + state[ELEVATOR_SIZE] - ELEVATOR_MAX_SIZE] + \
			[state[TENANTS_FLOOR_4]] + \
			[10]
		else:
			new_state = [3] + \
			[state[TENANTS_FLOOR_1]] + \
			[state[TENANTS_FLOOR_2]] + \
			[0] + \
			[state[TENANTS_FLOOR_4]] + \
			[state[TENANTS_FLOOR_3] + state[ELEVATOR_SIZE]]

		return new_state

def GoToFloor4(state):
	if state[ELEVATOR_SIZE] < ELEVATOR_MAX_SIZE and state[TENANTS_FLOOR_4]>0:
		if state[TENANTS_FLOOR_4] > ELEVATOR_MAX_SIZE - state[ELEVATOR_SIZE]:
			new_state = [4] + \
			[state[TENANTS_FLOOR_1]] + \
			[state[TENANTS_FLOOR_2]] + \
			[state[TENANTS_FLOOR_3]] + \
			[state[TENANTS_FLOOR_4] + state[ELEVATOR_SIZE] - ELEVATOR_MAX_SIZE] + \
			[10]
		else:
			new_state = [4] + \
			[state[TENANTS_FLOOR_1]] + \
			[state[TENANTS_FLOOR_2]] + \
			[state[TENANTS_FLOOR_3]] + \
			[0] + \
			[state[TENANTS_FLOOR_4] + state[ELEVATOR_SIZE]]

		return new_state

def GoToFloor0(state):
	if (state[ELEVATOR_SIZE] == ELEVATOR_MAX_SIZE) or (state[TENANTS_FLOOR_1] == 0\
		and state[TENANTS_FLOOR_2] == 0 and state[TENANTS_FLOOR_3] == 0 and state[TENANTS_FLOOR_4] == 0):
		new_state = [0] + \
		[state[TENANTS_FLOOR_1]] + \
		[state[TENANTS_FLOOR_2]] + \
		[state[TENANTS_FLOOR_3]] + \
		[state[TENANTS_FLOOR_4]] + \
		[0]

		return new_state
	

def find_children(state):
    
    children=[]
    
    floor0_state=copy.deepcopy(state)
    floor1_state=copy.deepcopy(state)
    floor2_state=copy.deepcopy(state)
    floor3_state=copy.deepcopy(state)
    floor4_state=copy.deepcopy(state)

    floor0_child=GoToFloor0(floor0_state)
    floor1_child=GoToFloor1(floor1_state)
    floor2_child=GoToFloor2(floor2_state)
    floor3_child=GoToFloor3(floor3_state)
    floor4_child=GoToFloor4(floor4_state)

    if floor0_child!=None: 
        children.append(floor0_child)

    if floor1_child!=None: 
        children.append(floor1_child)

    if floor2_child!=None: 
        children.append(floor2_child)

    if floor3_child!=None: 
        children.append(floor3_child)

    if floor4_child!=None: 
        children.append(floor4_child)

    return children


def expand_front(front, method):  
	if method=='DFS':
		if front:
			node=front.pop(0)
			for child in find_children(node):
			    front.insert(0,child)

	elif method=='BFS':
		if front:
			node=front.pop(0)
			for child in find_children(node):
				front.append(child)

	print("Front:")
	display(front)
    
	return front


def extend_queue(queue, method):
    if method=='DFS':
        
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])#pairnoume thn teleutaia katastash pou brisketai sthn oura twn monopatiwn
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0, path)
            


    elif method=='BFS':
        
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
		
    print("QUEUE:")
    display(queue)
   
    return queue_copy

	
def find_solution(front, queue, closed, goal, method):


	if not front:
		print('_NO_SOLUTION_FOUND_')

	elif front[0] in closed:
		new_front=copy.deepcopy(front)
		new_front.pop(0)

		#
		new_queue=copy.deepcopy(queue)
		new_queue.pop(0)
		#

		find_solution(new_front, new_queue, closed, goal, method)
		#find_solution(new_front, closed, method)

	# elif is_goal_state(front[0]):
	elif front[0]==goal:
		print('_GOAL_FOUND_')
		display(front[0])
		print('_LAST QUEUE_')
		display(queue)
		print('_PATH_')
		display(queue[0])
	else:
		closed.append(front[0])
		front_copy=copy.deepcopy(front)
		front_children=expand_front(front_copy, method)

		#
		queue_copy=copy.deepcopy(queue)
		queue_children=extend_queue(queue_copy, method)
		#

		closed_copy=copy.deepcopy(closed)
		find_solution(front_children, queue_children, closed_copy, goal, method)
		#find_solution(front_children, closed_copy, method)



# [Current floor, floor 1, floor 2, floor 3, floor 4, Current space ]
init_state = [0, 12, 3, 7, 8, 0]

goal = [0, 0, 0, 0, 0, 0]
'''
method='DFS'


print('____BEGIN__SEARCHING____')
find_solution([init_state], [[init_state]], [], goal, method)
print('____END__SEARCHING____\n')

'''
method='BFS'

print('____BEGIN__SEARCHING____')
find_solution([init_state], [[init_state]], [], goal, method)
print('____END__SEARCHING____')


# In[ ]:





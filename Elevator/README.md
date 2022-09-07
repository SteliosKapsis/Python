Python Problem using BFS and DFS algorithm.
Problem Description: 

Title: Building Evacuation using an Elevator

Description: The elevator of a multistory building goes in to auto-mode when the police commands to evacuate the building. The building has four stories (1-4) and a 
ground floor (0) and one elevator.The capacity of the elevator is ten (10) people. The first floor has twelve (12) residents, the second floor has three(3) residents, 
the third floor has seven (7) residents and the fourth floor has eight (8) residents. When the police orders for the evacuation of the building, the elevator is at ground 
floor (0) and is empty. The elevator can go up or down and from any floor to any floor(e.g. it can go from the first floor to the third floor without stopping anywhere in
between or from the ground floor to the fourth floor without stopping anywhere in between etc) considering that it is not at full capacity and that there is at least one 
resident at the floor that it "wants"/"needs" to go. When the elevator reaches a floor all the residents can go in as long as the capacity is not full (MAX_CAPACITY = 10).
The other residents have to wait for their turn to get inside(if there are any left). The elevator can go from any floor to the ground level only if the 
capacity = MAX_CAPACITY or there are no more residents left waiting inside the building.

Point of the Problem: The point of this problem is to evacuate the building using the elevator, in other words every resident has to be at ground level when the algorithms
stop running.

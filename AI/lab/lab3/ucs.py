initial_state = "Arad"
goal_state = "Bucharest"

state_space = [
    ['Arad', 'Zerind', 75],
    ['Arad', 'Timisoara', 118],
    ['Arad', 'Sibiu', 140],
    ['Zerind', 'Oradea', 71],
    ['Oradea', 'Sibiu', 151],
    ['Sibiu', 'Rimnicu Vilcea', 80],
    ['Sibiu', 'Fagaras', 99],
    ['Fagaras', 'Bucharest', 211],
    ['Timisoara', 'Lugoj', 111],
    ['Lugoj', 'Mehadia', 70],
    ['Mehadia', 'Drobeta', 75],
    ['Drobeta', 'Craiova', 120],
    ['Craiova', 'Rimnicu Vilcea', 146],
    ['Rimnicu Vilcea', 'Pitesti', 97],
    ['Craiova', 'Pitesti', 138],
    ['Pitesti', 'Bucharest', 101],
    ['Bucharest', 'Giurgiu', 90],
    ['Bucharest', 'Urziceni', 85],
    ['Urziceni', 'Vaslui', 142],
    ['Urziceni', 'Hirsova', 98],
    ['Hirsova', 'Eforie', 86],
    ['Vaslui', 'lasi', 92],
    ['lasi', 'Neamt', 87]
]

class Node:
  def __init__(self, state=None, parent=None, cost=0):
    self.state = state
    self.parent = parent
    self.cost = cost

def expandAndReturnChildren(state_space, node):
    children = []
    for [m,n,c] in state_space:
        if m == node.state:
            childnode = Node(n, node, c)
            children.append(childnode)
        elif n == node.state:
            childnode = Node(m, node, c)
            children.append(childnode)
    return children

# visualized, seems work!
def computePathCost(node):
    path_cost = 0
    while node is not None:
        path_cost += node.cost
        node = node.parent
    return path_cost


def ucs(state_space, initial_state, goal_state):
    frontier = []
    explored = []
    found_goal = False
    frontier.append(Node(initial_state, None))

    while not found_goal:
        # expand the first in the frontier
        children = expandAndReturnChildren(state_space, frontier[0])

        # children.sort(key=computePathCost)
        frontier.sort(key=computePathCost)

        # copy the node to the explored set
        explored.append(frontier[0])
        print(f"Parent: {frontier[0].state}, PathCost: {computePathCost(frontier[0])}", end="")

        # ucs test goal when expanded but not while added to frontier
        # goal test
        if frontier[0].state == goal_state:
            found_goal = True
            goal_node = frontier[0]
            # print(goal_node.state)
            break

        # remove the expanded node from the frontier
        del frontier[0]

        # # sort the children based on their path cost to the state.
        # children.sort(key=computePathCost)
        
        # loop through the children
        for child in children:
            # find redundant path
            # if same state is in frontier, compare their path cost, the lower cost node stay in frontier.
            redundant_node = next((f for f in frontier if f.state == child.state), None)
            
            # add this node to frontier and remove the old redundant path from frontier
            if redundant_node:
                if computePathCost(child) < computePathCost(redundant_node):
                    frontier.remove(redundant_node)
                # else, this new child has lower priority, do not add it to frontier!
                else:
                    continue
            # check if a node was expanded, avoid loopy path
            if not (child.state in [e.state for e in explored]):
                # add child to the frontiers
                frontier.append(child)
        print()

    solution = [goal_node.state]
    trace_node = goal_node
    while trace_node.parent is not None:
        solution.insert(0, trace_node.parent.state)
        trace_node = trace_node.parent
    
    return solution

print('Solution: ' + str(ucs(state_space, initial_state, goal_state)))

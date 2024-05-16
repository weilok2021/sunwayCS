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

remaining_state_space = [

]


class Node:
  def __init__(self, state=None, parent=None):
    self.state = state
    self.parent = parent

def expandAndReturnChildren(state_space, node):
    children = []
    for [m,n,c] in state_space:
        if m == node.state:
            childnode = Node(n, node)
            children.append(childnode)
        elif n == node.state:
            childnode = Node(m, node)
            children.append(childnode)
    return children

def bfs(state_space, initial_state, goal_state):
    frontier = []
    explored = []
    found_goal = False
    frontier.append(Node(initial_state, None))

    while not found_goal:
        # expand the first in the frontier
        children = expandAndReturnChildren(state_space, frontier[0])
        # copy the node to the explored set
        print(f"Parent: {frontier[0].state}, ", end="")
        explored.append(frontier[0])
        # remove the expanded node from the frontier
        del frontier[0]

        # loop through the children
        for child in children:
            # print(f" Child: {child.state}", end="")
            
            # check if a node was expanded or generated previously
            if not (child.state in [e.state for e in explored]) and not (child.state in [f.state for f in frontier]):
            # goal test
                if child.state == goal_state:
                    found_goal = True
                    goal_node = child
                    # print(goal_node.state)
                    break
                # add child to the frontiers
                frontier.append(child)
        print()

    solution = [goal_node.state]
    trace_node = goal_node
    while trace_node.parent is not None:
        solution.insert(0, trace_node.parent.state)
        trace_node = trace_node.parent
    
    return solution

print('Solution: ' + str(bfs(state_space, initial_state, goal_state)))

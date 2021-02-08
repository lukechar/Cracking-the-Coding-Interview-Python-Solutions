# 4-1: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

def solution(graph, node1, node2):
    # BFS is better than DFS for finding path between two points
    queue = []  # start with an empty queue
    marked = []  # mark all nodes that are added to the queue

    queue.append(node1)  # start at node1 and place into queue

    while len(queue):  # continue searching until queue is empty
        node = queue.pop(0)  # remove node at front of queue
        if node == node2:
            return True  # we found node2! The path between node1 and node2 exists - return True
        for adj_node in graph[node]:  # loop through all neighbors of node
            if adj_node not in marked:  # if we haven't added this node to the queue yet, add it to end of queue and mark it
                queue.append(adj_node)
                marked.append(adj_node)

    return False  # we checked all nodes connected to node1 and did not find node2 - return False
    

# Test solution
if __name__ == "__main__":
    # Note: this is the graph provided as an example of a directed graph on pg 106
    graph_1 = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [2],
        4: [6],
        5: [4],
        6: [5],
    }
    test_cases = {
        (0, 2): True,
        (0, 4): False,
        (5, 6): True,
        (6, 2): False,
        (6, 4): True,
        (1, 5): False
    }

    fails = 0
    for case in test_cases:
        try:
            res = solution(graph_1, *case)
            correct = test_cases.get(case)
            assert(res == correct)
        except AssertionError:
            fails += 1
            print(f'\nCase: {case[0]}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        
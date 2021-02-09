# 4-7: Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of 
# projets, where the second project is dependent on the first project). All of a project's dpendencies must 
# be built before the project is. Find a build order that will allow the projects to be built. If there is 
# no valid build order, return an error (note: changing this to return None to simplify testing).

def solution(projects, deps):
    # Construct directed graph with dependencies list
    dep_graph = dict()
    # Make each project a key in the hash table
    for project in projects:
        dep_graph[project] = None
    # Iterate through dependency list and add dependencies as edge
    # Note: ('a', 'd') -> 'd' depends on 'a'
    for dep in deps:
        dep_graph[dep[1]] = dep[0]
    
    build_order = []
    # Find all projects without dependencies - built these first.
    for proj in dep_graph:
        if dep_graph[proj] is None:
            build_order.append(proj)
    # If no such project exists, return None immeaditely.
    if len(build_order) == 0:
        return None
    # If no dependencies at all, we're done
    if len(build_order) == len(projects):
        return build_order

    # Start at latest project built and use BFS to check for path and return if found, otherwise, return None
    start_proj = build_order[-1]
    queue = [start_proj]
    while len(queue) > 0:
        node = queue.pop(0)  # pop from front of queue
        for proj in dep_graph:  # look for this node (project) as a dependency in graph
            if dep_graph[proj] == node:
                build_order.append(proj)  # dependency satisfied -> add proj to build list
                queue.append(proj)  # proj built -> can add to queue to search from now

    # Were we able to build all projects (i.e. find a path)?
    if len(build_order) == len(projects):
        return build_order
    else:
        return None
    
# Test solution
if __name__ == "__main__":
    test_cases = [
        (['a','b','c','d','e','f'], [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]),  # case 1
         ['f','e','a','b','d','c'],  # case 1 solution
         ['e','f','a','b','d','c'],  # case 1 alternate solution (technically, 'e' can be built at any time as it has no dependencies and is not depended upon)
        (['a','b','c','d','e','f'], [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('a', 'f')]),  # case 2 - cyclical, as 'a' depends on 'f', but 'f' depends on 'a'
         None,  # case 2 solution
    ]

    fails = 0
    try:
        # case 1
        res = solution(test_cases[0][0], test_cases[0][1])
        correct = test_cases[1]
        correct_2 = test_cases[2]
        assert(res == correct or res == correct_2)

        # case 2
        res = solution(test_cases[3][0], test_cases[3][1])
        correct = test_cases[4]
        assert(res == correct)

    except AssertionError:
        fails += 1
        print(f'Solution returned: {solution(test_cases[0][0], test_cases[0][1])}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        
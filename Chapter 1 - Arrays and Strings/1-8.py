# 1.8: Zero Matrix - if an element of the input MxN matrix is 0, make all of the entries in its row and 
# column 0.

def solution(mat):
    if not mat:
        return mat
    M = len(mat)
    N = len(mat[0])
    row_indicies = []
    col_indicies = []
    # Find zero rows/cols
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                row_indicies.append(i)
                col_indicies.append(j)
    # Zero out all elements of matrix with zero_indices
    for i in range(M):
        for j in range(N):
            if i in row_indicies or j in col_indicies:
                mat[i][j] = 0
    return mat


# Test solution
if __name__ == "__main__":
    test_cases = [
        ([[3,2,5],[8,0,2],[1,5,3]], [[3,0,5],[0,0,0],[1,0,3]]),
        ([[3,2,5],[8,7,2],[1,5,3]], [[3,2,5],[8,7,2],[1,5,3]]),
        ([[3,2,5],[8,7,2],[1,5,0]], [[3,2,0],[8,7,0],[0,0,0]]),
        ([[0,2,5],[8,7,2],[1,0,3]], [[0,0,0],[0,0,2],[0,0,0]]),
    ]

    fails = 0
    passes = 0
    for case in test_cases:
        try:
            res = solution([x[:] for x in case[0]])
            correct = case[1]
            assert(res == correct)
            passes += 1
        except AssertionError:
            fails += 1
            print(f'\nCase: {case[0]}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print(f'\nAll {passes} cases passed! :D\n')
        
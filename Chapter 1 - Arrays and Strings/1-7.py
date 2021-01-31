# 1.7: Rotate matrix by 90 degrees (CCW)

def solution(mat):
    N = len(mat)
    new_mat = [[None] * N for row in range(N)]
    for i in range(N):
        for j in range(N):
            new_mat[i][j] = mat[j][i]  # swap i and j indicies
    return new_mat[::-1]  # reverse row order
    

# Test solution
if __name__ == "__main__":
    test_cases = [
        ([[3,2,5],[8,7,2],[1,5,3]], [[5,2,3],[2,7,5],[3,8,1]]),
        ([[1,2,3],[4,5,6],[7,8,9]], [[3,6,9],[2,5,8],[1,4,7]]),
    ]

    fails = 0
    for case in test_cases:
        try:
            res = solution(case[0])
            correct = case[1]
            assert(res == correct)
        except AssertionError:
            fails += 1
            print(f'\nCase: {case[0]}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        
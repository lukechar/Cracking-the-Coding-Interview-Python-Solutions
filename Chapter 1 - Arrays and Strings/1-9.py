# 1.9: String rotation

def solution(s1, s2):
    def isSubstring(potentialSubstring, potentialSuperstring):  # can only call this once according to problem
        print(potentialSubstring, potentialSuperstring)
        return potentialSubstring in potentialSuperstring

    n = len(s1)

    if len(s2) != n:
        return False

    return isSubstring(s1, s2 * 2)  #  better solution --> O(1)

    # Brute force --> O(n)
    # for x in range(n):
    #     if s1[x:] + s1[0:x] == s2:
    #         return True
    # return False
    

# Test solution
if __name__ == "__main__":
    test_cases = {
        ('waterbottle', 'erbottlewat'): True,
        ('hello', 'lleho'): False,
        ('cat', 'atc'): True,
    }

    fails = 0
    for case in test_cases:
        try:
            res = solution(*case)
            correct = test_cases[case]
            assert(res == correct)
        except AssertionError:
            fails += 1
            print(f'\nCase: {case}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        
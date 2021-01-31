# 1.1: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def solution(s):
    read = set()
    for character in s:
        if character in read:
            return False
        read.add(character)
    return True

# Test solution
if __name__ == "__main__":

    test_cases = {
        'hi there': False,
        'Case TESt': True,
        '': True,
        'what?': True,
        'close, but no Cigar': False
    }

    fails = 0
    for case in test_cases:
        try:
            res = solution(case)
            correct = test_cases[case]
            assert(res == correct)
        except AssertionError:
            fails += 1
            print(f'\nCase: {case}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        
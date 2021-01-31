# 1.3: Write a method to replace all the spaces in a string with ‘%20’. You may assume that the string 
# has sufficient space at the end to hold the additional characters and that you are given the “true” 
# length of the string. 

def solution(s):
    res = ''
    stripped_s = s.strip()
    SPACE_CHAR = '%20'
    for character in stripped_s:
        if character == ' ':
            res += SPACE_CHAR
        else:
            res += character
    return res


# Test solution
if __name__ == "__main__":

    test_cases = {
        'Mr John Smith    ': 'Mr%20John%20Smith',
        'Mr  Yo   Smith    ': 'Mr%20%20Yo%20%20%20Smith',
        ' Mr X': 'Mr%20X',
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
        
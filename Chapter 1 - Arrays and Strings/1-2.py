# 1.2: Given two strings, write a method to decide if one is a permutation of the other.

def solution(s1, s2):
    if len(s1) != len(s2):
        return False
    chars1 = dict()
    chars2 = dict()
    for char1, char2 in zip(s1, s2):
        if char1 in chars1:
            chars1[char1] += 1
        else:
            chars1[char1] = 1
        if char2 in chars2:
            chars2[char2] += 1
        else:
            chars2[char2] = 1
    return chars1 == chars2


# Test solution
if __name__ == "__main__":

    test_cases = {
        ('abcd', 'dabc'): True,
        ('abcd', 'abcd'): True,
        ('', ''): True,
        ('fghj', 'abcd'): False,
        ('erty', 'kjpy'): False,
        ('racecar', 'carrace'): True,
        ('cow', 'wow'): False,
    }

    fails = 0
    for case in test_cases:
        try:
            res = solution(case[0], case[1])
            correct = test_cases[case]
            assert(res == correct)
        except AssertionError:
            fails += 1
            print(f'\nCase: {case}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        
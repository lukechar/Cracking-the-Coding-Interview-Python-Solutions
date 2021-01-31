# 1.5: There are three types of edits that can be performed on strings: insert a character, remove a
# character, or replace a character. Given two strings, write a function to check if they are one
# edit (or zero edits) away.

def solution(s1, s2):
    if s1 == s2:
        return True
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s2) > len(s1):
        longer = s2
        shorter = s1
    else:
        longer = s1
        shorter = s2
    short_chars = dict()
    for c in shorter:
        if c in short_chars:
            short_chars[c] += 1
        else:
            short_chars[c] = 1
    diffs = 0
    for c in longer:
        if c not in short_chars:
            diffs += 1
        elif c in short_chars and short_chars[c] > 0:
            short_chars[c] -= 1
        else:
            diffs += 1
    if diffs <= 1:
        return True
    return False

# Test solution
if __name__ == "__main__":
    test_cases = {
        ('pale', 'ple'): True,
        ('pales', 'pale'): True,
        ('pale', 'bale'): True,
        ('pale', 'bake'): False,
        ('pale', 'pale'): True,
        ('sale', 'mail'): False,
        ('kale', 'dale'): True,
        ('Hello', 'helli'): False,
        ('Hello', 'hello'): True,
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
        
# 1.4: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is
# a word or phrase that is the same fowards and backwards. A permutation is a rearrangement of letters. The
# palindrome does not need to be limited to just dictionary words.

def solution(s):
    s_clean = s.replace(' ', '').lower()  # assume: ignore spaces and case
    letters = dict()
    for let in s_clean:
        if let in letters:
            letters[let] += 1
        else:
            letters[let] = 1
    odd = 0
    for letter in letters:
        if letters[letter] % 2 != 0:
            odd += 1
    if len(s_clean) % 2 == 0:
        if odd == 0:
            return True
        return False
    if odd == 1:
        return True
    return False


# Test solution
if __name__ == "__main__":
    test_cases = {
        'tact coa': True,
        'eaarccr': True,
        'earshot': False,
        'hello there': False,
        'Able was I ere I saw Elba': True,
        'So patient a nurse to nurse a patient so': False,
        'nond dot': True,
        'this is not a palindrome': False,
        'tra rast': True,
        'trarast': True,
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
        
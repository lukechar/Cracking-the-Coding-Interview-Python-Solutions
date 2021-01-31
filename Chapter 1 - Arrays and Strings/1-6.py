# 1.6: String compression scheme: hhhhyyyyrr --> h4y4r2, if compression is same length or longer, return original string.

def solution(s):
    if not len(s):
        return s

    compressed_s = ''

    curr_letter = s[0]
    curr_count = 1
    for x in range(1, len(s)):
        if s[x] == curr_letter:
            curr_count += 1
        else:
            compressed_s += curr_letter
            compressed_s += str(curr_count)
            curr_letter = s[x]
            curr_count = 1

    compressed_s += curr_letter
    compressed_s += str(curr_count)

    if len(s) <= len(compressed_s):
        return s
    return compressed_s
    

# Test solution
if __name__ == "__main__":
    test_cases = {
        'aabcccccaaa': 'a2b1c5a3',
        'abcdefg': 'abcdefg',
        'aastyut': 'aastyut',
        'aaaarrrttttt': 'a4r3t5',
        'TTTTbbbGGGGG': 'T4b3G5',
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
        
# #!/usr/bin/python -tt
"""
Copyright (c) 2022, Phil Samoei
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

"""


def match_ends(words):
    count = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
    return count


def front_x(words):
    list_1 = []
    list_2 = []

    for word in words:
        if word[0] == "x":
            list_1.append(word)
        else:
            list_2.append(word)

    return sorted(list_1) + sorted(list_2)


def sort_last(tuples):
    return sorted(tuples, key=lambda item: item[-1])


# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
def sort_participants(partcipants):
    """
    Sorts with multiple keys by returning tuple instead of a number.
    :param partcipants: (Student's Name, Marks out of 100 , Age)
    :return: Sorted (Student's Name, Marks out of 100 , Age)
    """
    return sorted(partcipants, key=lambda item: (100-item[1], item[-1]))

def test(got, expected):
    if got == expected:
        prefix = "PASSED "
    else:
        prefix = "FAILED"
    print(f"TEST {prefix} | Expected: {expected}, Got: {got}")


def main():
    print('Testing match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print("Testing front_x")
    print('match_ends')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print("Testing sort_last")
    test(sort_last(
        [(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)]
    )
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    test(
        sort_participants(
            [
                ('Alison', 50, 18),
                ('Terence', 75, 12),
                ('David', 75, 20),
                ('Jimmy', 90, 22),
                ('John', 45, 12)
            ]
        ),
        [('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]

    )


if __name__ == "__main__":
    main()

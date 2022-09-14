#!/usr/bin/python -tt
"""
Copyright (c) <year>, Phil Samoei
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

"""

def verbing(s):
    if len(s) < 3:
        return s
    if s[-3:] == "ing":
        return s+"ly"
    else:
        return s+"ing"


def test(got, expected):
    if got == expected:
        prefix = "PASSED"
    else:
        prefix = " FAILED "
    print(f"TEST {prefix} | got: {got} expected: {expected}")

def not_bad(s):
    if "not" in s and "bad" in s:
        bad_index = s.index("bad")
        not_index = s.index("not")
        if bad_index > not_index:
            return s[:not_index] + "good" + s[bad_index + 3:]
    return s


def front_back(a, b):
    is_a_even = len(a) % 2 == 0
    is_b_even = len(b) % 2 == 0

    if is_a_even:
        a_front = a[:len(a)//2]
        a_back = a[len(a) // 2:]
    else:
        a_front = a[:(len(a)//2)+1]
        a_back = a[(len(a) // 2)+1:]

    if is_b_even:
        b_front = b[:len(b)//2]
        b_back = b[len(b) // 2:]
    else:
        b_front = b[:(len(b)//2)+1]
        b_back = b[(len(b) // 2)+1:]

    return a_front+b_front+a_back+b_back

def main():
    print("running verbing tests...")
    test(verbing("hail"), "hailing")
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print("running not_bad tests...")
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print("running front_back tests...")
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == "__main__":
    main()

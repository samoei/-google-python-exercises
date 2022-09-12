# #!/usr/bin/python -tt
"""
Copyright (c) <year>, Phil Samoei
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

"""


# returns count or many if 10 or more
def donuts(count):
    return f"Number of donuts: {count}" if count < 10 else "Number of donuts: many"


def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]


def test(got, expected):
    if got == expected:
        prefix = " OK "
    else:
        prefix = " X "
    print(f"{prefix} got: {got} expected: {expected}")


def main():
    print("running donuts tests...")
    test(donuts(4), "Number of donuts: 4")
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print("running both ends tests...")
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')


if __name__ == "__main__":
    main()

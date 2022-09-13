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


def fix_start(s):
    new_str = s[1:]
    return s[0] + new_str.replace(s[0], "*")


def mix_up(a, b):
    return f"{b[:2]+a[2:]} {a[:2]+b[2:]}"


def main():
    print("running donuts tests...")
    test(donuts(4), "Number of donuts: 4")
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print("running both_ends() tests...")
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print("running fix_start() tests...")
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print("running mix_up() tests...")
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == "__main__":
    main()

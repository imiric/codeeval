#!/usr/bin/env python2
# DeveloperAuction - Reverse and Add
# https://www.codeeval.com/open_challenges/45/
# Author: Ivan Miric <imiric@gmail.com>
# Score: 100.0

import sys


def palindrome(n, gen=0):
    """Finds the first palindrome from the sum of `n` and its reverse.

    Returns the palindrome found and the number of generations it took."""
    strn = str(n)
    rev = strn[::-1]
    if strn == rev:
        return n, gen
    return palindrome(n+int(rev), gen+1)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test:
        continue
    num = int(test.strip())
    try:
        pal = palindrome(num)
    except RuntimeError:  # reached max recursion
        print "%d can't be calculated" % num
        continue
    print pal[1], pal[0]

test_cases.close()

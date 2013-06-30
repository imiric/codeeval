#!/usr/bin/env python2
# Happy Numbers
# https://www.codeeval.com/open_challenges/39/
# Author: Ivan Miric <imiric@gmail.com>
# Score: 100.0

import sys

checked = []

def is_happy(n):
    if n == 1:
        return True
    if n in checked:
        # stuck in a loop
        return False
    checked.append(n)
    sum_squares = 0
    for i in str(n):
        sum_squares += int(i)**2
    return is_happy(sum_squares)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test:
        continue
    checked = []
    num = int(test.strip())
    if is_happy(num):
        print 1
    else:
        print 0

test_cases.close()

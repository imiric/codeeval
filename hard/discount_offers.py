#!/usr/bin/env python2
# Milo - Discount Offers
# https://www.codeeval.com/open_challenges/48/
# Author: Ivan Miric <imiric@gmail.com>

import re
import sys


def factors(n):
    """Find all factors of n.

    Not the fastest function, but works for our purposes."""
    lo = 1
    hi = n
    fac = [lo, hi]
    while hi > lo:
        lo += 1
        if not hi % lo:
            fac += factors(hi / lo)
    return sorted(set(fac))

def common_factors(m, n):
    """Find all common factors (besides 1) of m and n."""
    facs = sorted(factors(m) + factors(n))
    return [j for i, j in enumerate(facs) if j != 1 and j == facs[i-1]]


class Assoc(object):
    def __init__(self, prod, cust, ss=0.0):
        self.prod = prod
        self.cust = cust
        self.ss = ss

    def __unicode__(self):
        return u"%s - %s: %.2f" % (self.prod, self.cust, self.ss)

    def __repr__(self):
        return "<%s:%s>" % (self.__class__.__name__, unicode(self))

    def __lt__(self, other):
        return self.ss < other.ss

    def __radd__(self, other):
        return other + self.ss


re_letters = re.compile('[a-z]', re.I)
re_vowels = re.compile('[aeiouy]', re.I)
re_cons = re.compile('[^aeiouy\s]', re.I)
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test:
        continue
    customers, products = [(t.split(','), t.split(','))[0]
                            for t in test.strip().split(';')]

    assocs = []
    for cust in customers:
        c = ''.join(re_letters.findall(cust))
        for pr in products:
            p = ''.join(re_letters.findall(pr))
            if len(p) % 2: # odd
                ss = len(re_cons.findall(c))
            else:          # even
                ss = len(re_vowels.findall(c)) * 1.5
            if common_factors(len(p), len(c)):
                ss *= 1.5
            assocs.append(Assoc(pr, cust, ss))

    def get_combination(a, ass):
        comb = [a]
        for i in ass:
            isin = [i.prod != comb[k].prod and i.cust != comb[k].cust for k in range(len(comb))]
            if all(isin):
                comb.append(i)
        return comb

    all_combs = []
    for a in assocs:
        all_combs.append(get_combination(a, assocs))

    #from pprint import pprint
    #pprint(all_combs)
    #import ipdb; ipdb.set_trace()

    max_ss = 0.0
    for c in all_combs:
        ss = sum(c)
        if ss > max_ss:
            max_ss = ss

    print "%.2f" % max_ss

test_cases.close()

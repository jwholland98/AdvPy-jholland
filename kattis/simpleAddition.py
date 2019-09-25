#!/usr/bin/env python

import sys

def test():
    inp, inp2 ='1', '9999999999999'
    assert(answer(inp,inp2)==10000000000000)
    inp, inp2 ='478302', '8839201'
    assert(answer(inp,inp2)==9317503)
    inp, inp2 ='0', '243'
    assert(answer(inp,inp2)==243)
    print('All test cases passed!')

def solve():
    inp = input()
    inp2 = input()
    print(answer(inp, inp2))

def answer(inp, inp2):
     return eval(inp)+eval(inp2)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
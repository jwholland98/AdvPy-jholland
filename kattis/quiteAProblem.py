#!/usr/bin/env python

import sys

inp=[]

def test():
    inp.extend(['lqoervasjdv','problem','lkjbproblemlkjbca','Problem','lavjbProblem', 'LVJBPROBLEMLKJDB', 'jkvlProblEM infinef', 'ctrl-z'])
    answers=['no','yes','yes','yes','yes','yes','yes']
    assert(answer()==answers)
    print('All test cases passed!')

def solve():
    global inp
    inp.append(input())
    while inp[-1]!='':
        inp.append(sys.stdin.readline())
    answers=answer()
    for i in answers:
        print(i)

def answer():
    global inp
    answers=[]
    for i in range(len(inp)-1):
        inp[i]=inp[i].lower()
        if 'problem' in inp[i]:
            answers.append('yes')
        else: answers.append('no')
    return answers

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
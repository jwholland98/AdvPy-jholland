#!/usr/bin/env python

import sys

def deleteSmallest(dic):
    min=list(dic.keys())[0]
    for i in dic:
        if dic[i]<dic[min]:
            min=i
    dic[min]-=1
    if dic[min]==0: del(dic[min])

def test():
    string = ['hi', 'answer', 'assessment']
    assert(answer(string[0])==0)
    assert(answer(string[1])==4)
    assert(answer(string[2])==4)
    print('All test cases passed!')

def solve():
    inp = input()
    print(answer(inp))

def answer(inp):
    letters={}
    for c in inp:
        if c in letters:
            letters[c]+=1
        else:
            letters.update({c:1})
    count=0
    while len(letters)>2:
        deleteSmallest(letters)
        count+=1
    return count

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
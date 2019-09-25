#!/usr/bin/env python

import sys

def test():
    inp=('Jesse Holland\nKaleb Neiginfind\nBarbara Skinner\nKaleb Neiginfind\nJose Antonio Gomez-Iglesias\nBruce Stanger\nBarbara Skinner\n***')
    people=solveForTest(inp)
    assert(winner(people)=='Runoff!')
    inp=('Jesse Holland\nMarti Graham\nKaleb Neiginfind\nJoseph Ivers\nKaleb Neiginfind\nJesse Holland\nKaleb Neiginfind\nBruce Stanger\nKaleb Neiginfind\nBarbara Skinner\nBarbara Skinner\n***')
    people=solveForTest(inp)
    assert(winner(people)=='Kaleb Neiginfind')
    inp=('Jesse Holland\nJesse Holland\nMart Graham')
    people=solveForTest(inp)
    assert(winner(people)=='Jesse Holland')
    print('All test cases passed')

def solveForTest(string):
    people={}
    inp=string.split('\n')
    for i in inp:
        if i=='***':
            break
        if i in people:
            people[i]+=1
        else:
            people.update({i:1})
    return people

def winner(people):
    lead=list(people.keys())[0]
    for i in people:
        if people[i]>people[lead]:
            lead=i
    for i in people:
        if people[i]==people[lead] and i != lead:
            return 'Runoff!'
    return lead
        
def solve():
    people={}
    while True:
        inp=input()
        if inp=='***':
            break
        if inp in people:
            people[inp]+=1
        else:
            people.update({inp:1})
    print(winner(people))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
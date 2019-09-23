#!/usr/bin/env python

import sys

def test():
    inp=('Penny Franklin\nConnie Froggatt\nBarbara Skinner\nConnie Froggatt\nJose Antonio Gomez-Iglesias\nConnie Froggatt\nBruce Stanger\nBarbara Skinner\nBarbara Skinner\n***')
    people=solveForTest(inp)
    assert(winner(people)=='Runoff!')
    inp=('Penny Franklin\nMarti Graham\nConnie Froggatt\nJoseph Ivers\nConnie Froggatt\nPenny Franklin\nConnie Froggatt\nBruce Stanger\nConnie Froggatt\nBarbara Skinner\nBarbara Skinner\n***')
    people=solveForTest(inp)
    assert(winner(people)=='Connie Froggatt')
    inp=('Penny Franklin\nPenny Franklin\nMart Graham')
    people=solveForTest(inp)
    assert(winner(people)=='Penny Franklin')
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
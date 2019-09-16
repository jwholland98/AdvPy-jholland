#!/usr/bin/env python

import sys

def makeList(string):
    return list(string)

def test():
    arr=[['E','S'],['T','W']]
    assert(answer(arr) == 3)
    arr=[['S','E','S'],['E','N','T']]
    assert(answer(arr) == 5)
    arr=[['E','S'],['S','W']]
    assert(answer(arr) == 'Out')
    arr=[['E','S'],['N','W']]
    assert(answer(arr) == 'Lost')
    print('All test cases passed')
    quit()

def answer(arr):
    x, y, count = 0, 0, 0
    while True:
        if x<0 or x>len(arr)-1 or y<0 or y>len(arr[0])-1:
            return 'Out'
        if arr[x][y] == 'F':
            return 'Lost'
        elif arr[x][y] == 'N':
            arr[x][y] = 'F'
            x-=1
        elif arr[x][y] == 'E':
            arr[x][y] = 'F'
            y+=1
        elif arr[x][y] == 'S':
            arr[x][y] = 'F'
            x+=1
        elif arr[x][y] == 'W':
            arr[x][y] = 'F'
            y-=1
        elif arr[x][y] == 'T':
            return count
        count+=1

def solve():
    R, C = input().split()
    arr = [None] * eval(R)
    for i in range(eval(R)):
        arr[i]=makeList(input())
    print(answer(arr))
    quit()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()

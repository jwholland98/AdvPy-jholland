#!/usr/bin/env python

import sys

dic=[]
visited=[]
transl=[]

def match(a, b):#recurse through dic to see if translation is correct
    global dic
    global visited
    flag=False
    if a==b: return True
    else:
        for i in range(len(dic)):
            if dic[i][0]==a:
                if i in visited:
                    return False
                visited.append(i)
                flag=match(dic[i][1], b)
            if flag==True: break
    return flag

def test():
    global dic
    global transl
    dic.extend([['c','t'],['i','r'],['k','p'],['o','c'],['r','o'],['t','e'],['t','f'],['u','h'],['w','p']])
    transl.extend([['we','we'],['can','the'],['work','people'],['it','of'],['out','the']])
    answer=['yes','no','no','yes','yes']
    assert(solve(True)==answer)
    print('All test cases passed')


def start():
    global dic
    global transl
    inp, inp2 = input().split()
    for i in range(eval(inp)):
        key, value = input().split()
        dic.append([key,value])
    for i in range(eval(inp2)):
        key, value = input().split()
        transl.append([key,value])
    solve()

def solve(test=False):
    if test: ret=[]
    global transl
    global visited
    for i in transl:
        flag=False
        if len(i[0])==len(i[1]):
            for c in range(len(i[0])):
                visited.clear()
                if not match(i[0][c], i[1][c]):
                    flag=True
            if flag==False:
                if test: ret.append('yes')
                else: print('yes')
            else:
                if test: ret.append('no')
                else: print('no')
        else:
            if test: ret.append('no')
            else: print('no')
    if test: return ret

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        start()
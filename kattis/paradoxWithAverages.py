#!/usr/bin/env python

def average(lst): 
    return sum(lst) / len(lst)

def find_best(lst):
    global cs_ave
    for i in range(len(lst)):
        if lst[i]>=cs_ave:
            if i == 0:
                return i
            else:
                return i-1


for i in range(eval(input())):
    inp = input()
    inp, inp2 = input().split()
    cs=list(map(int,input().split()))
    e=list(map(int,input().split()))
    cs.sort()
    cs_ave = average(cs)
    e_ave = average(e)
    num = 0
    #print(cs_ave, ' ', e_ave)
    while True:
        num+=1
        if num == eval(inp):
            break
        x = find_best(cs)
        e.append(cs[x])
        del cs[x]
        if(average(cs)>cs_ave and average(e)>e_ave):
            break
    print(num)



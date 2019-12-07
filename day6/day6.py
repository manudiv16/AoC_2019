from collections import deque

def read():
    lines = open("input").read().split("\n")
    return [x.split(")") for x in (lines)]

def main():
    dic = {}
    dic2 ={}
    nodes = read()
    for x in nodes:
        if x[0] not in dic:
            dic[x[0]]= []
        if x[0] not in dic2:
            dic2[x[0]] = []
        if x[1] not in dic2:
            dic2[x[1]]= []
        dic[x[0]] = dic[x[0]]+[x[1]]
        dic2[x[0]]= dic2[x[0]]+[x[1]]
        dic2[x[1]]= dic2[x[1]]+[x[0]]
    #print(dic)
    part1(dic)
    part2(dic2)


def part2(dic):
    D = {}
    Q = deque()
    Q.append(('YOU', 0))
    while Q:
        x,d = Q.popleft()
        if x in D:
            continue
        D[x] = d
        for y in dic[x]:
            Q.append((y,d+1))
    print(D["SAN"]-2)

def part1(dic):
    count = 0
    for clave in dic:
        count += sumdic(dic,clave)
    print(count)

def sumdic(dic,clave):
    sum=0
    for x in dic.get(clave,[]):
        sum += sumdic(dic,x)+1
    return sum


        

main()
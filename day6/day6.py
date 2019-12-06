

def read():
    relations = open("input_test").read().split("\n")
    relations = [x.split(")") for x in (relations)]
    
    return(relations)

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



def main():
    dic = {}
    nodes = read()
    for x in nodes:
        if x[0] not in dic:
            dic[x[0]]= []
        dic[x[0]]= dic[x[0]]+[x[1]]
    part1(dic)
    part2(dic)


main()
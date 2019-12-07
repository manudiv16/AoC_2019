dic = {}
dic2 = {}
def create_dictionarys(nodes):
    for x in nodes:
        if x[0] not in dic:
            dic[x[0]]= []
        if x[1] not in dic2:
            dic2[x[1]]= x[0]
        dic[x[0]] = dic[x[0]]+[x[1]]

def read():
    lines = open("input").read().split("\n")
    return [x.split(")") for x in (lines)]


def go_to_father(clave):
    array = []
    while True:
        if dic2[clave] == 'COM':
            array.append(dic2[clave])
            break
        else:
            array.append(dic2[clave])
            clave = dic2[clave]
    return array
    
    
def sum_tree(clave):
    sum=0
    for x in dic.get(clave,[]):
        sum += sum_tree(x)+1
    return sum

def part2():
    stack_YOU =go_to_father('YOU')
    stack_SAN = go_to_father('SAN')
    hola =[]
    for x in stack_YOU:
        if x not in hola:
            hola.append(x)
    for x in stack_SAN:
        if x in hola:
            hola.remove(x)
        else:
            hola.append(x)
    print(len(hola))

def part1():
    count = 0
    for clave in dic:
        count += sum_tree(clave)
    print(count)

def main():
    nodes = read()
    create_dictionarys(nodes)
    part1()
    part2()
        

main()
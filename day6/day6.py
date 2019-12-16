dic = {}
dic2 = {}

def create_dictionary_one(x): #only catch sons
    if x[0] not in dic:
        dic[x[0]] = []
    dic[x[0]] = dic[x[0]]+[x[1]]

def create_dictionary_two(x): # only catch father
    if x[1] not in dic2:
        dic2[x[1]] = x[0]

    
def create_dictionarys(nodes):
    map(create_dictionary_one,nodes)
    map(create_dictionary_two,nodes)
    

def read():
    lines = open("input").read().split("\n")
    return [x.split(")") for x in (lines)]

def go_to_father(clave,list_compare=[]): # creat list, you or san to COM
    if dic2[clave] == 'COM' or dic2[clave] is in list_compare:
        return [dic2[clave]]
    else:
        return [dic2[clave]]+go_to_father(dic2[clave])

def sum_tree(clave): # sum distance for all nodes 
    return sum(map(lambda x: sum_tree(x)+1, dic.get(clave, [])) )


def part2():
    stack_YOU = go_to_father('YOU')
    stack_SAN = go_to_father('SAN',stack_YOU)
    print(len(set(stack_YOU) ^ set(stack_SAN))) # lenth of diference elements of both lists


def part1():
    print(sum(map(lambda clave : sum_tree(clave),dic))) # sum of distances


def main():
    nodes = read()
    create_dictionarys(nodes)
    part1()
    part2()


main()
  

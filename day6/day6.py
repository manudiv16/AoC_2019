
def read():
    relations = open("input_test").read().split("\n")
    relations = [x.split(")") for x in (relations)]
    
    return(relations)

def main():
    dic = {}
    nodes = read()
    for x in nodes:
        if x[0] not in dic:
            dic[x[0]]= []
        dic[x[0]]= dic[x[0]]+[x[1]]
    ans = 0
    for x in dic:
        ans += sumdic(x,dic)
    print(ans)

def sumdic(clave,dic):
    sum = 0
    for planet in dic.get(clave,[]):
        sum += sumdic(planet,dic) + 1
    return sum
    


main()
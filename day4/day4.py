



def hasrep(x):
    number = str(x)
    new = []
    for n in number:
        if n in new:
            return True
        else:
            new.append(n)
    return False

def hasrep3(x):
    number = str(x)
    hola = any([(n==0 or number[n]!=number[n+1])and number[n]==number[n+1] and (n==len(number)-2) or number[n]!= number[n+2] for n in range(len(number)-2)])
    return hola
       
        
            
        
            

    

def manortomajor(x):
    number = str(x)
    no = sorted(number)
    ne = "".join(no)
    if number == ne:
        return True
    else:
        return False

def concat(zero,one,two,three,four,five):
    return int("%d%d%d%d%d%d" % (zero,one,two,three,four,five))

def part1():
    n=0
    for x in range(134792,675810):
        if hasrep(x) and manortomajor(x):
            n+=1
    print(n)

def part2():
    n=0
    for x in range(134792,675810):

        if not hasrep3(x) and manortomajor(x) :
            n+=1
    print(n)



def manin():
    part1()
    part2()

manin()


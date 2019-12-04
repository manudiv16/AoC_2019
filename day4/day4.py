

encapsule=[]

def hasrep(x):
    number = str(x)
    new = []
    for n in number:
        if n in new:
            return True
        else:
            new.append(n)
    return False
   
def manortomajor(x):
    number = str(x)
    no = sorted(number)
    ne = "".join(no)
    if number == ne:
        encapsule.append(number)
        return True
    else:
        return False

def part1():
    n=0
    for x in range(134792,675810):
        if hasrep(x) and manortomajor(x):
            n+=1
    return(n)

def part2():
    resposta = []
    for digits in encapsule:
        count = 0
        dianterior = ""
        n=0
        for di in digits:
            if di==dianterior:
                count = count + 1
                if n==5:
                    if count==1 and digits not in resposta:
                            resposta.append(digits)
            else:
                if count == 1 and digits not in resposta:
                    resposta.append(digits)
                count = 0
            n=n+1
            
            dianterior = di
    return (len(resposta))


def manin():
    print(part1())
    print(part2())

manin()


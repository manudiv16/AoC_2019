import simple 

def main():
    intcode = read()
    # start(intcode)
    start2(intcode)

def read():
    with open("input","r") as file:
        line = file.readline()
        intcode = map(int,line.split(","))
    return intcode

def start(intcode):
    x=0
    y=4
    r=0
    while (True):
        subcode = intcode[x:y]
        if subcode[0]==1:
            r= intcode[subcode[1]] + intcode[subcode[2]]
        elif subcode[0]==2:
            r= intcode[subcode[1]] * intcode[subcode[2]]
        elif subcode[0]==99:
            break
        intcode[subcode[3]] = r
        x = x + 4 
        y = y + 4
        if y > len(intcode)-1:
            break
    

def start2(intcode):

    for i in range(99):
        for j in range(99):
            intcode[1]=i
            intcode[2]=j
            start(intcode)
            if intcode[0]==19690720:
                break
            intcode = read()
        if intcode[0]==19690720:
                break
    print(intcode)


if __name__ == "__main__":
    main()
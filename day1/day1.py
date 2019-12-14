
calcule_fuel = lambda x: (x/3)-2
sum_fuel = lambda x :sum(calcule_fuel_two(x))


def part_two(doc):
    return str(sum(map(sum_fuel,doc)))

def calcule_fuel_two(mass):
    if calcule_fuel(mass) > 0:
        return [calcule_fuel(mass)]+calcule_fuel_two(calcule_fuel(mass))
    else :
        return []

def part_one(doc):
    return str(sum(map(calcule_fuel, doc)))

def read():
    document =  open("input").read().split("\n")
    return map(int,document)

    
doc = read()
print("part 1: "+ part_one(doc))
print("part 2: "+ part_two(doc))

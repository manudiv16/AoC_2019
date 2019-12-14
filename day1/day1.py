
calcule_fuel = lambda x: (x/3)-2
sum_fuel = lambda x :sum(calcule_fuel_two(x))

def part_one(doc):
   print("part 1: "+ str(sum(map(calcule_fuel, doc))))

def part_two(doc):
    print("part 2: "+ str(sum(map(sum_fuel,doc))))

def calcule_fuel_two(mass):
    if calcule_fuel(mass) > 0:
        return [calcule_fuel(mass)]+calcule_fuel_two(calcule_fuel(mass))
    else :
        return []

def raead():
    document =  open("input").read().split("\n")
    return map(int,document)

    
doc = raead()
part_one(doc)
part_two(doc)


     

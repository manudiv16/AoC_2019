import sys
doc = []


def part_one():
    fuel_sum = []
    for mass in doc:
        fuel_sum.append((mass/3)-2)
    print(sum(fuel_sum))


def part_two():
    fuel_sum = []
    for mass in doc:
        while mass > 0:
            mass = (mass/3)-2
            if mass > 0:
                fuel_sum.append(mass)
    print(sum(fuel_sum))


with open(str(sys.argv[1])) as file:
    for l in file:
        doc.append(int(l))
    part_one()
    part_two()

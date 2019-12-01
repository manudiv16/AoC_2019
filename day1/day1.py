import spart_ones 
part_two = []
part_one = []
with open(str(spart_ones.argv[1])) as file:
    for l in file:
        n = int(l)
        part_one.append((int(l) /3 )-2)
        while n > 0:
            n = (n /3 )-2
            if n > 0:
                part_two.append(n)




print(sum(part_one))
print(sum(part_two))


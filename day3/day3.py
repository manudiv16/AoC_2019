

coordenate = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

ordenades = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def get_points(wire_one):
    x = 0
    y = 0
    length = 0
    result = {}
    for movement in wire_one:
        d = movement[0]
        n = int(movement[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x += coordenate[d]
            y += ordenades[d]
            length += 1
            if (x, y) not in result:
                result[(x, y)] = length
    return result


def read():
    wire_one, wire_two, _ = open("input.txt").read().split("\n")
    return [x.split(",") for x in [wire_one, wire_two]]

def part1(points_wire_two,points_wire_one,path):
    
    result = min([abs(x)+abs(y)for (x, y) in path])
    print (result)

def part2(points_wire_one,points_wire_two,path):
    result = min([points_wire_one[p]+points_wire_two[p] for p in path])
    print (result)


def main():

    wire_one, wire_two = read()
    points_wire_one = get_points(wire_one)
    points_wire_two = get_points(wire_two)
    path = set(points_wire_one.keys()) & set(points_wire_two.keys())
    part1(points_wire_one,points_wire_two,path)
    part2(points_wire_one,points_wire_two,path)
    


main()
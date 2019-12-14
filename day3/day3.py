

coordenate = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

ordenades = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def get_points(A):
    x = 0
    y = 0
    length = 0
    result = {}
    for movement in A:
        for _ in range(int(movement[1:])):
            x += coordenate[movement[0]]
            y += ordenades[movement[0]]
            length += 1
            if (x, y) not in result:
                result[(x, y)] = length

    return result

        

def read():
    wire_one, wire_two, _ = open("input.txt").read().split("\n")
    return [x.split(",") for x in [wire_one, wire_two]]

def absolute(path):
    x,y = path
    return abs(x)+abs(y)

def part1(path):
    print(min(map(absolute, path)))



def part2(poin, path):
    points_wire_one,points_wire_two = poin
    print(min(map(lambda x :points_wire_one[x]+points_wire_two[x] , path )))


def main():

    wire_one, wire_two = read()
    poin = map(get_points, [wire_one, wire_two])
    def path(poin):
        x,y = poin
        return set(x.keys()) & set(y.keys())
    part1(path(poin))
    part2(poin, path(poin))


main()

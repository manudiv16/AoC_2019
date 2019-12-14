

coordenate = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

ordenades = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def get_points(A):
    x = 0
    y = 0
    length = 0
    result = {}
    for movement in A:
        assert movement[0] in ['L', 'R', 'U', 'D']
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


def part1( path):
    print(min(map(lambda (x, y): abs(x)+abs(y), path)))



def part2((points_wire_one, points_wire_two), path):
    print(min([points_wire_one[l]+points_wire_two[l] for l in path]))


def main():

    wire_one, wire_two = read()
    poin = map(get_points, [wire_one, wire_two])
    def path((x, y)): return set(x.keys()) & set(y.keys())
    part1(path(poin))
    part2(poin, path(poin))


main()

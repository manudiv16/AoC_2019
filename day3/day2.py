

up = "U"
down = "D"
left = "L"
right = "R"


def read():
    with open("input.txt","r") as file:
        wire_one = file.readline().rstrip().split(",")
        wire_two = file.readline().rstrip().split(",")
        
        print(wire_one)
        print(wire_two)


def create_table_of_segments(new_direction):
    if new_direction[0] == up:
        print((0),(int(new_direction[1:])))
        return ((0),(int(new_direction[1:])))
    elif new_direction[0] == down:
        print((0),(-1*int(new_direction[1:])))
        return ((0),(-1*int(new_direction[1:])))
    elif new_direction[0] == right:
        print((int(new_direction[1:])),(0))
        return ((int(new_direction[1:])),(0))
    elif new_direction[0] == left:
        print((-1*int(new_direction[1:])),(0))
        return ((-1*int(new_direction[1:])),(0)) 
    
def create_table(wire):
    last_section=(0,0)
    table_of_segments=()
    for recored in wire:
        table_of_segments = table_of_segments+(last_section,next_section_calcule(last_section,recored))
    print (table_of_segments)
    return table_of_segments

def next_section_calcule(last_section,recorded):
    next_sel = create_table_of_segments(recorded)
    return (last_section[0]+next_sel[0],last_section[1]+next_sel[1])
#read()
create_table_of_segments("R300")
create_table(['D837', 'R921', 'U838', 'R986', 'D441', 'L950', 'D530', 'L397', 'U41', 'L81', 'D60', 'L245', 'D75', 'R620', 'D455', 'L937', 'D180', 'R215', 'D684', 'R724', 'U561', 'R479', 'D353', 'L501'])
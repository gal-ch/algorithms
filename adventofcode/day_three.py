
# f1 = open('input1.txt', "r")
# content1 = f1.read()
# f2 = open('input2.txt', "r")
# content2 = f2.read()
all_values1 = []
all_values2 = []
with open('input2.txt', newline='') as infile:
    for line in infile:
        all_values1.extend(line.strip().split(','))

with open('input1.txt', newline='') as infile:
    for line in infile:
        all_values2.extend(line.strip().split(','))


def crossedWires(in_move):
    obj = {}
    x = y = cnt = 0
    for move in in_move:
        direction = move[0]
        direction_amount = int(move[1:])
        mx = my = 0
        if direction == 'L':
            mx += -1
        if direction == 'R':
            mx += 1
        if direction == 'U':
            my += 1
        if direction == 'D':
            my += -1

        for m in range(0, direction_amount):
            y += my
            x += mx
            cnt += 1
            if (x,y) not in obj:
                obj[(x,y)] = cnt
    return obj


line_1 = crossedWires(all_values1)
line_2 = crossedWires(all_values2)
intersections = list(set(line_1.keys()) & set(line_2.keys()))


def short():
    distances = []
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        distances.append(dist)
    return min(distances)


def few():
    combined_steps = [line_1[i] + line_2[i] for i in intersections]
    return min(combined_steps)


print("SOLUTION", short(), few())


# line_1 = crossedWires(moving_input_1)
# line_2 = crossedWires(moving_input_2)










# def crossedWires(move):
#         dircation = move[0:1]
#         dircation_amount = int(move[1:])
#         print(dircation)
#         print(dircation_amount)


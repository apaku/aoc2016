import sys

directionmap = {
                'U': (0, 1),
                'L': (-1, 0),
                'D': (0, -1),
                'R': (1, 0)
               }

def walk(directions, startpos, limits):
    newpos = startpos
    for direction in directions:
        oldpos = newpos
        newpos = (newpos[0] + directionmap[direction][0],
                  newpos[1] + directionmap[direction][1])
        if newpos not in limits:
            newpos = oldpos
    return newpos

def findbuttons(instructions, limits, keypad):
    oldbutton = (0,0)
    buttons = []
    for instruction in instructions:
        oldbutton = walk(instruction, oldbutton, limits)
        buttons.append(keypad[oldbutton])

    return buttons

if __name__ == "__main__":
    instructions = [line.strip() for line in sys.stdin.readlines()]
    part1limits = set([(-1,1), (0,1), (1,1), (-1,0), (0,0), (1,0), (-1,-1), (0,-1), (1,-1)])
    part1keypad = {(-1, 1): 1, (0, 1): 2, (1, 1): 3,
        (-1, 0): 4, (0, 0): 5, (1, 0): 6,
        (-1, -1): 7, (0, -1): 8, (1, -1): 9}
    print findbuttons(instructions, part1limits, part1keypad)
    part2limits = set([(0,0), (1,0), (2,0), (3,0), (4,0), (1,1), (2,1), (3,1), (1,-1),(2,-1),(3,-1),(2,2),(2,-2)])
    part2keypad = {(2, 2): 1, (1, 1): 2, (2, 1): 3,
        (3, 1): 4, (0, 0): 5, (1, 0): 6,
        (2, 0): 7, (3, 0): 8, (4, 0): 9,
        (1,-1): 'A', (2,-1): 'B', (3,-1): 'C',
        (2,-2): 'D'}
    print findbuttons(instructions, part2limits, part2keypad)


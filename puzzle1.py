import sys

def parse(lines):
    directionMapLeft = {
            (0,1): (-1,0),
            (-1,0): (0,-1),
            (0,-1): (1,0),
            (1,0): (0,1)
            }
    directionMapRight = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1)
            }
    for line in lines:
        yield (directionMapLeft if line[0] == 'L' else directionMapRight, int(line[1:]))

def part1(instructions):
    direction = (0,1)
    pos = (0,0)
    for instruction in instructions:
        direction = instruction[0][direction]
        pos = (pos[0] + direction[0] * instruction[1], pos[1] + direction[1] * instruction[1])
    return pos

def part2(instructions):
    direction = (0,1)
    pos = (0,0)
    seenpositions = set([pos])
    for instruction in instructions:
        direction = instruction[0][direction]
        for _ in range(instruction[1]):
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            if pos in seenpositions:
                return pos
            seenpositions.add(pos)
    return None

def distance(pos):
    return abs(pos[0]) + abs(pos[1])


if __name__ == "__main__":
    instructions = list(parse(sys.stdin.read().strip().split(', ')))
    print distance(part1(instructions))
    print distance(part2(instructions))


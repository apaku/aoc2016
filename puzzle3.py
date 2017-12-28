import sys

def part1(triangles):
    for triangle in triangles:
        (a,b,c) = tuple(map(int, filter(bool, triangle.split(' '))))
        if a+b > c and a+c > b and b+c > a:
            yield (a,b,c)

def part2(lines):
    intlines = [map(int, filter(bool, line.split(' '))) for line in lines]
    for i in range(0, len(intlines), 3):
        triangles = list(map(list, zip(*intlines[i:i+3])))
        for triangle in triangles:
            (a,b,c) = tuple(triangle)
            if a+b >c and a+c > b and b+c > a:
                yield (a,b,c)
if __name__ == "__main__":
    triangles = sys.stdin.readlines()
    print len(list(part1(triangles)))
    print len(list(part2(triangles)))

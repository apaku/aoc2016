import sys

def istriangle(listofthree):
    (a,b,c) = tuple(listofthree)
    return a+b > c and a+c > b and b+c > a

def part1(triangles):
    for triangle in triangles:
        yield istriangle(map(int, filter(bool, triangle.split(' '))))

def part2(lines):
    intlines = [map(int, filter(bool, line.split(' '))) for line in lines]
    for i in range(0, len(intlines), 3):
        triangles = list(map(list, zip(*intlines[i:i+3])))
        for triangle in triangles:
            yield istriangle(triangle)

if __name__ == "__main__":
    triangles = sys.stdin.readlines()
    print len(filter(bool, part1(triangles)))
    print len(filter(bool, part2(triangles)))

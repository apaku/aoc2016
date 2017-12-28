from operator import itemgetter
from collections import defaultdict, deque
import string
import sys

def countletters(text):
    counts = defaultdict(int)
    for x in text:
        counts[x] += 1
    return counts

def filterrealrooms(lines):
    for room in lines:
        info = room.strip().split('-')
        dashedname = '-'.join(info[:-1])
        name = ''.join(info[:-1])
        brackidx = info[-1].find('[')
        sectorid = int(info[-1][:brackidx])
        checksum = info[-1][brackidx+1:-1]
        lettercounts = countletters(name)
        orderedbyletter = sorted(lettercounts.items(), key=itemgetter(0))
        orderedbycount = sorted(orderedbyletter, key=itemgetter(1), reverse=True)
        calculatedchecksum = ''.join(map(itemgetter(0), orderedbycount))
        if calculatedchecksum[:len(checksum)] == checksum:
            yield (dashedname, sectorid)

def decipher(rooms):
    alphabet = list(string.ascii_lowercase)
    for room in rooms:
        name = room[0]
        sectorid = room[1]
        shifted = deque(alphabet)
        shifted.rotate(-sectorid)
        deciphered = ""
        for c in name:
            if c == '-':
                deciphered += ' '
            else:
                deciphered += shifted[alphabet.index(c)]
        yield deciphered, sectorid

if __name__ == "__main__":
    rooms = list(filterrealrooms(sys.stdin.readlines()))
    print sum(map(itemgetter(1), rooms))
    print filter(lambda room: 'northpole' in room[0], decipher(rooms))


FILEPATH = input()

with open(FILEPATH) as f:
    RAWCORDS = f.read()
CORDCOUNT = int()
for line in open(FILEPATH):
    print()
    CORDCOUNT += 1
splitCords = []
for i in range(CORDCOUNT):
    splitCords.append(RAWCORDS.split(' '))

print(splitCords)
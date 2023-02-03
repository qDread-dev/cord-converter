
FILEPATH = input()

with open(FILEPATH) as f:
    RAWCORDS = f.read()
CORDCOUNT = int()
for line in open(FILEPATH):
    print()
    CORDCOUNT += 1
print(RAWCORDS)
print(CORDCOUNT)
    
import time
import base64

ROUTENAME = 'tmp name'
STARTTIME = time.localtime()

FILEPATH = input()
#Gets cord length, splits into list, ect
with open(FILEPATH) as f:
    RAWCORDS = f.read().splitlines()

CORDCOUNT = int()
for line in open(FILEPATH):
    CORDCOUNT += 1
splitCords = []
for i in range(CORDCOUNT):
    splitCords.append(RAWCORDS[i].split(' '))


with open(f'cords.txt', 'w') as f:
    f.write("""{"categories":[{"name" : "tmp_name", "waypoints" : [""")
    for i in range(CORDCOUNT):
        if i != CORDCOUNT:
            f.write(f"""{{"name" : "{i},"x" : {splitCords[0]},"y" : {splitCords[1]},"z" : {splitCords[2]},"color" : 16711680,"addedAt" : 1672044394720}},""")
        else:
            f.write(f"""{{"name" : "{i},"x" : {splitCords[0]},"y" : {splitCords[1]},"z" : {splitCords[2]},"color" : 16711680,"addedAt" : 1672044394720}}""")
    f.write("""],"island" : "crystal_hollows"}]}""")
with open(f'cords.txt', 'r') as f:
    cordTmp = f.readlines()
print(cordTmp)

cordTmp = base64.b64encode(cordTmp)

with open('cords.txt') as f:
    f.write(cordTmp)
from datetime import datetime
import base64
import time

now = datetime.now()
ROUTENAME = 'tmp name'
OUTFILENAME = f'{now.strftime("%Y-%m-%d_%H-%M-%S")}_OUT.txt'
jsonCode = ""
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

# print(splitCords)

jsonCode += """{"categories":[{"name" : "tmp_name", "waypoints" : ["""
for i in range(CORDCOUNT):
    if i != CORDCOUNT:
        jsonCode += f"""{{"name" : "{i}","x" : {splitCords[i][0]},
        "y" : {splitCords[i][1]},"z" : {splitCords[i][2]},"color" : 16711680,"addedAt" : {str(round(datetime.timestamp(now), 0)).replace('.0', '')}}},"""
    else:
        jsonCode += f"""{{"name" : "{i}","x" : {splitCords[i][0]},"y" : {splitCords[i][1]},"z" : {splitCords[i][2]},"color" : 16711680,"addedAt" : {str(round(datetime.timestamp(now), 0)).replace('.0', '')}}}"""
jsonCode += """],"island" : "crystal_hollows"}]}"""

print(jsonCode)

cordTmp_bytes = str(jsonCode).encode('ascii')
base64_bytes = base64.b64encode(cordTmp_bytes)
base64_string = base64_bytes.decode('ascii')

with open(OUTFILENAME, 'w') as f:
    f.write(base64_string)

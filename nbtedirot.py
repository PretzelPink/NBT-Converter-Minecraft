
import nbtlib
from nbtlib.tag import *
import shutil as sh
import os
i = 0
l = []
conversionKey = ""

newr = {}
idList = open("minecrftBlockIds")
ref = list(idList)
sh.copyfile("provided.nbt", "copy.nbt")
nbt = "copy.nbt"

v=0
b=0
n=0
m=0
j=0
for x in ref:
    if(x.find('stair') != -1):
        v+=1
    elif (x.find('slab') != -1):
        b += 1
    elif (x.find('wall') != -1):
        n += 1
    elif (x.find('fence') != -1):
        m += 1
    else:
        j+=1

print("minecrat block list\n", str(v) + " stairs\n", b, "slab\n", n, "wall\n", m, "fence\n", j, "blocks")
def mapWall(keyBlock):
        for g in ref:
            if g.find('wall') != -1:
                newr[keyBlock] = g.strip('\n')
                while g in ref:
                    ref.remove(g)
                break
def mapFence(keyBlock):
        for g in ref:
            if g.find('fence') != -1:
                newr[keyBlock] = g.strip('\n')
                while g in ref:
                    ref.remove(g)
                break
def mapStair(keyBlock):
        for g in ref:
            newr[keyBlock] = g.strip('\n')
            while g in ref:
                ref.remove(g)
            break
def mapSlab(keyBlock):
        for g in ref:
            if g.find('slab') != -1:
                newr[keyBlock] = g.strip('\n')
                while g in ref:
                    ref.remove(g)
                break
def mapBlock(keyBlock):
        for g in ref:
            if g.find('fence') == -1 and g.find('stair') == -1 and g.find('slab') == -1 and g.find('wall') == -1:
                newr[keyBlock] = g.strip('\n')
                while g in ref:
                    ref.remove(g)
                break



with nbtlib.load(nbt) as ee:
    for x in ee.find('palette'):
        if(x['Name'][0:1] == 'f'):  # Checks for f as first character in the provided string I believe, if you are converting blocks from a mod, use the minecraft mod id (first letter)
            #print(x['Name'])
            l.append(x['Name'])
            #x['Name'] = nbtlib.String('minecraft:stone_stairs')
l= List(set(l))


while i < len(l):
    l[i] = str(l[i]).strip('\n')
    i += 1

f= 0
g= 0
h= 0
y= 0
u= 0
for x in l:
    if(x.find('stair') != -1):
        f+=1
    elif (x.find('slab') != -1):
        g += 1
    elif (x.find('wall') != -1):
        h += 1
    elif (x.find('fence') != -1):
        y += 1
    else:
        u+=1
print("new block list\n", str(f) + " stairs\n", g, "slab\n", h, "wall\n", y, "fence\n", u, "blocks")

for d in l:
    if(d.find('wall')) != -1:
        mapWall(d)
    elif(d.find('fence')) != -1:
        mapFence(d)
    elif (d.find('stair')) != -1:
        mapStair(d)
    elif (d.find('slab')) != -1:
        mapSlab(d)
    else:
        mapBlock(d)
i=0
st=0
for x in newr:
    #print(x + " : " + 'minecraft:' + newr[x + ""]) #prints key pair values
    conversionKey += (x + " : " + 'minecraft:' + newr[x + ""] + "\n")
    i += 1
print(i)
i=0
t = open('textTests.txt', 'w')
t.flush()
if(True):#input("Apply to " + nbt + "? y/n  ") == 'y'):
    with nbtlib.load(nbt) as ee:
        for x in ee.find('palette'):
            if (x['Name'][0:1] == 'f'):
                h = str(x['Name'])
                x['Name'] = nbtlib.String(('minecraft:' + str(newr[h])))
                #print(nbtlib.String('minecraft:' + str(newr[x['Name']])))
                #print(type(nbtlib.String('minecraft:' + str(newr[x['Name']]))))
                #print(('minecraft:'+str(newr[h]))) #prints all minecraft: blocks used
                i+=1
                #wrties to textTest to check if string has \n #t.write(nbtlib.String('minecraft:'+str(newr[h])))


fs = open("conversionPairKey.txt", 'w')
fs.write(conversionKey)
fs.close()

print("complete")
t.close()
#<class 'nbtlib.tag.String'>
#<class 'nbtlib.tag.String'>

#notes, fix to avoid panes or blocks that dont support carpet or signs
#       ensure blocks are being removed from the list correctly to avoid multiple blocks with same tag - Issue caused by older minecraft version (setting blocks that hadnt been added to minecraft yet)

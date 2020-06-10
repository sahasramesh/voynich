import re
import csv
import time
from itertools import permutations

#function to convert list to string
def convert(list):
    s = [str(i) for i in list]
    res = str(", ".join(s))
    return res

#decrypted letters: Thoyan9!m
userLet = input("Letters: ")

#define counter and empty lists
filterWords = []
comboPerms = []
allPerms = []
lookupList = ['word']
folioList = ['folio']
userList = ['lookup', userLet]

#removes duplicates from list
def noRepeats(x):
    return list(dict.fromkeys(x))

#function to remove 2 and 1 letter words
def removeShortPerms(wordss):
    return [i for i in wordss if len(i) >= 3]

#interpret user input
userLen = len(userLet)

#find all permutations of user input
perms = [''.join(p) for p in permutations(userLet)]
permsLen = len(perms)
print("\nLoading permutations...")
#print("All permutations: ", perms)

#filter out words longer than the user-submitted letters(or too short)
for z in range(0, len(perms)):
    if 3 <= len(perms[z]) <= userLen:
        filterWords.append(perms[z])
filterLen = len(filterWords)

#create smaller permutations
def shorterPerms(num):
    newPerms = []
    for y in range(0, permsLen):
        miniPerm = perms[y]
        miniPerm = miniPerm[num : : ]
        newPerms.append(miniPerm)
    return newPerms


#add all perm lists depending on number of letters
if 1 <= userLen <= 3:
    allPerms = perms

if 4 <= userLen <= 9:
    for i in range(1, userLen):
        comboPerms+= list(dict.fromkeys(shorterPerms(i)))
    allPerms = perms + comboPerms

allPerms = noRepeats(allPerms)

#get rid of all two letter and one letter permutations
allLen = len(allPerms)

#iterate through text file and look for matches
ind=0
while ind < allLen:
    myFile = open('datacaptions.rtf', 'r')
    enum = enumerate(myFile, 1)
    lookup = '.' + allPerms[ind] + '.'
    for num, line in enum:
        if lookup in line:
            folio = re.findall(r'<(.*?)>', line)
            lookin = re.sub('[.]', '', lookup)
            lookupList.append(lookin)
            folioList.append(folio)
    ind+=1
myFile.close()

#zip lists and write to csv
rows = zip(lookupList, folioList, userList)
f = open('testoutput.csv', 'w')
writer = csv.writer(f)
for row in rows:
    writer.writerow(row)

lookupList = lookupList[2:]
folioList = folioList[2:]
rows = zip(lookupList, folioList)
writer = csv.writer(f)
for row in rows:
    writer.writerow(row)

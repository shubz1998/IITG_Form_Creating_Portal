from collections import OrderedDict,Counter
import operator,os,errno
from glob import glob

# namelist is the list of different attacks
AttackList = ["Adduser_" , "Hydra_FTP_" , "Hydra_SSH_" , "Java_Meterpreter_" , "Meterpreter_" , "Web_Shell_"]

# for storing the features of the different n-grams
features_7 = {}
features_5 = {}
features_3 = {}


# an array of dictionaries for storing the grams of the corresponding attacks
grams_7 = [[Counter() for x in range(7)] for y in range(6)]
grams_5 = [[Counter() for x in range(7)] for y in range(6)]
grams_3 = [[Counter() for x in range(7)] for y in range(6)]

# processing each folder
for AttackIterator,Attack in enumerate(AttackList):
    for foldernum in range(0,7):
        path = 'ADFA-LD/ADFA-LD/Attack_Data_Master/' + Attack+ str(foldernum) +  '/*.txt'
        files = glob(path)
        for file in files:
            dict7 = {}
            dict5 = {}
            dict3 = {}

            attackdata = ""

            try:
                with open(file) as f:
                    attackdata = attackdata  + f.read()
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise

            attackdata = attackdata.split()

            # finding and storing the 7 grams in the corresponding dictionary
            grams7 = ()
            for it in range(0, len(attackdata) - 8):
                grams7 = tuple(attackdata[it: (it + 7)])
                if grams7 in dict7:
                    dict7[grams7]= dict7[grams7] + 1
                else:
                    dict7[grams7] = 1

            # according to the logic we need to calculate the last 5/3 grams separtely

            # calculating the last two 5 grams from the last 7 gram
            residual5a = grams7[2:7]
            residual5b = grams7[1:6]

            if residual5a in dict5:
                dict5[residual5a] = dict5[residual5a] + 1
            else:
                dict5[residual5a] = 1

            if residual5b in dict5:
                dict5[residual5b] = dict5[residual5b] + 1
            else:
                dict5[residual5b] = 1

            # now calculating the residual 3-grams from the last 5-grams
            residual3a = residual5b[2:7]
            residual3b = residual5b[1:6]

            if residual3a in dict3:
                dict3[residual3a] = dict3[residual3a] + 1
            else:
                dict3[residual3a] = 1

            if residual3b in dict3:
                dict3[residual3b] = dict3[residual3b] + 1
            else:
                dict3[residual3b] = 1

            # calcualting & storing the normal 5-grams from the 7-grams
            for key in dict7:
                grams5 = key[:5]
                if grams5 in dict5:
                    dict5[grams5]= dict5[grams5] + 1
                else:
                    dict5[grams5] = 1

            # calcualting & storing the normal 3-grams from the 5-grams
            for key in dict5:
                grams3 = key[:3]
                if grams3 in dict3:
                    dict3[grams3] = dict3[grams3] + 1
                else:
                    dict3[grams3] = 1

            grams_7[AttackIterator][foldernum] = grams_7[AttackIterator][foldernum] + Counter(dict7)
            grams_5[AttackIterator][foldernum] = grams_5[AttackIterator][foldernum] + Counter(dict5)
            grams_3[AttackIterator][foldernum] = grams_3[AttackIterator][foldernum] + Counter(dict3)

path = 'ADFA-LD/ADFA-LD/Training_Data_Master/*.txt'
files = glob(path)
length = 0.7*len(files)
normaldata = ""
for name in files[0:int(length)]:
    try:
        with open(name) as f:
            normaldata = normaldata + f.read()
        normaldata = normaldata + "@"
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise

normaldata= normaldata.split('@')

# finding and storing the 7 grams in the corresponding dictionary
dict7_normal = Counter()
dict5_normal = Counter()
dict3_normal = Counter()

for normalfile in normaldata:
    normalfile = normalfile.split()
    grams7 = ()
    for it in range(0, len(normalfile) - 8):
        grams7 = tuple(normalfile[it: (it + 7)])
        if grams7 in dict7_normal:
            dict7_normal[grams7]= dict7_normal[grams7] + 1
        else:
            dict7_normal[grams7] = 1

    # according to the logic we need to calculate the last 5/3 grams separtely

    # calculating the last two 5 grams from the last 7 gram
    residual5a = grams7[2:7]
    residual5b = grams7[1:6]

    if residual5a in dict5_normal:
        dict5_normal[residual5a] = dict5_normal[residual5a] + 1
    else:
        dict5_normal[residual5a] = 1

    if residual5b in dict5_normal:
        dict5_normal[residual5b] = dict5_normal[residual5b] + 1
    else:
        dict5_normal[residual5b] = 1

    # now calculating the residual 3-grams from the last 5-grams
    residual3a = residual5b[2:7]
    residual3b = residual5b[1:6]

    if residual3a in dict3_normal:
        dict3_normal[residual3a] = dict3_normal[residual3a] + 1
    else:
        dict3_normal[residual3a] = 1

    if residual3b in dict3_normal:
        dict3_normal[residual3b] = dict3_normal[residual3b] + 1
    else:
        dict3_normal[residual3b] = 1

    # calcualting & storing the normal 5-grams from the 7-grams
    for key in dict7_normal:
        grams5 = key[:5]
        if grams5 in dict5_normal:
            dict5_normal[grams5]= dict5_normal[grams5] + 1
        else:
            dict5_normal[grams5] = 1

    # calcualting & storing the normal 3-grams from the 5-grams
    for key in dict5_normal:
        grams3 = key[:3]
        if grams3 in dict3_normal:
            dict3_normal[grams3] = dict3_normal[grams3] + 1
        else:
            dict3_normal[grams3] = 1

Final7_normal = dict7_normal.most_common(int(0.3*len(dict7_normal)))
Final5_normal = dict5_normal.most_common(int(0.3*len(dict5_normal)))
Final3_normal = dict3_normal.most_common(int(0.3*len(dict3_normal)))

Final7 = [Counter() for x in range(0,7)]
Final5 = [Counter() for x in range(0,7)]
Final3 = [Counter() for x in range(0,7)]

for i in range(0,6):            # 6 attack
    for j in range(0,7):            # 7 folders of each attack
        Final7[i] = Final7[i] + grams_7[i][j]
        Final5[i] = Final5[i] + grams_5[i][j]
        Final3[i] = Final3[i] + grams_3[i][j]

    #picking top 30%
    Final7[i] = Final7[i].most_common(int(0.3*len(Final7[i])))
    Final5[i] = Final5[i].most_common(int(0.3*len(Final5[i])))
    Final3[i] = Final3[i].most_common(int(0.3*len(Final3[i])))

    # print(len(Final7[i]))


    path7 = 'ADFA-LD/ADFA-LD/Attack_Data_Master/Attack' + str(i) + '1-7top30%7tupple.txt'
    path5 = 'ADFA-LD/ADFA-LD/Attack_Data_Master/Attack' + str(i) + '1-7top30%5tupple.txt'
    path3 = 'ADFA-LD/ADFA-LD/Attack_Data_Master/Attack' + str(i) + '1-7top30%3tupple.txt'

    if os.path.isfile(path7):
        os.remove(path7)
    if os.path.isfile(path3):
        os.remove(path3)
    if os.path.isfile(path5):
        os.remove(path5)

    filewrite=open(path7,'a')
    q = Final7[i]
    for tmp in q:
        filewrite.write(str(tmp)+"\n")
    filewrite.close()

    filewrite=open(path5,'a')
    q = Final5[i]
    for tmp in q:
        filewrite.write(str(tmp)+"\n")
    filewrite.close()

    filewrite=open(path3,'a')
    q = Final3[i]
    for tmp in q:
        filewrite.write(str(tmp)+"\n")
    filewrite.close()

path7 = 'ADFA-LD/ADFA-LD/Attack_Data_Master/normal_top30%7tupple.txt'
path5 = 'ADFA-LD/ADFA-LD/Attack_Data_Master/normal_top30%5tupple.txt'
path3 = 'ADFA-LD/ADFA-LD/Attack_Data_Master/normal_top30%3tupple.txt'

if os.path.isfile(path7):
    os.remove(path7)
if os.path.isfile(path3):
    os.remove(path3)
if os.path.isfile(path5):
    os.remove(path5)

filewrite = open(path7, 'a')
q = Final7_normal
for tmp in q:
    filewrite.write(str(tmp) + "\n")
filewrite.close()

filewrite = open(path5, 'a')
q = Final5_normal
for tmp in q:
    filewrite.write(str(tmp) + "\n")
filewrite.close()

filewrite = open(path3, 'a')
q = Final3_normal
for tmp in q:
    filewrite.write(str(tmp) + "\n")
filewrite.close()


'''

path = 'ADFA-LD/ADFA-LD/features_7gram.txt'
f = open(path, 'w')
for i in features_7.keys():
    temp = str(i)
    f.write(temp + "\n")

path = 'ADFA-LD/ADFA-LD/features_5gram.txt'
f = open(path, 'w')
for i in features_5.keys():
    temp = str(i)
    f.write(temp + "\n")

path = 'ADFA-LD/ADFA-LD/features_3gram.txt'
f = open(path, 'w')
for i in features_3.keys():
    temp = str(i)
    f.write(temp + "\n")
'''
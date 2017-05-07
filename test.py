import pickle
import IAhash
import numpy as np
import random
import CChash

def media(l):
    count = 0.
    for i in range(len(l)):
        count += l[i]
    return count / len(l)


def test():
    val = pickle.load(open("percents.p", "rb"))

    chainedr = Chained(val)
    iaopenr = Iaperto(val)

    pickle.dump(chainedr,open("chained.p", "wb"))
    pickle.dump(iaopenr, open("iaopen.p", "wb"))


def Chained(val):
    collist = []
    totcoll = []
    rd = []
    perc = []
    for i in range(len(val[1])):
        perc.append((val[0] * val[1][i]) / 100)
    for i in range(len(perc)):
        for j in range(20):
            cc = CChash.HashC(val[0])
            rd.append(random.randint(0, 100 * val[0]))
            for k in rd:
                cc.Cinsert(k)
            collist.append(cc.numColl())
        totcoll.append(max(collist))
        totcoll.append(min(collist))
        totcoll.append(media(collist))
        collist = []
    print "Valore di m preso:", cc.getM()
   # print cc.tostring()
    return totcoll


def Iaperto(val):
    collist = []
    totcoll = []
    isplength = []
    isp = []
    totisp = []
    rd = []
    perc = []
    for i in range(len(val[1])):
        perc.append((val[0] * val[1][i]) / 100)
    for i in range(len(perc)):
        for i in range(20):
            ia = IAhash.Hash(val[0])
            rd.append(random.randint(0, 100 * val[0]))
            for k in rd:
                ia.indAinsert(k)
            collist.append(ia.getC())
            isplength = ia.getisp()
            if isplength != []:
                isp.append(max(isplength))
                isp.append(min(isplength))
                isp.append(media(isplength))
        totisp.append(max(isp))
        totisp.append(min(isp))
        totisp.append(media(isp))

        totcoll.append(max(collist))
        totcoll.append(min(collist))
        totcoll.append(media(collist))

        isplength = []
        collist = []
    print "Valore di m preso: ", ia.getM()
    #print ia.tostring()
    return totcoll, totisp


# val = pickle.load(open("percents.p", "rb"))
# Iaperto(val)
# Chained(val)

'''
a = np.empty([2, ], dtype=list)
a[0] = 10
a[1] = [10, 50, 90]

ia = IAhash.Hash(a[0])
b = []
for i in range(3):
    b.append((a[0] * a[1][i]) / 100)
    ia = IAhash.Hash(a[0])
    for j in range(b[i]):
        ia.indAinsert(random.randint(0, 100 * a[0]))
    ia.tostring()
    print "collisioni:", ia.getC()
    print ia.getisp()
    ip = ia.getisp()
    if ip != []:
        print "max:", max(ip), "min:", min(ip), "avg:", media(ip), "\n"

print " "
cc = CChash.HashC(a[0])
c = []
for i in range(3):
    c.append((a[0] * a[1][i]) / 100)
    cc = CChash.HashC(a[0])
    for j in range(c[i]):
        cc.Cinsert(random.randint(0, 100 * a[0]))
    cc.tostring()
    print "collisioni:", cc.numColl(), "\n"
'''

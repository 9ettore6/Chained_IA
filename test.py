import pickle
import numpy as np
import random
import IAhash as ho
import CChash as hc


def test():
    val = pickle.load(open("percents.p", "rb"))
    chainedr = Chained(val)
    iaopenr = Iaperto(val)

    pickle.dump(chainedr, open("chained.p", "wb"))
    pickle.dump(iaopenr, open("iaopen.p", "wb"))


def Chained(val):
    percentage = val[1]
    collist = []
    totcoll = []

    for i in percentage:
        for j in range(0, 20):
            rd = random.sample(range(100 * val[0]), val[0] * i / 100)
            cc = hc.HashC(val[0])
            for value in rd:
                cc.Cinsert(value)

            totcoll.append(cc.numColl())

        maxCollisionsValue = max(totcoll)
        minCollisionsValue = min(totcoll)
        avgCollisionsValue = sum(totcoll) / len(totcoll)
        cList = [maxCollisionsValue, minCollisionsValue, avgCollisionsValue]

        collist.append(cList)
        totcoll = []

    return collist


def Iaperto(val):
    m = val[0]
    percentage = val[1]
    totcoll = []
    totisp = []
    collist = []
    isp = []
    for j in percentage:
        for i in range(0, 20):
            ia = ho.Hash(m)
            rd = random.sample(range(100 * m), m * j // 100)

            for value in rd:
                ia.indAinsert(value)

            collist.append(ia.getC())
            isp.append(ia.getisp())

        maxC = max(collist)
        minC = min(collist)
        avgC = sum(collist) / len(collist)
        cList = [maxC, minC, avgC]

        maxI = max(max(v) for v in isp)
        minI = min(min(v) for v in isp)
        avgI = sum(sum(v) / len(v) for v in isp) / len(isp)
        iList = [maxI, minI, avgI]

        totcoll.append(cList)
        totisp.append(iList)

        collist = []
        isp = []

    return totcoll, totisp

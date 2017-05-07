import pickle
import matplotlib.pyplot as plt
import test

'''
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
'''
perc = (10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 90, 91, 92, 93, 94, 95, 96, 97, 98, 100)
m = 1000
val = [m, perc]
pickle.dump(val, open("percents.p", "wb"))

test.test()
chainedcol = pickle.load(open("chained.p", "rb"))
iaresult = pickle.load(open("iaopen.p", "rb"))
x = perc
yMax = []
for i in range(0, len(chainedcol), 3):
    yMax.append(chainedcol[i])
yMin = []
for i in range(1, len(chainedcol), 3):
    yMin.append(chainedcol[i])
yAvg = []
for i in range(2, len(chainedcol), 3):
    yAvg.append(chainedcol[i])

plt.plot(x, yMax)
plt.plot(x, yMin)
plt.plot(x, yAvg)
plt.title("Chained")
plt.xlabel("Percents")
plt.ylabel("Collisions")
plt.legend(["Max","Min","Avg"],loc = 2)
plt.show()

iacoll = iaresult[0]
iaisp = iaresult[1]
x = perc
yMax = []
for i in range(0,len(iacoll),3):
    yMax.append(iacoll[i])
yMin = []
for i in range(1,len(iacoll),3):
    yMin.append(iacoll[i])
yAvg = []
for i in range(2,len(iacoll),3):
    yAvg.append(iacoll[i])

plt.plot(x,yMax)
plt.plot(x,yMin)
plt.plot(x,yAvg)
plt.xlabel("Percents")
plt.ylabel("Collisions")
plt.title("Indirizzamento Aperto(collisioni)")
plt.legend(["Max","Min","Avg"],loc = 2)
plt.show()

yMax = []
for i in range(0,len(iaisp),3):
    yMax.append(iaisp[i])
yMin = []
for i in range(1,len(iaisp),3):
    yMin.append(iaisp[i])
yAvg = []
for i in range(2,len(iaisp),3):
    yAvg.append(iaisp[i])
plt.plot(x,yMax)
plt.plot(x,yMin)
plt.plot(x,yAvg)
plt.xlabel("Percents")
plt.ylabel("Ispections")
plt.title("Indirizzamneto Aperto(ispezione)")
plt.legend(["Max","Min","Avg"],loc = 2)
plt.show()
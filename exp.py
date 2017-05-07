import pickle
import Test
import matplotlib.pyplot as plt

m = 1000
perc = (10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)
val = (m, perc)

pickle.dump(val, open("percents.p", "wb"))

Test.test()

chainedcol = pickle.load(open("chained.p", "rb"))
iaresult = pickle.load(open("iaopen.p", "rb"))
iacol = iaresult[0]
iaisp = iaresult[1]

# Plot collisions for chained hash
xAxis = perc
yMax = [i[0] for i in chainedcol]
yMin = [i[1] for i in chainedcol]
yAvg = [i[2] for i in chainedcol]

plt.plot(xAxis, yMax)
plt.plot(xAxis, yMin)
plt.plot(xAxis, yAvg)

plt.xlabel('Percents')
plt.ylabel('Collisions')
plt.legend(['Max', 'Min', 'Avg'], loc=2)
plt.title("Chained")
plt.show()

# Plot collisions for open hash
yMax = [i[0] for i in iacol]
yMin = [i[1] for i in iacol]
yAvg = [i[2] for i in iacol]

plt.plot(xAxis, yMax)
plt.plot(xAxis, yMin)
plt.plot(xAxis, yAvg)

plt.xlabel('Percents')
plt.ylabel('Collisions')
plt.legend(['Max', 'Min', 'Avg'], loc=2)
plt.title("Indirizzamento aperto(collisioni)")
plt.show()

# Plot inspections for open hash
yMax = [i[0] for i in iaisp]
yMin = [i[1] for i in iaisp]
yAvg = [i[2] for i in iaisp]

plt.plot(xAxis, yMax)
plt.plot(xAxis, yMin)
plt.plot(xAxis, yAvg)

plt.xlabel('Percents')
plt.ylabel('Insepctions')
plt.legend(['Max', 'Min', 'Avg'], loc=2)
plt.title("Indirizzamento aperto(ispezioni)")
plt.show()

import numpy as np
import math


class Hash:
    m = 0

    def __init__(self, m):
        self.m = m
        self.col = 0
        self.arrisp = []
        while not self.ifprime(self.m):
            self.m += 1
        self.a = np.array([None for _ in range(self.m)])
        for i in range(0, self.m):
            self.a[i] = None

    def getM(self):
        return self.m

    def ifprime(self, m):
        if m == 2:
            return True
        if m % 2 == 0 or m <= 1:
            return False
        sqr = int(math.sqrt(m)) + 1
        for i in range(3, sqr, 2):
            if m % i == 0:
                return False
        return True

    def indAhash(self, i, k):
        h = ((k % self.m) + i) % self.m
        # print h
        return h

    def indAinsert(self, k):
        i = 0
        while i != self.m:
            j = self.indAhash(i, k)
            if self.a[j] == None or self.a[j] == "Del":
                self.a[j] = k
                self.arrisp.append(i)
                return j
            else:
                i += 1
                self.col += 1
        print "Error: Hash table overflow!"

    def getisp(self):
        return self.arrisp

    def tostring(self):
        print self.a

    def indAsearch(self, k):
        i = 0
        while i != self.m or i != None:
            j = self.indAhash(i, k)
            if self.a[j] == k:
                print "Posizione: ", j
                return j
            elif self.a[j] == None:
                print "Non presente!"
                break
            else:
                i += 1

    def indAdelete(self, k):
        b = self.indAsearch(k)
        if b != None:
            self.a[b] = "Del"
        else:
            print "Elemento non presente!"

    def getC(self):
        return self.col


'''
b = Hash(13)
b.indAinsert(5)
b.tostring()
b.indAinsert(8)
print ""
b.indAsearch(5)
print ""

b.indAdelete(5)
b.tostring()
b.indAsearch(8)
b.indAinsert(5)
b.tostring()
'''

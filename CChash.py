from Lista import LinkedList
import numpy as np
import math


class HashC:
    def __init__(self, m):
        self.m = m
        while not self.ifprime(self.m):
            self.m -= 1
        self.a = np.empty([m, ], dtype=list)
        for i in range(0, self.a.size):
            self.a[i] = LinkedList()

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

    def hashf(self, k):
        return k % self.m

    def Cinsert(self, k):
        self.a[self.hashf(k)].add(k)

    def Cdelete(self, k):
        self.a[self.hashf(k)].remove(k)

    def Csearch(self, k):
        for i in range(0, self.m):
            b = self.a[self.hashf(k)].search(k)
        if b:
            print b, k, "indice dell'array:", self.hashf(k)
        else:
            print b, k, "Elemento non presente!"

    def tostring(self):
        for i in range(0, self.m):
            print i, "[]", self.a[i].PrintL()

    def numColl(self):
        coll = 0
        for i in range(0, self.m):
            if self.a[i].size() != 0:
                coll += self.a[i].size() - 1
        return coll


'''
b = HashC(10)
b.Cinsert(1)
b.Cinsert(4)
b.Cinsert(8)
b.Cinsert(45)
b.Cinsert(16)
b.tostring()
'''

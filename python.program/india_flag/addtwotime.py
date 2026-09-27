"""class Time:
    def __init__(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def sum(self, t2):
        t = Time(0, 0, 0)

        t.__s = self.__s + t2.__s
        t.__m = self.__m + t2.__m
        t.__h = self.__h + t2.__h

        if t.__s >= 60:
            t.__s = t.__s - 60
            t.__m = t.__m + 1

        if t.__m >= 60:
            t.__m = t.__m - 60
            t.__h = t.__h + 1

        return t

    def display(self):
        print("Time:", self.__h, ":", self.__m, ":", self.__s)


t1 = Time(2, 45, 50)
t2 = Time(3, 30, 25)

t3 = t1.sum(t2)

t3.display()"""


"""class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def sum(self, t2):
        t = Time(0, 0, 0)

        t.s = self.s + t2.s
        t.m = self.m + t2.m
        t.h = self.h + t2.h

        if t.s >= 60:
            t.s = t.s - 60
            t.m = t.m + 1

        if t.m >= 60:
            t.m = t.m - 60
            t.h = t.h + 1

        return t

    def display(self):
        print("Time:", self.h, ":", self.m, ":", self.s)


t1 = Time(2, 45, 50)
t2 = Time(3, 30, 25)

t3 = t1.sum(t2)

t3.display()"""
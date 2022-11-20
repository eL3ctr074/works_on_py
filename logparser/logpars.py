class Pars:

    def __init__(self):
        self.sourcearr = []
        self.iparr = []
        self.timearr = []
        self.statusarr = []
        self.urlarr = []

    def initfile(self, filename):
        self.sourcearr = list(open(filename))
        length = len(self.sourcearr)

        for index in range(length):
            temparr = self.sourcearr[index].split(' ')
            self.iparr.append(temparr[0])
            for indexY in range(len(temparr)):
                if indexY == 4:
                    temper = temparr[indexY]
                    temper = ''.join(temper)
                    self.timearr.append(temper[:5])
            self.urlarr.append(temparr[6])
            self.statusarr.append(temparr[8])
        self.iparr = list(set(self.iparr))

    def timefinder(self, time):
        countT = 0
        for z in range(len(self.timearr)):
            if self.timearr[z] == time:
                countT += 1
        return countT

    def timebytime(self):
        arr = []
        temp = set(self.timearr)
        temp = sorted(temp)
        for elem in temp:
            count = self.timefinder(elem)
            arr.append(elem)
            arr.append(count)
        return arr

    def urlfind(self, errcode):
        temp = []
        for index in range(len(self.statusarr)):
            if self.statusarr[index] == errcode:
                temp.append(self.urlarr[index])
        return temp

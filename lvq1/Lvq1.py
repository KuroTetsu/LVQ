from LVQ import ReadFile
from random import randint

class LVQ:
    __data = []
    __uniqeClass = []
    __weight = []

    __epoch = 0
    __alpha = 0
    __alpha_gain = 0
    __tolerant = 0
    __accu = 0

    #Get data from excel to array @data
    def FileData(self, link):
        global data
        data = ReadFile.OpenFile().GetFile(link)

        
    def Parameter(self,*args):
        global epoch 
        global alpha
        global alpha_gain
        global tolerant

        if len(args) == 3:
            epoch = args[0]
            alpha = args[1]
            alpha_gain = args[2]
            tolerant = 0.000001
        elif len(args) == 4:
            epoch = args[0]
            alpha = args[1]
            alpha_gain = args[2]
            tolerant = args[3]
        
        self.classType()
        self.fweight()

    
    def classType(self):
        global UniqeClass 
        UniqeClass = []
        for x in data:
            if x[-1:] not in UniqeClass:
                UniqeClass.append(x[-1:])

    def fweight(self):
        global weight
        weight = []
        rand = []
        for x in UniqeClass:
            rand = []
            for y in data:
                if y[-1:] == x:
                    rand.append(y[:])
            weight.append(rand[randint(0,len(rand))])
        return weight
        

    def ecludean(self,arr,wei):
        self.sort = []
        self.ar = []
        self.temp = 0

        for x in wei:
            temp = 0
            for y,z in zip(x[:-1],arr):
                temp += (y-z)**2
            self.ar.append(temp)
        
        temp = min(self.ar)
        return self.ar.index(temp)

    def Train(self):
        global weight, alpha
        
        self.id = 0
        coun = 0
        
        for self.a in range(epoch):
            for self.b in range(len(data)):
                self.id = self.ecludean(data[self.b][:-1],weight)
                if weight[self.id][-1:] == data[self.b][-1:]:
                    up = 0
                    for x,y in zip(weight[self.id][:-1],data[self.b][:-1]):
                        weight[self.id][up] = x + alpha*(y-x)
                        up+=1
                else:
                    up = 0
                    for x,y in zip(weight[self.id][:-1],data[self.b][:-1]):
                        weight[self.id][up] = x - alpha*(y-x)
                        up+=1

            if alpha < tolerant:
                break
            else:
                alpha *= alpha_gain
            coun+=1
        
    def Testing(self):
        global accu

        self.count = 0
        for x in range(len(data)):
           self.id = self.ecludean(data[x][:-1],weight)
           if data[x][-1:] == weight[self.id][-1:]:
               self.count+=1
        accu = self.count * 100 / len(data)

    def getWeight(self):
        return weight
    
    def getAccurate(self):
        return accu
        
    def getClass(self):
        print tolerant
        return UniqeClass


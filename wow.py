class area:
    hori = []
    verti = []

    def __init__(self):
        self.hori
        self.verti

    def setArea(self,list):
        hStart = list[0]
        hEnd = list[2]
        vStart = list[1]
        vEnd = list[3]

        for i in range(hStart,hEnd):
            if(i not in self.hori):
                self.hori.append(i)

        for j in range(vStart,vEnd):
            if(j not in self.verti):#오 이런거 중요
                self.verti.append(j)

    def getH(self):
        return self.hori

    def getV(self):
        return self.verti


def Compar(a1, a2):
    rlisth = a1.getH()
    rlistv = a1.getV()
    blisth = a2.getH()
    blistv = a2.getV()
    hlen = []
    vlen = []

    for i in rlisth:
        if i in blisth:
            hlen.append(i)

    for j in rlistv:
        if j in blistv:
            vlen.append(j)

    return len(hlen) * len(vlen)

red = area()
blue = area()

aws  = []

testcase = int(input())
for i in range(1,testcase+1):
    areanum = int(input())
    for j in range(1,areanum+1):
        list1 = list((map(int,input().split())))

        if list1[len(list1)-1] == 1:
            red.setArea(list1)
        else:
            blue.setArea(list1)

    awsval = Compar(red,blue)
    aws.append(awsval)

for anwser in aws:
    print("# "+ str(anwser))


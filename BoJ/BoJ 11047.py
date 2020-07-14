

'''a,b = int(input())'''

b1=4790
b2=4200

'''for i in range(a):
    dic[i] = 0'''
list1 = [1,5,10,50,100,500,1000,5000,10000,50000]


def judge(list1,b):
    sums = 0
    dic = {}
    reList = sorted(list1,reverse=True)
    for i in reList:
        dic[i] = 0
    check = b
    newlist = dic.keys()
    for coin in newlist:
        if b//coin > 0:
            dic[coin] += b//coin
            b = b - (b//coin)*coin

    for nums in dic.values():
        sums += nums
    return sums

a1 = judge(list1,b1)
a2 = judge(list1,b2)

print(a1)
print(a2)




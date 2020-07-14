
'''check = False
while(check == False):
    n = int(input())
    if n % 2 is 1:
        check = True
#  홀수의 마방진 얻는 알고리즘'''
from typing import List


def mabangjin(arr: List) -> None:
    row = len(arr) - 1  # 4
    col = len(arr) // 2  #  몫
    value = 1

    arr[row][col] = value
    value += 1

    while value <= len(arr) ** 2:
        if arr[(row + 1) % len(arr)][(col + 1) % len(arr)] == 0:
            row += 1
            col += 1
            arr[row % len(arr)][col % len(arr)] = value
            value += 1
        else:
            row -= 1
            arr[row % len(arr)][col % len(arr)] = value
            value += 1


map = []
for i in range(5):
    map.append(list())
    for k in range(5):
        map[i].append(0)
        print(f"{map[i][k]:2d} ", end='')
    print()

mabangjin(map)
print()
for i in range(5):
    for k in range(5):
        print(f"{map[i][k]:2d} ", end='')
print()








'''def mabangjin(map,n):
    answer_list = [i for i in range(1,(n*n)+1)]
    allnum = n*n
    path=[]
    index=0
    k=3  #  중복을 허용하지 않는 조합
    statick = k
    backtracking(map,answer_list,allnum,k,index,path,statick)


def judgerow(n):
    if n == 0:
        return 0
    elif n > 0:
        return n + judgerow(n-1)


def backtracking(map,answer_list,allnum,k,index,path,statick):
    if k == 0:
        if sum(path) == judgerow(allnum)/statick:
            map.append(path)
            for i in path:
                answer_list.remove(i)
            return
    for j in range(index,allnum):
        backtracking(map,answer_list,allnum,k-1,j,path+[answer_list[j]],statick)


map = []
mabangjin(map,3)'''






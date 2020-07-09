def my_algorithm(list): #입력 받은 값의 큰 값과 작은 값의 차를 구합니다.
    front = list[0]
    back = list[len(list)-1]
    return back - front

T = int(input())



for test_case in range(1, T + 1):
    a=map(int,input())
    input_list = list(map(int,input().split()))
    input_list.sort() #원래는 sort를 직접 구현해야 좋지만 파이썬의 정렬이 병합 정렬과 퀵정렬을 활용한 sort 알고리즘을 사용하기에 제일 빠를 것이라 판단하여 사용
    answer = my_algorithm(input_list)
    print("#%d %d"%(test_case,answer))

def check_count(list1):
    anw = [0 for i in range(10)] #0~9의 숫자가 몇번 나왔는지 카운트 합니다.
    for i in list1:
        anw[i] += 1
    return anw


T = int(input())

for test_case in range(1, T + 1):
    a = int(input())
    list1 = list(int(x) for x in input()) #입력값이 78974이기에 string으로 입력 받아서 int로 변환합니다.
    answer = check_count(list1)
    max_val = max(answer)

    for i in range(-9, 0):
        chi = abs(i) #리스트를 뒤로부터 읽습니다.
        if answer[chi] == max_val: #가장 많이 나온 최대값을 바로 뽑습니다.
            print("#{0} {1} {2}".format(test_case, chi, max_val))
            break
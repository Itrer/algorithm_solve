def reverse(sen):
    reverse_sen = ""
    for char in sen:
        reverse_sen = char +reverse_sen
    return reverse_sen

def compresio(sen1 ,sen2):
    for i in range(0 ,len(sen1 ) -1):
        if sen1[i] != sen2[i]:
            return 0
    return 1

T = int(input())

for test_case in range(1, T + 1):
    input_data = input()
    rever = reverse(input_data)
    anw = compresio(input_data ,rever)
    print("#{0} {1}".format(test_case ,anw))
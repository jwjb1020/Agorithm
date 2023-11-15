#문제 n개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 구하시오.
#입력 첫째 줄에 정수의 개수가 주어진다. 둘째 줄에는 n개의 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1000000보다 크거나 같고, 1000000보다 작거나 같은 정수이다.
n =  int(input())
array_list = list(map(int, input().split()))

max_num = array_list[0]
min_num = array_list[0]

for num in array_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)
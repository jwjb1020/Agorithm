# n개의 수가 주어 졌을 때, 이를 오름차순으로 정렬하는 프로그램
#입력
#첫째 줄에 수의 개수 n이 주어짐, 둘째줄 n개의 줄에는 수가 주어짐
#출력 오름차순으로 정렬한 결과 하나씩 출력
import sys
input = sys.stdin.readline
# 입력 받는 코드
n = int(input())

# 배열 초기화(최대로 입력가능한 수 + 1)
arr = [0] *10001
# 배열에 값넣기
# 값을 넣을때 인덱스에 1을 추가하기
for _ in range(n):
    num = int(input())
    arr[num] = arr[num] +1

#출력
#전체 배열을 돌면서 인덱스 값이 0이 아닌걸 
for i in range(len(arr)):
    # 인덱스 값이 0이 아닌걸 
    if arr[i] != 0:
        # 순서대로 출력(0이아닌 인덱스)
        for _ in range(arr[i]):
            print(i)



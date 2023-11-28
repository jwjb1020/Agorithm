# 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램 만들기
# 1. 배열에 자연수 X를 넣는다.
# 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

#입력
# 첫째 줄에 연산의 개수 n이 주어짐
# 다음 n개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어짐
# 만약 x가 자연수라면 배열에 x라는 값을 넣는 연산
# x가 0이라면 배열에서 가장 큰 값을 출력하고, 배열에서 제거
# 입력되는 자연수는  2 ^31 보다 작음 

#빨리 입력받기 위해 sys import
import sys
# 큐를 사용하기 위해 heapq 임포트
import heapq

input = sys.stdin.readline
# n입력 받기
n = int(input())
# 힙큐 초기화(파이썬에서는 min heap이 default)
heap = []
# 연산에 대한 정보
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,(-1)*x)            

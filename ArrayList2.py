cook = [list(map(int, input().split())) for _ in range(5)]
cookScore = [0]*5
score = 0
for i in range(5):
    sum = 0
    for j in range(4):
        sum += cook[i][j]
    cookScore[i] = sum
    score = max(score,sum)

for i in range(5):
    if cookScore[i] == score:
        print(i+1,score)
        break



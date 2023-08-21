# 입력 받기
burger = []
N = int(input())
*burger, = map(int, input().split(" "))

# 맛의 정도가 가장 높은 값의 인덱스 구하기 (top)
top = burger.index(max(burger))

# 맛이 완벽할 경우의 값
result = sum(burger)

# 순회하면서 top을 기준으로 오름차순-top-내림차순인지 체크
for i in range(0, top):
    if burger[i+1] - burger[i] < 0:
        result = 0
        break
    else:
        continue

for i in range(top, N-1):
    if burger[i] - burger[i+1] < 0:
        result = 0
        break
    else:
        continue

# 결과 출력
print(result)

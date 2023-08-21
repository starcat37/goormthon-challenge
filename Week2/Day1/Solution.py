from itertools import combinations

# 입력 받기
N = int(input())
S = input()

# 조합으로 모든 부분문자열 구하기
cnt = [i for i in range(N)]
cnt_comb = list(combinations(cnt, 3))
str_comb = []
for i in cnt_comb:
  comb = [S[i[0]:i[1]], S[i[1]:i[2]], S[i[2]:]]
  if "".join(comb) == S:
    str_comb.append(comb)

# 모든 부분문자열 기반으로 P 구하기
P = sorted(set(sum(str_comb, []))) # 이중 리스트을 flatten하는 방법 중 하나: sum

# 점수 계산하기
score = []
for i in str_comb:
  score.append(P.index(i[0]) + P.index(i[1]) + P.index(i[2]) + 3) # X번째 보정을 위해 3 더해줌

# 결과 출력
print(max(score))

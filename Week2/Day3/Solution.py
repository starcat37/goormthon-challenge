N = int(input())
cnt = 0

while N >= 14:
    cnt += (N // 14)
    N %= 14

while N >= 7:
    cnt += (N // 7)
    N %= 7

while N >= 1:
    cnt += (N // 1)
    N %= 1

print(cnt)

N = int(input())
T, M = map(int, input().split(" "))
work_time = []
for _ in range(N):
    work_time.append(int(input()))
total = sum(work_time)
if M + total < 60:
    print(T % 24, M + total)
else:
    print((T + (M + total) // 60) % 24, (M + total) % 60)

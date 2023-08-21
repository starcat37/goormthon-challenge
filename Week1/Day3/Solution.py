sum = 0
T = int(input())
for _ in range(T):
    evaluation = input()
    sum += int(eval(evaluation))

print(sum)

# 입력 받기
N, K = map(int, input().split(" "))
*nums, = map(int, input().split(" "))

# 이진수 정렬 처리
bin_nums = [str(bin(i)) for i in nums]
bin_nums.sort(reverse=True, key=lambda x: (x.count("1"), int(x[2:])))

# 출력
print(int(bin_nums[K-1], 2))

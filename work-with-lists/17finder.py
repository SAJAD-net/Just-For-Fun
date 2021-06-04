
def finder(nums):
    for n in nums:
        if n == 17:
            return n, nums.index(n)

def run():
    nums=[]
    for i in range(10):
        num=int(input(f"[{i}]-enter a number -> "))
        nums.append(num)
    print(finder(nums))

run()

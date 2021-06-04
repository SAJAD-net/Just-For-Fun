number = int(input("Enter number : "))


def returns(num):
    new=0
    for i in range(1, num+1):
            new+=i
    print(new)
returns(number)

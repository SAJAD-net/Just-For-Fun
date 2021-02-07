num=int(input("Enter range number :"))

print("Number\tSquare\tCube")
for i in range(num+1):
    square=i*i
    cube=i*square
    print(f"{i}\t{square}\t{cube}")

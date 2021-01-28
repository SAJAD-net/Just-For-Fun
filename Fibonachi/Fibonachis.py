numf=int(input("Enter [From] number ~$ "))
numt=int(input("Enter [To] number ~$ "))
first=numf
second = numf+1
for i in range(numf,numt):
    print('\nThis is The First Numbers:',first)
    print('This is The Second Numebrs:',second)
    new = first+second
    first =second
    second = new
    print(' This is The Fibonachi Numbers:',new)

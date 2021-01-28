import random as r
def math(f,s,t,nm):
    nnm=f * s * t
    if nnm == nm-1:
        nfirst,nsecond,ntherid = f,s,t
        print("this number %i = %i x %i x %i"%(nm-1,nfirst,nsecond,ntherid))
def create(nm):
    # while True:
    for i in range(nm):
        for i in range(1,nm):
            first=i
            # print("this is the first number ",first)
            i = r.randrange(0,nm)
            second=i
            # print("this is the second number ",second)
            i = r.randrange(0,nm)
            therid=i
            # print("this is the therid number ",therid)
            if math(first,second,therid,nm):
                break

def main():
    number=int(input("enter the number : "))
    create(number+1)
main()

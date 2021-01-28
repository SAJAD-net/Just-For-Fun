import time,os
def positived(i,count):
    for o in range(1,20):
        # print("this is the number 1 to 20",o)
        if i % o == 0:
            count+=1
            # print(i,count)
        if count >= 19:
            print(count)
            print("--> this number is divisable by all of the numbers from 1 to 20 ===>",i)
            input("press Enter to exit SCH :~$ ")
            exit()

def main():
    os.system("clear")
    print("Please wait ...")
    start=time.time()
    for i in range(3000,1000000000):
        positived(i,count=0)
    end=time.time()
    tmies=end-start
    print("this tmieout ==> ",int(tmies),"s")

main()

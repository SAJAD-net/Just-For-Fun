def sum_squares_and_reverseit():
    sum_squar,squar_sum=0,0
    for i in range(1,101):
        sum_squar+=i**2
        squar_sum+=i
    print("this is the diffrence between the sum square first one hundred natural numbers and squre sum ==>",squar_sum**2-sum_squar)
sum_squares_and_reverseit()

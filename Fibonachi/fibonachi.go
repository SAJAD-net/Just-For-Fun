package main

import "fmt"

func main(){
	first, second, fib  := 0,1,0
	for item:=0; item <= 10; item+=1{
		fmt.Printf("[-]- This is [FIRST] number --> %d\n", first)
		fmt.Printf("[-]- This is [SECOND] number --> %d\n", second)
		fib = first+second
		fmt.Printf("[+]---> This is [FIBONACHI] number --> %d\n", fib)
		first, second = second, fib
	}
}

package main

import "fmt"


func main(){

	var first, second, fib int = 0,1,0
	var item int
	for item=0; item <= 10; item+=1{
		fmt.Printf("[-]- This is [FIRST] number --> %d\n", first)
		fmt.Printf("[-]- This is [SECOND] number --> %d\n", second)
		fib = first+second
		fmt.Printf("[+]---> This is [FIBONACHI] number --> %d\n", fib)
		first, second = second, fib
	}
}

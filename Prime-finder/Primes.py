from colorama import Fore,Back,init
init()
import os
primes = []
def is_prime(n):
	
	if n == 1:
		print(Fore.RED+'1 is special')
		return False
	for x in range(2,n):
		if n % x == 0:
			print(Fore.BLUE+'{} equals To {} x {}'.format(n,x,n//x))
			return False
	else:
		#print(Fore.GREEN,n,'is a prime number')
		primes.append(n)
def main():
	os.system("clear") if os.name == "posix" else os.system('cls')
	num1 = int(input(Fore.LIGHTBLACK_EX+'Please Enter Number1 : '))
	print(Fore.GREEN+'Ok')
	num2 = int(input(Fore.LIGHTBLACK_EX + "Enter Number2 : "))
	for n in range(num1,num2):
		is_prime(n)
	End=input(Fore.LIGHTBLACK_EX + 'Enter [Y/N] To Show a Prime Numbers Or Exit :')
	End=End.upper()
	if End == "Y":
		print(primes)	
	exits=input(Fore.LIGHTBLACK_EX + 'Enter [Y/N] To Try Again Or Exit :')
	exits=exits.upper()
	if exits == 'Y':
		main()
	else:
		return
main()
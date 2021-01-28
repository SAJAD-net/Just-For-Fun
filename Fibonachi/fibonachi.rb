def fibonachi
	system("clear")
	print"\t\t\t WELCOME TO FIBONACHI FINDER APP !! \n
#==> if you not enetr number, App start auto of 0\n\n"
    while true
		print"Please enter the [From] number ~$"
		numberf=gets.chomp
		print"Please enter the [To] number ~$"
		numbert=gets.chomp
		if numberf == "exit" 
			break
		end
		numberf=numberf.to_i
		numbert=numbert.to_i
	
		puts""
		first=numberf
		second=first+1
		for num in numberf..numbert
			puts"this is the first number ==> #{first}"
			puts"this is the second number ==> #{second}"
        	fib=first+second
        	first=second
        	second=fib
        	puts"\t this is the fibonachi numbers ==> #{fib}"
    	end
    	print"Press enter to back the apps :"
    	gets.chomp
    	system("clear")
	end
end
fibonachi

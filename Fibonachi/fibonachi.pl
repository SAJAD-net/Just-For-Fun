sub Fibonachi(){
	
	$first = 0;
	$second = 1;
	$fib = 0;

	for ($item = 0; $item <= 10; $item++){
		print"[!]- This is [FIRST] number --> ",$first,"\n";
		print"[!]- This is [SECOND] number --> ",$second,"\n";
		$fib = $first+$second;
		print"\t[+]---> This is [FIB] number --> ",$fib,"\n";
		$first = $second;
		$second = $fib; 
	}
}

Fibonachi();

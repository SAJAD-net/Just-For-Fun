#!/usr/bin/perl

sub files(){
	print"Enter your text \~\$ ";
	$text = <STDIN>;
	open(FILE1,"+<file.txt") or die "Can't open this file !";
	my $line;
	while ($line = $text){
		print FILE1 $line;
		print"OK, Query 1, Successfully !\n";
		close FILE1;
		return 1;
	}
}
files();

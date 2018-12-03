#!/usr/bin/perl

use Time::HiRes qw(gettimeofday tv_interval);

$t0 = [gettimeofday];
my $a =0;
for (my $i = 0; $i < 10000; $i++) {
	for (my $j = 0; $j < 10000; $j++) {
		$a++;
	}
}

$t1 = [gettimeofday];
$t0_t1 = tv_interval $t0, $t1;
print $t0_t1;
print " secondes \n";

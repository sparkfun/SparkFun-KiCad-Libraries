#!/usr/bin/perl -W

use feature qw(state);

sub usage();

if(scalar(@ARGV) < 4) {
	usage();
}

my $outfile = $ARGV[1];
my $size = $ARGV[3]; # in 'mm' or in 'in'
my $factor;
my $calibration;
my $layer = $ARGV[2];

open(FILE, '<', $ARGV[0]) || die("cannot open: $!");
my @infiledata = <FILE>;
close(FILE);

foreach $line (@infiledata) {
	my $tmp = $line;
	state $xmin = 0; # same as 'static xmin = 0;' in C
	state $xmax = 0;
	state $ymin = 0;
	state $ymax = 0;
	if($tmp =~ m/^(.*Dl)\ (.*)\ (.*)$/) {
		if($2 <= $xmin) {
			$xmin = $2;
		}
		if($2 >= $xmax) {
			$xmax = $2;
		}
		if($3 <= $ymin) {
			$ymin = $3;
		}
	        if($3 >= $ymax) {
			$ymax = $3;
		}
	}
	if( ($xmax - $xmin) > ($ymax - $ymin) ) {
		$calibration = ($xmax - $xmin);
	} else {
		$calibration = ($ymax - $ymin);
	}
	#print $xmin," - ",$xmax," - ",$ymin," - ",$ymax,"\n";
	#print $calibration;
}

if($size =~ m/^\d{1,3}\.\d{1,3}in$/) {
	$size =~ s/in//;
	$factor = 10000/$calibration*$size; # currently all KiCad native units are in 1/10000 in
} elsif($size =~ m/^\d{1,3}\.\d{1,3}mm$/) {
	$size =~ s/mm//;
	$factor = 10000/$calibration/25.4*$size;
} else {
	usage();
}

open(FILE,'>',$outfile) || die("cannot open: $!");
foreach $line (@infiledata) {
	my $tmp = $line;
	if($tmp =~ m/^(.*Dl)\ (.*)\ (.*)$/) {
		if( ($layer == 21) || ($layer == 15) ) { # top silkscreen or top copper
			print FILE $1," ",int($2*$factor)," ",int($3*$factor),"\n";
		} elsif ( ($layer == 20) || ($layer == 0) ) { # bottom silkscreen or bottom copper - needs horizontal mirroring
			print FILE $1," ",int((-1)*$2*$factor)," ",int($3*$factor),"\n";
		}
	} elsif($tmp =~ m/^T(\d{1})\ 0\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)\ ([A-Z]{1})\ ([A-Z]{1})\ (-{0,1}\d*)\ (\".*\")$/) {
		# always print module text on top-silkscreen (layer 21)
		# printing it on the bottom silkscreen seems to confuse KiCad
		# and things go haywire (text always appers on 'top'-whatever
		# when graphics are on 'bottom'-whatever and vice versa).
		print FILE "T$1 0 ",int($2*$factor)," ",int($3*$factor)," ",int($4*$factor)," ",int($5*$factor)," ",int($6*$factor)," ",$7," ",$8," 21 N ",$10,"\n"; 
	} elsif($tmp =~ m/^(.*DP)\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)\ (-{0,1}\d*)(.*)$/) {
		if( ($layer == 0) || ($layer == 15) ) { # on top/bottom copper layer - always print on top-copper to avoid crap. see above
			print FILE "$1 $2 $3 $4 $5 $6 $7 15\n";
		} elsif ( ($layer == 20) || ($layer == 21) ) { # on top/bottom silk - always print on top-silk to avoid crap. see above
			print FILE "$1 $2 $3 $4 $5 $6 $7 21\n";
		}
	}
	else {
		print FILE $line;
	}
}
close(FILE);

sub usage() {
	print "\nusage: scale.pl <infile.emp> <outfile.emp> <layer number> <size: e.g. 5.00mm or 0.25in>\n\n";
	print "The module will be scaled so that its largest dimension (x or y) matches <size>\n\n";
	print "KiCad layers:\n";
	print "-------------\n\n";
	print "Top    copper:      15\n";
	print "Bottom copper:	     0 (*)\n";
	print "Top    silkscreen:  21\n";
	print "Bottom silkscreen:  20 (*)\n\n";
	print "(*) To move the mirrored logo to bottom copper/silkscreen\n";
	print "    move the curser over it and press 'F' for flip layer.\n\n";
	print "    The layer-swap is not done in this script as KiCad\n";
	print "    gets confused and prints stuff on wrong layers.\n\n";
	exit;
}


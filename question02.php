<?php

$input = [1, 2, 1, 5];

$count = 0;
$outputString = "";

$i = 0;



while ($i < count($input) || $i < 0) {
	if ($i == 0) {
		$outputString = $input[$i];
	}else{
		$outputString = $outputString."->".$input[$i];
	}

	$i += $input[$i];

	$count++;
}


$outputString = $outputString."-><jump out>";

echo  "<pre>jumps = ".$count."(".htmlentities($outputString).")</pre>";

?>
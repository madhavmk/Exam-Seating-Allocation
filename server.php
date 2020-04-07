<?php

function upload($file,$dest){
	$fname = $file['name'];
	$ftmp = $file['tmp_name'];
    $dst = $dest . '/' . $fname;
	if(!move_uploaded_file($ftmp, $dst)){
		echo "I did not work for";
		var_dump($file);
		echo"<br/>";
    }
    return $fname;
}

function recurse_copy($src,$dst) { 
    $dir = opendir($src); 
    @mkdir($dst); 
    while(false !== ( $file = readdir($dir)) ) { 
        if (( $file != '.' ) && ( $file != '..' )) { 
            if ( is_dir($src . '/' . $file) ) { 
                recurse_copy($src . '/' . $file,$dst . '/' . $file); 
            } 
            else { 
                copy($src . '/' . $file,$dst . '/' . $file); 
            } 
        } 
    } 
    closedir($dir); 
} 

function execCommand($option,$name,$out,$conf='',$workload=''){

	if($option === 1){
		$command = 'java -jar '.$name.' > uploads/'.$out;
	}
	if($option === 2){
		$command = 'java -jar '.$name.' '.$conf. ' > uploads/'.$out;
	}
	if($option === 3){
		$command = 'java -jar '.$name.' '.$conf. $workload.' '.' > uploads/'.$out;
	}
	exec($command);
}


// main

$date = date_create();
$ts = date_timestamp_get($date);
//echo $_FILES['file1'] . $_FILES['file2'] . $_FILES['file3']; 
$src = './app';
$dest = $src . $ts; 
recurse_copy($src,$dest);
//echo "Sucess";
$file1 = upload($_FILES['file1'],$dest);
$file2 = upload($_FILES['file2'],$dest);
$file3 = upload($_FILES['file3'],$dest);

/*// change working dir
chdir($dest);
$command = "python3 create_groups.py " . $file1 . " " .  $file2 . " ". $file3 . " > out.txt";
exec($command);
$command = "tar -czvf Rooms.zip Rooms";
exec($command);
echo $dest . "/Rooms.zip"; */

echo "success";

?>
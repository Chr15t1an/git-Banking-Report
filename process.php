<?php



#Check Upload is Exel from coop
$uploaded_file = basename($_FILES["fileToUpload"]["name"]);
$info = new SplFileInfo($uploaded_file);
$exts = $info->getExtension();
if ( $exts !== "xls") {
	header("Location: /error.html");
	die();
	}

#Get Current Time Stamp
$date = new DateTime();
$date = $date->getTimestamp();
$dir = "uploads/";
$dir.=$date;

#Create Directory to work from 
mkdir($dir, 0777);

$dir .= "/";

#echo "<br/>"."dir ".$dir."<br/>";
#echo "File".basename( $_FILES["fileToUpload"]["name"])."<br/>";

$target_file = $dir.basename($_FILES["fileToUpload"]["name"]);

    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
		header("Location: /exports.php");
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
	


	
exec('sudo python3 process.py'.' '.$dir.' '.basename( $_FILES["fileToUpload"]["name"]));

#pass timestamp + Filename


# uploads/1493236781 banking-report-20170424151944.xls



?>
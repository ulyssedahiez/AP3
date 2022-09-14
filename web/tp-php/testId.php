<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Teste ID</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
 <?php
 $users1 = [
    "JLecat"=>"lecat01",
    "CChaudron"=>"chaudron01",
    "MBizot"=>"bizot01"
  ];
  $username = $_POST["username"];
  $password = $_POST["password"];

  function   connection ($login  , $pass, $list) {
    if(array_key_exists($login, $list)) {
        if($list[$login]==$pass){
            return true;
        }    
    }
    else{
        return false;
    }
}
$resultConnect = connection($username, $password, $users1);
 ?>
<?php 
if($resultConnect){
?>
 <h1> Correct !</h1>
 <?php }else{?>
    <h1></h1>
    <h1> incorrect !</h1>
<?php } ?>
<input type="button" name="lien1" value="retour" onclick="self.location.href='./td3.php'">
</body>
</html>
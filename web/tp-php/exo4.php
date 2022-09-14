
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>exo 4</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
<input type="button" name="lien1" value="retour" onclick="self.location.href='./td3.php'">
<input type="button" name="lien1" value="session destroy" onclick="<?php session_destroy();?>">
<br /><br /><br />
<form   method ="post" action ="exo4.php">
<label for="username">entrez un nombre :</label><br />
    <input   type="text" name="nombre" />
    <input   type="submit" value="Validate" />
</form >
 <?php
 session_start();
 if(!isset($_SESSION ["mesnombre"])){
    $_SESSION ["mesnombre"] = [];

 }

if(isset($_POST["nombre"])){
    array_push($_SESSION ["mesnombre"], $_POST["nombre"]);
}
if(count($_SESSION ["mesnombre"])>0){
    foreach($_SESSION ["mesnombre"] as $nombre){
        echo "$nombre</br>";
    }
}
 ?>
</body>
</html>
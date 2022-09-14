<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>checkout</title>
  <link rel="stylesheet" type="text/css" href="./style.css" media="all"/>
  <script src="script.js"></script>
</head>
<body>
  <h2>checkout</h2>
</br>
<?php include("navbar.php");


$nom = "pas de depart";
$prenom = "pas de arrivé";
$age = 0;
if(isset($_SESSION ["age"])){
    $age  = $_SESSION["age"];
}
if(isset($_SESSION ["nom"])){
  $nom  = $_SESSION["nom"];
}
if(isset($_SESSION ["prenom"])){
  $prenom  = $_SESSION["prenom"];
}
?>
<p>nom : <?php  echo "$nom"; ?> prenom : <?php  echo "$prenom"; ?> age : <?php  echo "$age"; ?></p>




</body>
</html>
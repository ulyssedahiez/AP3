<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>navbar</title>
  <link rel="stylesheet" type="text/css" href="./style.css" media="all"/>
  <script src="script.js"></script>
</head>
<body height = "200px">
<?php   
session_start();
$depart = "pas de depart";
$arrive = "pas de arrivé";

if(isset($_SESSION ["depart"])){
    $depart  = $_SESSION["depart"];
}
if(isset($_SESSION ["arrive"])){
    $arrive  = $_SESSION["arrive"];
}

if(isset($_SESSION ["distance"])){
    $distance  = $_SESSION["distance"];
}
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
?>
<ul class="menu">
<li>
                <a href="index.php">acceuil</a>
            </li>
            <li>
                <a href="trajet.php">trajet</a>
            </li>
            <li>
                <a href="voyageur.php">voyageur</a>
            </li>
        
                <a href="client.php">client</a>
            </li>
            <li>
                <a href="checkout.php">checkout</a>
            </li>
            
        </ul>

        <p>depart : <?php  echo "$depart"; ?> arrivé : <?php  echo "$arrive"; ?> distance : <?php  echo "$distance"; ?> </p>
        <p>nom : <?php  echo "$nom"; ?> age : <?php  echo "$age"; ?> carte de reduc : <?php  ?> </p>

  
</body>
</html>
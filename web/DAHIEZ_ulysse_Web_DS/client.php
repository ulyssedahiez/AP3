<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>client</title>
  <link rel="stylesheet" type="text/css" href="./style.css" media="all"/>
  <script src="script.js"></script>
</head>
<body>
  <h2>client</h2>
</br>
<?php include("navbar.php"); ?>

<form   method ="post" action ="index.php">

<label for="nom">nom:</label><br />
    <input   type="text" name="nom" id="nom" />
    <br />
    <label for="age">age:</label><br /> 
    <input type="number" id="age" name="age"
       min="0" >
       <br />
    <label for="reduc">reduction:</label><br />
    <input type="checkbox" id="reduc" name="reduc" value="reduc"
             >
   
             <br /><br />
    <input   type="submit" value="Validate" />
</form >

<img class="fit-picture"
     src="./homme.jpg"
     alt="homme">

     <?php
 if(!isset($_SESSION ["age"])){
    $_SESSION ["age"] = 0;

 }
 if(!isset($_SESSION ["nom"])){
  $_SESSION ["nom"] = "";

}
if(!isset($_SESSION ["reduc"])){
  $_SESSION ["reduc"] = "";

}

if(isset($_POST["age"])){
  $_SESSION ["age"] = $_POST["age"];
}
if(isset($_POST["nom"])){
  $_SESSION ["nom"] = $_POST["nom"];
}
if(isset($_POST["reduc"])){
 $_SESSION ["reduc"] = $_POST["reduc"];
}



 ?>

</body>
</html>
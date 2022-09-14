
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>exo 5</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
<input type="button" name="lien1" value="retour" onclick="self.location.href='./exo5.php'">


<form   method ="post" action ="exo5p3.php">
<?php if(isset($_POST["nom"])){ ?>
    <div>
      <label for="nom">Nom:</label><br />
      <input type="text" id="nom" name="nom">
  </div>

    
<?php } ?>
<?php if(isset($_POST["prenom"])){ ?>
  <div>
      <label for="prenom">Prénom:</label><br />
      <input type="text" id="prenom" name="prenom">
  </div>
  <?php } ?>
  <?php if(isset($_POST["age"])){ ?>
  <div>
      <label for="age">age:</label><br />
      <input type="number" id="age" name="age">
</div>
<?php } ?>
<?php if(isset($_POST["lunette"])){ ?>
<div id="lunette">

<input type="checkbox" name="lunette" checked>Lunette</input>


</div>
<?php } ?>
<?php if(isset($_POST["gauchedroite"])){ ?>
<label for="gauchedroite">vous etes:</label>

<select name="gaucherDroitier" id="gaucherDroitier">
    <option value="">--Please choose an option--</option>
    <option value="Droitier">Droitier</option>
    <option value="Gaucher">Gaucher</option>
    
</select>
  
<?php } ?>
  <br />
  <input type="submit" value="Sign in">
</form >


 <?php
  if(isset($_POST["nom"])){
    $nom = $_POST["nom"];
 }
 if(isset($_POST["prenom"])){
    $prenom = $_POST["prenom"];
 }
 if(isset($_POST["age"])){
    $age = $_POST["age"];
 }
 if(isset($_POST["lunette"])){
    $lunettes = $_POST["lunette"];
 }
 if(isset($_POST["gauchedroite"])){
    $gauchedroite = $_POST["gauchedroite"];
 }

 ?>
</body>
</html>
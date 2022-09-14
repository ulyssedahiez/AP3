
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>exo 5</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
<input type="button" name="lien1" value="retour" onclick="self.location.href='./td3.php'">
</br></br>
<form   method ="post" action ="exo5p2.php">

<fieldset>
    <legend>selectinonnez les valeurs que vous voulez renseigner :</legend>
    </br>
    <div>
      <input type="checkbox" id="prenom" name="prenom"  checked>
      <label for="prenom">Prénom</label>
    </div>

    <div>
      <input type="checkbox" id="nom" name="nom">
      <label for="nom">Nom</label>
    </div>
    <div>
      <input type="checkbox" id="age" name="age">
      <label for="age">Age</label>
    </div>
    <div>
      <input type="checkbox" id="lunette" name="lunette">
      <label for="lunette">Lunette</label>
    </div>
    <div>
      <input type="checkbox" id="gauchedroite" name="gauchedroite">
      <label for="gauchedroite">Gauche / Droite</label>
    </div>

    </br>
    <input   type="submit" value="Suivant" />
</fieldset>


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
    $lunette = $_POST["lunette"];
 }
 if(isset($_POST["gauchedroite"])){
    $gauchedroite = $_POST["gauchedroite"];
 }

 ?>

</body>
</html>
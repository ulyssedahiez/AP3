<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>billets de train</title>
  <link rel="stylesheet" type="text/css" href="./style.css" media="all"/>
  <script src="script.js"></script>
</head>
<body>
  <h2>billet</h2>
</br>
<?php include("navbar.php"); ?>

<form   method ="post" action ="trajet.php">
<label for="username">depart:</label><br />
    <input   type="text" name="depart" id="depart" />
    <label for="username">arrive:</label><br />
    <input   type="text" name="arrive" id="arrive" />
    <input type="number" id="distance" name="distance"
       min="0" >

       <fieldset>
    <legend>depart / retour:</legend>

    <div>
      <input type="radio" id="aller" name="aller" value="aller"
             checked>
      <label for="aller">aller</label>
    </div>

    <div>
      <input type="radio" id="aller" name="aller" value="aller">
      <label for="allour">aller-retour</label>
    </div>
</fieldset>

    <input   type="submit" value="Validate" />
</form >

</br>

<img class="fit-picture"
     src="./voiture.jpg"
     alt="voiture">

     <?php
 if(!isset($_SESSION ["depart"])){
    $_SESSION ["depart"] = "";

 }
 if(!isset($_SESSION ["arrive"])){
  $_SESSION ["arrive"] = "";

}
if(!isset($_SESSION ["distance"])){
  $_SESSION ["distance"] = 0;

}

if(isset($_POST["depart"])){
  $_SESSION ["depart"] = $_POST["depart"];
}
if(isset($_POST["arrive"])){
  $_SESSION ["arrive"] = $_POST["arrive"];
}
if(isset($_POST["distance"])){
  $_SESSION ["distance"] = $_POST["distance"];
}



 ?>


</body>
</html>
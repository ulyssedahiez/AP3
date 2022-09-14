
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
<p>
    Bonjour <?php if(isset($_POST["nom"])){echo $nom;} ?> <?php if(isset($_POST["prenom"])){echo $prenom;} ?>
<p>

<?php if(isset($_POST["age"])){ ?>

    <p>tu as <?php echo $age ?> ans.</p>
    
<?php   } ?>

    <?php if(isset($_POST["lunette"])){ ?>
        <?php if($lunette){?>
            <p>Vous portez des lunette</p>
        <?php }else{?>
    
    
            <p>Vous ne portez pas de lunette</p>
    <?php }  } ?>



</body>
</html>
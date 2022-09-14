
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Titre de la page</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
<h1>Mon TP PHP </h1>

Exercice 1 :<br /><br />
<?php
$tqt = "hello world !";
echo $tqt;
?><br /><br />
Exercice 2 :<br /><br />
<form   method ="post" action ="td3.php">
    <input   type="text" name="myname" />
    <input   type="submit" value="Validate" />
</form >
<?php
$myname = "indisponible";
if(isset($_POST["myname"])){

    $myname = $_POST["myname"];
}
?>
<img width = "200px" src="./<?php echo $myname;?>.jpg">
<br /><br />
Exercice 3 :<br /><br />
<form   method ="post" action ="testid.php">
  <div>
      <label for="username">Username:</label><br />
      <input type="text" id="username" name="username">
  </div>

  <div>
      <label for="pass">Password (3 characters minimum):</label><br />
      <input type="password" id="pass" name="password"
            minlength="3" required>
  </div>
  <br />
  <input type="submit" value="Sign in">
</form >
<?php
if(isset($_POST["username"]) && isset($_POST["username"])){
  $myname = $_POST["username"];
  $password = $_POST["password"];
}
?><br /><br />
Exercice 4 :<br /><br />
<input type="button" name="lien1" value="exo4" onclick="self.location.href='./exo4.php'">
<br /><br />
Exercice 5 :<br /><br />
<input type="button" name="lien1" value="exo5" onclick="self.location.href='./exo5.php'">


</body>
</html>
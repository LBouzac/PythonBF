<?php

// Page pour tester l'app brute force

// Connexion a la bdd
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'bf_test');

$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

if ($conn->connect_error) {
    die("Erreur de connexion : " . $conn->connect_error);
}

// Si le formulaire est soumis
if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Requete pour verifier si l'utilisateur existe
    $sql = "SELECT * FROM login WHERE login = '$username' AND mdp = '$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "Connexion reussie";
        header("Location: accueil.php");
        exit();
    } else {
        echo "Nom d'utilisateur ou mot de passe incorrect";
    }
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Page de connexion</title>
</head>

<body>
    <h2>Connexion</h2>
    <form method="post" action="index.php">
        <label>Nom d'utilisateur</label>
        <input type="text" name="username" required>
        <br>
        <label>Mot de passe</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit" name="submit">Connexion</button>
    </form>
</body>
</html>
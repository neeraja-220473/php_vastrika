
<?php
$conn = mysqli_connect("localhost", "root", "", "neerajadb");

if (!$conn) {
    die("Database connection failed");
}

$username = $_POST['username'];
$email = $_POST['email'];
$password = $_POST['password'];

$sql = "SELECT * FROM user_details WHERE username='$username' AND password='$password'";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    echo "<h2 style='color:green; text-align:center;'>Login Succesful </h2>";
} else {
    echo "<h2 style='color:red; text-align:center;'>Invalid Username or Password </h2>";
}

mysqli_close($conn);
?>

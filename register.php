<?php
$conn = mysqli_connect("localhost", "root", "", "neerajadb");

if (!$conn) {
    die("Database connection failed");
}

function registrationCounter() {
    static $count = 0;
    $count++;
    echo "<p>Total registrations in this session: $count</p>";
}

function registerUser() {
    global $conn;

    $username = $_POST['username'];
    $email    = $_POST['email'];
    $password = $_POST['password'];

    $sql = "INSERT INTO user_details (username, email, password)
            VALUES ('$username', '$email', '$password')";

    if (mysqli_query($conn, $sql)) {
        echo "<h2 style='color:green; text-align:center;'>Registration Successful </h2>";
        registrationCounter();
    } else {
        echo "<h2 style='color:red; text-align:center;'>Registration Failed </h2>";
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    registerUser();
}

mysqli_close($conn);
?>
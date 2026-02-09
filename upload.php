<?php
if (isset($_FILES['myfile'])) {

    $fileName = basename($_FILES['myfile']['name']);
    $tempName = $_FILES['myfile']['tmp_name'];
    $error    = $_FILES['myfile']['error'];

    if ($error === 0) {

        $uploadDir = "uploads/";
        $filePath = $uploadDir . $fileName;

        if (move_uploaded_file($tempName, $filePath)) {
            header("Location: index.php?file=" . urlencode($fileName));
            exit();
        } else {
            echo "Failed to upload file.";
        }

    } else {
        echo " Upload error code: " . $error;
    }
}
?>
<?php
    $destinatario = 'kevin.pizarrosanz@gmail.com';
    // Correo que recibira el mensaje del formulario

    $nombre = $_POST['name'];
    $email = $_POST['email'];
    $numero = $_POST['number'];
    $asunto = $_POST['asunto'];
    $mensaje = $_POST['message'];

    $header = "Enviado desde el portafolio KevinP";
    $mensajeCompleto = $mensaje . "\nAtentamente: " . $nombre;

    mail($destinatario, $asunto, $mensajeCompleto, $header);
    echo "<script>alert('correo enviado exitosamente')</script>";
    echo "<script> setTimeout(\ "location.href='index.html'\",1000)</script>";

?>


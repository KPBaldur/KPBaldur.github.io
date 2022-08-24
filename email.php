<?php

if (isset($_POST['enviar'])) {
    if (!empty($_POST['nombre']) && !empty($_POST['mensaje']) && !empty($_POST['correo'])) {
        $nombre = $_POST['name'];
        $mensaje = $_POST['mensaje'];
        $correo = $_POST['correo'];
        $header = "From: noreply@example.com" . "\r\n";
        $header.= "Reply-to: noreply@example.com" . "\r\n";
        $header.= "X-Mailer: PHP/" . phpversion();
        mail($email,$asunto,$msg,$header);
        if ($mail) {
            echo "<h4>¡Mail enviado exitosamente!</h4>";
        }
    }
}
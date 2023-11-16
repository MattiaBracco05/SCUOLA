<?php
session_start();
session_unset();
session_destroy();

//Cancello il cookie (impostando come già scaduto)
setcookie('user', '', time() - 1);

//Ritorno alla pagina principale di login
header("Location: index.html");
exit();
?>
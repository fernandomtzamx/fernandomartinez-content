<?php
/**
 * Portada de www.fernandomartinez.mx.
 * WordPress vive en /dev (sus archivos no se mueven) y se sirve desde la raíz.
 * Método oficial "Dar a WordPress su propio directorio".
 */
define( 'WP_USE_THEMES', true );
require __DIR__ . '/dev/wp-blog-header.php';

<?php
/**
 * Plugin Name: fernandomartinez.mx: auth para API REST
 * Description: Permite que el agente de contenido publique por la API REST con contraseña de aplicación en servidores que borran el encabezado Authorization (LiteSpeed, FastCGI) o con plugins que consultan el usuario antes de tiempo. No abre acceso nuevo: sin contraseña de aplicación válida todo sigue rechazado. Funciona igual en /dev y en la raíz.
 * Version: 1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

// 1. Recuperar la credencial si el servidor quitó Authorization.
//    Acepta un encabezado alterno X-Agente-Auth con el mismo "Basic base64(usuario:contraseña)".
if ( empty( $_SERVER['PHP_AUTH_USER'] ) ) {
	$fm_header = '';
	if ( ! empty( $_SERVER['HTTP_X_AGENTE_AUTH'] ) ) {
		$fm_header = $_SERVER['HTTP_X_AGENTE_AUTH'];
	} elseif ( ! empty( $_SERVER['HTTP_AUTHORIZATION'] ) ) {
		$fm_header = $_SERVER['HTTP_AUTHORIZATION'];
	} elseif ( ! empty( $_SERVER['REDIRECT_HTTP_AUTHORIZATION'] ) ) {
		$fm_header = $_SERVER['REDIRECT_HTTP_AUTHORIZATION'];
	}
	$fm_header = trim( (string) $fm_header );
	if ( 0 === stripos( $fm_header, 'basic ' ) ) {
		$fm_decoded = base64_decode( substr( $fm_header, 6 ), true );
		if ( false !== $fm_decoded && false !== strpos( $fm_decoded, ':' ) ) {
			list( $fm_user, $fm_pass ) = explode( ':', $fm_decoded, 2 );
			$_SERVER['PHP_AUTH_USER'] = $fm_user;
			$_SERVER['PHP_AUTH_PW']   = $fm_pass;
		}
	}
}

// 2. Reconocer peticiones a la API REST desde el inicio (incluye /dev/wp-json/),
//    aunque otro plugin consulte el usuario antes de que WordPress defina REST_REQUEST.
add_filter(
	'application_password_is_api_request',
	function ( $is_api_request ) {
		if ( $is_api_request ) {
			return true;
		}
		$uri = isset( $_SERVER['REQUEST_URI'] ) ? (string) $_SERVER['REQUEST_URI'] : '';
		return false !== strpos( $uri, '/wp-json/' ) || isset( $_GET['rest_route'] );
	}
);

// 3. Si alguien fijó el usuario como anónimo antes de tiempo, recalcularlo
//    al iniciar la API REST, cuando la contraseña de aplicación sí se evalúa.
add_action(
	'rest_api_init',
	function () {
		if ( ! empty( $_SERVER['PHP_AUTH_USER'] ) && 0 === get_current_user_id() ) {
			$GLOBALS['current_user'] = null;
			wp_get_current_user();
		}
	},
	0
);

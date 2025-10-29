# sistema de inicio de sesión como si fuera un usuario, con intentos (sin beake)
correctos = {
    "ruben": "@ITB2025.",
    "admin": "@ITB2025."
}
intentos = 3
while intentos > 0:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in correctos and correctos[usuario] == contraseña:
        print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario))
        break
    else:
        intentos -= 1
        print("Credenciales incorrectas. Te quedan {} intentos.".format(intentos))
        if intentos == 0:
            print("Has agotado todos los intentos. Acceso denegado.")
        else:
            print("Por favor, inténtalo de nuevo.")



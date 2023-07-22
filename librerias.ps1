try {
    # Instala la libreri­a pytube
    pip install pytube

    # Instala la libreri­a moviepy
    pip install moviepy

    # Mostrar mensaje de finalizacion
    Write-Host "La instalacion de las librerias pytube y moviepy se ha completado correctamente."
}
catch {
    # En caso de que ocurra un error durante la instalacion, muestra el mensaje de error
    Write-Host "Error durante la instalacion de las librerias: $_"
}

# Solicitar al usuario que presione Enter para salir
Write-Host "Presiona Enter para cerrar esta ventana."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

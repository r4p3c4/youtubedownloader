#instala la libreria pytube
pip install pytube
#instala la libreria moviepy
pip install moviepy
# Mostrar mensaje de finalizacion
Write-Host "La instalacion de las librerias pytube y moviepy se han completado correctamente."
# Solicitar al usuario que presione Enter para salir
Write-Host "Presiona Enter para cerrar esta ventana."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
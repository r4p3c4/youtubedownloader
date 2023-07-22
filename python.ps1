# Define la ruta del instalador y la versión de Python que deseas instalar
$PythonInstallerUrl = "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"
$PythonVersion = "3.11.4"
# Define la ubicación donde deseas guardar el instalador
$InstallerPath = "$env:TEMP\python_installer.exe"
# Descarga el instalador de Python desde el sitio oficial
Invoke-WebRequest -Uri $PythonInstallerUrl -OutFile $InstallerPath
# Ejecuta el instalador de Python de manera silenciosa y marca la casilla "Agregar Python X.X al PATH"
Start-Process -FilePath $InstallerPath -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
# Borra el instalador descargado una vez que se haya completado la instalacion
Remove-Item $InstallerPath
# Mostrar mensaje de finalizacion
Write-Host "La instalacion de Python $PythonVersion se ha completado correctamente."
# Solicitar al usuario que presione Enter para salir
Write-Host "Presiona Enter para cerrar esta ventana."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

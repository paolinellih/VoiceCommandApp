Write-Host "Building EXE..."
py -m PyInstaller --onefile --noconsole --add-data "src\funny_warning_image.jpg;." --hidden-import="transcriber" src\main.py
Write-Host "Build complete! EXE is in 'dist/'"
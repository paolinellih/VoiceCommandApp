# Navigate to the src folder
cd .\src\

# Build the EXE
Write-Host "Building EXE..."
py -m PyInstaller --onefile --noconsole --add-data "image.jpg;." main.py

# Notify when the build is complete
Write-Host "Build complete! EXE is in 'dist/'"
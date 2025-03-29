Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate

.\setup_env.ps1

.\build_exe.ps1
Or
py -m PyInstaller --onefile --noconsole --add-data "src\funny_warning_image.jpg;." --hidden-import="transcriber" --debug all src\main.py
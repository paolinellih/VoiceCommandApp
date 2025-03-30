# 🎤 Windows Voice Command Application

Welcome to the **Windows Voice Command Application**! This project demonstrates how Python can be used for voice command tasks and fetching advice from APIs. It also includes a **unique IoT integration**, where the system can control other computers over a local network. You can run it from the command line or even create a standalone EXE for easy use. 🚀

## 🎉 What You'll Learn:
- How to control your computer using voice commands (open browser, calculator, take screenshots, etc.).
- Fetch random advice from an API and translate it to Portuguese.
- How to create a Python `.EXE` file that can be run without Python installed!
- IoT Integration: Control other PCs running the same project over a local network via Flask API.

## 💻 Getting Started

Before you can run the project, you'll need to set up a few things. Follow these easy steps:

### 1. Install Visual Studio Code (VS Code) (Optional but Recommended)

**Why?**: VS Code is a code editor that will make writing and running Python code much easier!

- Download it from [VS Code's official website](https://code.visualstudio.com/).
- Install VS Code and make sure you also install the Python extension for VS Code!

### 2. Install Python

**Why?**: Python is the programming language used to build this app, so you'll need it to run the project.

- Download Python from [Python's official website](https://www.python.org/downloads/).
- During installation, **make sure you check the box that says "Add Python to PATH"**. This will make it easier to run Python from the command line!

### 3. Clone the Repository

Now that you have the necessary tools installed, it's time to get the project code:

- Open a terminal/command prompt.
- Navigate to the folder where you want the project to be.
- Run this command to clone the project repository:
  
  ``git clone https://github.com/paolinellih/VoiceCommandApp.git``

### 4. Create a Virtual Environment (Recommended)

A virtual environment keeps your project's dependencies isolated, so it's a good idea to create one!

1. Open a terminal/command prompt and navigate to your project folder.
2. Run this command to create a virtual environment:

   ``python -m venv venv``

3. To activate the virtual environment, run:

   - **Windows**: ``venv\Scripts\activate``
   - **Mac/Linux**: ``source venv/bin/activate``

### 5. Install Dependencies

With your virtual environment activated, you need to install the libraries that the project requires:

1. Make sure you're in the project directory (where the `requirements.txt` file is located).
2. Run this command:

   ``pip install -r requirements.txt``

### 6. Run the Project

Now that everything is set up, you can run the project!

1. Open a terminal in your project folder source code '/src'.
2. Run this command:

   ``python main.py``

The app will listen for voice commands and respond accordingly!

### 7. IoT Integration - Remote Control Over Network

When you run the project, it will first prompt you for the IP address of the computer you wish to control. The application acts as both a client and a server depending on the IP provided:
- Server Mode: If you enter localhost or 127.0.0.1, it will act as the server and listen for commands.
- Client Mode: If you enter a different computer's IP address on the same network, it will send commands to that computer running the project.

This allows you to control other computers running the same project over the local network via the Flask API, making it an IoT integration!

### 8. Create the `.EXE` File

Want to make your voice command app a standalone EXE file? Here’s how you can do it:

1. Open a terminal in your project folder.
2. Run this command to create the `.EXE`:

   ``pyinstaller --onefile --noconsole --add-data "image.jpg;." main.py``

   This will bundle everything into a single executable file (`main.exe`) without a console window appearing when you run it.

   > **Note**: Replace `image.jpg` with any other image you may want to include in your EXE.

3. Once the build completes, you’ll find the `.EXE` file in the `dist` folder.

### 9. Test the EXE

- Go to the `dist` folder and double-click on `main.exe` to run the application.

Your voice commands and API fetching features should be ready to go! 🎤

---

## 📝 Project Commands

🔍 Discover the Hidden Commands! 🔍

Say "Oi Carol!" to wake her up, and then try these commands:

1️⃣ "abrir calculadora" – Opens the calculator.

2️⃣ "abrir navegador" – Launches the web browser.

3️⃣ "diminuir brilho" – Lowers the screen brightness.

4️⃣ "aumentar brilho" – Brightens the screen.

5️⃣ "capturar tela" – Takes a screenshot.

6️⃣ "quero um conselho" – Fetches a random piece of advice and translates it to Portuguese.

And there are more hidden commands waiting to be discovered!
Can you find them all? 🤫💡

Feel free to change these commands or add your own!

---

## 🌟 Enjoy Exploring!

This project is just the beginning! You can expand it by adding more voice commands, integrating smart devices (IoT), or even building more useful features. I hope you have fun experimenting and learning!

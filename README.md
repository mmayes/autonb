# 🛫 AutoNB: Automated Navblue PBS Runs
AutoNB is a Python-based automation tool designed to simplify and streamline the process of running Navblue PBS schedule runs, customized for C5's version of Navblue PBS.

## 🖥️ Installation & Setup

### Prerequisites
**Google Chrome** must be installed on your system. Download from [google.com/chrome](https://www.google.com/chrome/)
- The app uses Selenium to automate Chrome
- ChromeDriver is automatically managed, but Chrome itself must be installed manually

### 1. Install Python
**MacOS**
- **Option A (Recommended):** Install via Homebrew: `brew install python`
- **Option B:** Download the installer from [python.org](https://www.python.org/downloads/macos/)

**Windows**
- **Option A (Recommended):** Install via Chocolatey: `choco install python`
  - If you don't have Chocolatey, install it from [chocolatey.org](https://chocolatey.org/install)
- **Option B:** Download the installer from [python.org](https://www.python.org/downloads/windows/)
  - **IMPORTANT:** Check the box **"Add Python to PATH"** during installation.

### 2. Credentials Setup (Required)
Create a file named `userInfo.py` in the project root directory. This file should contain your NavBlue credentials:

```python
username = 'YourUsername'
password = 'YourPassword'
```

**Note:** `userInfo.py` is included in `.gitignore` and will never be tracked by Git to keep your credentials secure. If you leave `userInfo.py` empty or don't create it, the Streamlit UI will prompt you for credentials. However, **CLI mode requires this file to be present and populated.**

## 🚀 Running the Application

### Option 1: Streamlit UI (Recommended)
The easiest way to use AutoNB is via the web interface.

**MacOS / Linux**
1. Open Terminal.
2. Navigate to the project folder.
3. Run: `./run_app.sh`

**Windows**
1. Open the project folder.
2. Double-click `run_app.bat`.

This will automatically install dependencies and launch the browser-based UI where you can configure and run your automation.

**Troubleshooting (Windows)**
If you see an error like `'python' or 'pip' is not recognized`:
- Ensure Python is installed.
- Re-run the Python installer and select **"Modify"**, then ensure **"Add Python to environment variables"** is checked.
- Or, manually add the Python installation path to your system's PATH.

### Option 2: Manual CLI Mode
For advanced users who prefer the command line or want to run headless scripts.

1. Edit `config.py` to set your desired run parameters (Base, Seat, Thresholds, etc.).
2. Ensure `userInfo.py` is set up with your credentials.
3. Run the script:
   - For **Basic Runs**: `python3 main.py`
   - For **Unstack Runs**: `python3 mainUnstack.py`

### config.py
Most of the settings for CLI mode are contained in `config.py`. See the inline documentation in that file for usage of all variables. Note that the UI overrides these settings when running in Streamlit mode.

## 📁 Project Structure
| File      | Purpose                                                                                                 |
|-----------|----------------------------------------------------------------------------------------------------------|
| **app.py** | **Main Streamlit UI application - run this to use the web interface** |
| **run_app.sh** | Helper script to install dependencies and launch the app (Mac/Linux) |
| **run_app.bat** | Helper script to install dependencies and launch the app (Windows) |
| main.py   | Legacy CLI entry point for executing schedule runs |
| mainUnstack.py | Legacy CLI entry point for unstack runs |
| config.py | Default configuration settings (can be overridden in the UI) |
| userInfo.py | NavBlue PBS credentials (username/password) |
| basicRun.py | Handles the basic PBS run scenarios |
| unstackRun.py | Handles unstack PBS run scenarios |
| run_logic.py | Logic for generating run parameters |
| browserSetup.py | Selenium browser setup and login |
| seleniumSetup.py | ChromeDriver setup using webdriver-manager |
| requirements.txt | Python dependencies | 


## 📄 License

Distributed under the BSD-3-Clause License — free to use and modify with attribution.
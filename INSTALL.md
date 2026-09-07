# Installation and IDE Setup

## Fresh install of python3 and selenium on MacOS Tahoe (26)
1. Follow instructions at https://brew.sh/ to install Homebrew
2. Install python using `brew install python`
3. Verify Installation:
   * Close and relaunch the terminal to ensure the system recognizes the newly installed Python.
   * Type `python3 --version` and press Enter. This should display the installed Python version.
   * You can also type python to open the Python interactive shell.
4. Install git `brew install git`
5. Install github-desktop (optional) `brew install --cask github`
6. Install chromedriver `brew install chromedriver`
9. Install PyCharm from https://www.jetbrains.com/pycharm/download/ (or use your favorite Python IDE)
10. Verify PIP installed `pip --version`
11. Install Selenium `pip install selenium`

## Fresh install of python3 and selenium on Windows 11
1. Follow instructions at https://chocolatey.org/install to install Chocolatey
2. Install python using `choco install python`
   * If prompted to accept licenses or run scripts during the installation, type Y for yes or A for all. To avoid prompts, you can add -y to the command:
   * `choco install python -y`
4. Verify Installation:
   * Close and relaunch the terminal to ensure the system recognizes the newly installed Python.
   * Type `python --version` and press Enter. This should display the installed Python version.
   * You can also type python to open the Python interactive shell.
5. Install git `choco install git`
6. Install github-desktop (optional) `choco install github-desktop`
7. Install chromedriver `choco install chromedriver`
9. Install PyCharm from https://www.jetbrains.com/pycharm/download/ (or use your favorite Python IDE)
10. Verify PIP installed `py -m pip --version`
11. Install Selenium `py -m pip install selenium`

## Import project into PyCharm
1. If using PyCharm, need to add selenium to the project
   * Go to PyCharm->Preferences->Project XXXXX->Project Interpreter
   * Then click the + and it will install selenium
   * Might be able to specify interpreter and packages from system when you create a project

### Keep homebrew up to date
##### From https://docs.brew.sh/FAQ
First update all package definitions (formulae) and Homebrew itself: `brew update`

You can now list which of your installed packages (kegs) are outdated with: `brew outdated`

Upgrade everything with: `brew upgrade`

Or upgrade a specific formula with:`brew upgrade <formula>`

### Keep Chocolatey up to date
Once installed, Chocolatey can be upgraded in exactly the same way as any other package that has been installed using Chocolatey. Simply use the command to upgrade to the latest stable release of Chocolatey: `choco upgrade chocolatey`
# autonb
Automated way to do NAVBLUE schedule runs


### Fresh install of python3 and selenium on High Sierra
1. Follow instructions at https://docs.python-guide.org/starting/install3/osx/
2. Download and install command line tools from Apple Developer https://developer.apple.com/download/more/
3. Install Homebrew with command given in the python installation guide
4. Create the .profile file in your home directory and then open it in textedit
	1. `touch ~/.profile`
	2. `open -e ~/.profile`
5. The .profile file should be empty so add this line to it:
	1. `export PATH="/usr/local/opt/python/libexec/bin:$PATH"`
6. Then install python as instructed in the installation guide
7. Check to see what version of python was installed and that it runs properly
	1. `python --version`
8. Then install selenium using pip:
	1. `pip install selenium`
9. You can check to see what version of selenium was installed by:
	1. `pip freeze`
10. Install drivers to interface with the different browsers
	1. Can do manually via https://selenium-python.readthedocs.io/installation.html
	2. Chrome - https://sites.google.com/a/chromium.org/chromedriver/downloads
	3. or [this page](https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/) mentions
		1. `brew install --cask chromedriver`
11. Install some sort of IDE. CodeRunner via the appstore. Can download PyCharm community edition from their website or use homebrew.
	1. `brew install --cask pycharm-ce`
12. If using PyCharm, need to add selenium to the project
	1. Go to PyCharm->Preferences->Project XXXXX->Project Interpreter
	2. Then click the + and it will install selenium
	3. Might be able to specify interpreter and packages from system when you create a project


### Keep homebrew up to date
##### From https://docs.brew.sh/FAQ
To update homebrew:
`brew update`

To find out what is out of date:
`brew outdated`

Upgrade everything with:
`brew upgrade`

To list the versions of installed casks:
`brew cask list --versions`

As of December 2017, you can also keep Brew Cask up to date ([per Stack Overflow](https://stackoverflow.com/questions/31968664/upgrade-all-the-casks-installed-via-homebrew-cask))
`brew cask upgrade`

However this will not update casks that do not have versioning information (version :latest) or applications that have a built-in upgrade mechanism (auto_updates true). To reinstall these casks (and consequently upgrade them if upgrades are available), run the upgrade command with the --greedy flag like this:
`brew cask upgrade --greedy`
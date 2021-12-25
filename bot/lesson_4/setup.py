from setuptools import setup

APP=['desktopApp.py']
OPTIONS = {
	'iconfile':'icon.png',
	'argv_emulation': True
}

setup(
	app=APP,
	name="Name of app",
	options={'py2app': OPTIONS},
	setup_requires=['py2app']
)

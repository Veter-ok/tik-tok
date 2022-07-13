from setuptools import setup

APP = ['desktopApp.py'] # Имя файла
OPTIONS = {
	'iconfile': 'icon.icns', # Путь к файлу
	'argv_emulation': True
}

setup(
	app=APP,
	name="Name of app", # Имя программы
	options={'py2app': OPTIONS},
	setup_requires=['py2app']
)
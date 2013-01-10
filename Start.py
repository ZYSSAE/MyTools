#Python AutoPrepare #0.1 By INUTE Elec. @ 2013

ProjectName = raw_input('Your Project Name: ')

SetupFile = open(ProjectName+"/setup.py","w")

SetupFile.write("""
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)

	""")

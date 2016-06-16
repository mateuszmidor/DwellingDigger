# DwellingDigger
See Gumtree.pl/Olx.pl dwelling offers on a map


Made to work with Python 2.6
Developed using eclipse + PyDev plugin

Test run:
-install pip: sudo apt-get instal pip
-install py.test: sudo pip install -U pytest
-install mock: sudo pip install -U mock
-maybe fix OpenSSL: sudo pip uninstall pyopenssl && sudo pip install mozdownload
-inside ../DwellingDigger/ run: 
	py.test . 

Server install:
-copy the dirtree on FTP
-recursively change persmissions of *.py files to executable
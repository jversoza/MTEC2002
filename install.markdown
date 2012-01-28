---
layout: default
title: MTEC2002 - Programming Foundations for Emerging Technology - OSX 10.6 (Snow Leopard) Installation Instructions 
nav-state: index
---
OSX 10.6 (Snow Leopard) Installation Instructions 
=====
This document contains descriptions and installation instructions of for the libraries and applications required for MTEC2002.  These include:
* git
* TextWrangler
* XCode4
* pip
* virtualenv
* virtualenvwrapper
* MySQL

Note that when the instructions reference "user", that means you should be logged in as the user that will ultimately be using the applicaitons and libraries listed above.

git
=====
##Overview:
git is an open source distributed version control system.

##Rationale:
Using a source code management tool is required for any programming task.  It is necessary for version tracking/back up and collaboration. 

##Install Instructions:
1. Follow the links in http://code.google.com/p/git-osx-installer/ to download the installer
2. Unpack the .dmg and run the .pkg
3. The default options should be sufficient
4. You will need admin rights to install

##Verification Process:
1. If not __user__, log in __as user__
2. Open terminal
3. `which git` # should return location of git binary
4. `git --version` # should print out git version (1.7.x most likely)

TextWrangler
=====
##Overview:
TextWrangler is a free text editor.

##Rationale:
Standardizing on a text editor minimizes the work required for setting up a development environment.  Pre-installed text editors on OSX are either not sufficient (TextEdit does not do syntax highlighting for Python), or may have a steep learning curve (vim, emacs).  TextWrangler is adequate for Python development, and its behavior is similar to more widely used editors.

##Install Instructions:
1. Download the .dmg from http://www.barebones.com/products/textwrangler/
2. __As user__, unpack and copy the .app file Applications

##Verification Process:
1. __As user__, open TextWrangler; verify application starts

XCode4 (Developer Tools)
=====
##Overview:
XCode4 includes Apple's IDE, XCode, and various developer tools, such as gcc.

##Rationale:
Having gcc will allow installation of Python libraries that require compilation (for example, the Python PostgreSQL adapter, needs to be compiled).  Having gcc will allow customized compilation of libraries and applications, making it possible to install these libraries and applications into specific locations.  As a result, administrative access may not be necessary for some future installations, and these future installations would be isolated to the current user.

##Install Instructions:
1. Go to http://developer.apple.com/xcode/
2. Follow the links to the "App Store"
3. Allow App Store to open
4. Install the free app

## Verification Process:
1. If not __user__, log in __as user__
2. In terminal...
3. `/Developer/usr/bin/gcc --version` # should return gcc version number (note that gcc is probably not in path, so used absolute path)


pip
=====
##Overview:
pip is a modern package management system for Python.

##Rationale:
pip will be used to install Python libraries.

##Install Instructions:
1. Open terminal
2. `sudo easy_install pip`

## Verification Process:
1. If not __user__, log in __as user__
2. In terminal...
3. `pip --version` # should return pip version
4. May need to open new terminal for any environment variables to be set appropriately (for example, pip may not be in your path yet)?

virtualenv and virtualenvwrapper
=====
##Overview:
virtualenv and virtualenvwrapper

##Rationale:
These tools will allow users to install Python libraries into "virtual" Python environments.  These will be isolated from the rest of the system and the Python libraries used for these environments will be located in the user's home directory.  Admin rights will not be necessary to manipulate a user's virtualenvs.

##Install Instructions:
1. Open terminal
2. `sudo pip install virtualenv`
3. `sudo pip install virtualenvwrapper`

The following commands can be run by the user, so they are not required.  For the sake of completeness (and convenience for the class)....
1. __As user__ follow the instructions in step "4. Configuring .bashrc to enable virtualenvwrapper commands" of this article: http://blog.praveengollakota.com/47430655

## Verification Process:
1. In terminal...
2. `which mkvirtualenv` 
3. May need to open new terminal for any environment variables to be set appropriately (for example, pip may not be in your path yet)?

MySQL
=====
##Overview:
MySQL is an open source database.

##Rationale:
A database will be necessary during the web development (with Django) portion of this class.

##Install Instructions:
http://dev.mysql.com/downloads/mysql/


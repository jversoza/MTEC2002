---
layout: default
title: MTEC2002 - Programming Foundations for Emerging Technology - Spring 2012 - Installing Modules
---

Modules
=====

Creating Modules
-----
* Modules are just files with Python code
* We created our own modules and used them in previous exercises
* What steps did we need to follow?

Built in Modules
-----
* turtle
* random
* sys

Where do we find the built in modules?
-----
* all of these built in modules are actually somewhere on your computer - for instance, as compiled python, or as packages (collections of modules)
* where does Python look for these packages or modules?
* obv, in the same directory, but... they're not there
* you can see where else Python looks by importing sys and printing out sys.path, the list of directories that Python checks
* let's check out one of those paths ...ls /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk
* now let's try messing with sys.path
* how do I import turtle?
* let's quit
* let's try resetting the path and importing turtle
* no turtle for you!

We know where Python finds modules... we know how to make our own modules... now let's see if we can install modules from the internetz 
=====

Setup
-----
* usually, you need administrative rights to install things python packages and modules
* we installed a tool called virtualenv in the labs; it lets us install packages into a directory in our home folder without needing admin privileges... and also tells python to look there for packages
* echo "source /usr/local/bin/virtualenvwrapper.sh" > ~/.bash_login; source ~/.bash_login; mkvirtualenv mtec2002; echo "workon mtec2002" >> ~/.bash_login

{% highlight bash %}
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/initialize
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/premkvirtualenv
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/postmkvirtualenv
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/prermvirtualenv
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/postrmvirtualenv
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/predeactivate
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/postdeactivate
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/preactivate
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/postactivate
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/get_env_details
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/postmkproject
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/prermproject
virtualenvwrapper.user_scripts creating /Users/professor/.virtualenvs/postrmproject
{% endhighlight %}

For functionality that's not built-in to Python, packages can be installed by using a few different commands - easy_install, pip, etc...
-----
* the lab computers are set up with pip
{% highlight bash %}
pip install some_package_name
{% endhighlight %}

Further reading on modules and installing modules
-----
* http://mirnazim.org/writings/python-ecosystem-introduction/
* http://docs.python.org/tutorial/modules.html
* http://www.virtualenv.org/en/latest/index.html#what-it-does


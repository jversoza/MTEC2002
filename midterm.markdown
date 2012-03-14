---
layout: default
title: MTEC2002 - Programming Foundations for Emerging Technology - Spring 2012 - Midterm Project
---
Midterm Project
===
Due Dates
---
Proposal due by __March 21st__

Project due on __March 28th__

Overview
---
Create a small Python program.  The Python program should be chosen from the list of projects below.  You must submit your proposal project any time between March 14th (class 7) and March 21st (class 8).  The proposal is simply an email containing:

* your name
* the project that you're planning on doing
* a brief description of your project 

The actual project is due on March 28th (class 9).  You must submit your source file(s) using github. 

Project Descriptions
---
__1. Text Adventure__

Do [Exercise 35 in Learn Python the Hard Way](http://learnpythonthehardway.org/book/ex35.html).  __Add at least 3 other rooms to the program__

__2. Rock Paper Scissors__

Create a commandline version of rock-paper scissors.

Example Output:
{% highlight bash %}
Hi, what's your name?
> Bob
Hi Bob, let's play a game of Rock, Paper, Scissors...
Type "r", "p", or "s" to play rock, paper, or scissors respectively
Type "quit" to leave the game

Round 1
============================
Bob: 0, computer: 0

(r)ock, (p)aper, or (s)cissors
> p
Bob played p, computer played r
Player wins

Round 2
============================
Bob: 1, computer: 0

(r)ock, (p)aper, or (s)cissors
> 
{% endhighlight %}

__3. Exploring Python's Built-In Modules__

Python comes with many built-in modules.  Research one of these modules and create a small program that uses it.  Here are some lists of modules:
1. http://docs.python.org/tutorial/stdlib.html
2. http://docs.python.org/modindex.html

For example:
* use the [regular expression library, regex](http://docs.python.org/library/re.html), to enhance the [pluralizer function that we created in class 3](class3/labs/pluralize.py)
* using the [datetime library] (http://docs.python.org/library/datetime.html) write a utility that asks a user for their birthday; it will determine how many weeks it is until that date
* try connecting to and retrieving information from a simple database called [sqlite3](http://docs.python.org/library/sqlite3.html#module-sqlite3)
* use the [turtle library](http://docs.python.org/library/turtle.html) to draw a picture

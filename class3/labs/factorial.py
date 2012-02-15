"""
Factorial
=====

This is a classic recursion problem.  Without looking up the solution, create a function that calculates the factorial of a number.  The factorial of n is the product of all of the positive integers that are less than or equal to n:  

n! = n * (n - 1)! for n > 0
n! = 1 for n = 0

For a more concrete example, see 4 factorial:

4! = 4 * 3 * 2 * 1

Note that 0! = 1

Without using loops, can you come up with a way to calculate factorial?  Hint: you can call the function that you just defined in your function definition!  So... you could do something like:

def foo():
	return foo()

Of course, that would continue going on forever.  You would have to put some guard condition to stop the execution of the program.  The guard condition for factorial is related to the fact that 0! = 1.

Example Output (after importing into Python interactive shell):
>>> from factorial import *
>>> fact(0)
1
>>> fact(1)
1
>>> fact(2)
2
>>> fact(3)
6
>>> fact(4)
24
>>> fact(5)
120

Want to cheat?  See http://www.openbookproject.net/thinkcs/python/english2e/ch11.html, sections 11.8 and 11.9.
"""

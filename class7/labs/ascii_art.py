"""
ascii_art.py
===
Create a program that prints out ascii art based on user input.  Continue to ask the user for input until the user types in "quit".
* Create variables named "tree", "truck" and "heart" that contain the following patterns (note that the backslashes must be "escaped"; having two backslashes in a row is intentional):

    /\\
   /  \\
   /  \\
  /____\\
    ||
      __
 ____|  \_    
|_________|
  O     O
  __  __
 /  \/  \\
  \    /
    \/

* Create a while loop that will loop forever.
* In the while loop...
* Prompt the user for input by asking for a picture to draw; store it in a variable called user_input.
* If the input is "tree", "truck" or "heart", print out the associated image. 
* If the input is "quit", exit the program using the exit() function.
* If the input is none of the above, print out "I don't know how to draw that.".
* As long as the input is not quit, keep prompting the user for more input.
* (INTERMEDIATE) add a command named "help"; it will display all of the commands and pictures that are available (construct the output using the existing variables for you pictures)

Example Output:
What picture should I draw?
> anteater
I don't know how to draw that
What picture should I draw?
> truck

      __
 ____|  \_    
|_________|
  O     O

What picture should I draw?
> quit
Bye!

"""

# this first variable is an example of how you would store an "image" in a variable
tree =  """
    /\\
   /  \\
   /  \\
  /____\\
    ||
"""


"""
animation.py
===
In this exercise, we'll animate a circle so that it moves from the top of the screen to the bottom of the screen...

1. We'll use a dictionary to store the circle's coordinates and velocity.  
2. Since our game loops continuously, if we redraw the circle at a different position after each iteration of the loop, it will look like it's moving.  
3. To do this, we'll draw the circle using the coordinates in the dictionary we created.  
4. At each iteration, we'll also increment that position with the velocity that we have stored in the same dictionary.

To write this code...

1. Copy the template file from the previous exercise - hello_pygame.py.
2. Create a dictionary called c (for circle) above the while loop.
3. This dictionary should have four keys - x, y, velocity_x, and velocity_y (x and y coordinates... and velocity along the x and y axis). Use these default values:
	x: window_dimensions[0] / 2
	y: 0
	vx: 0
	vy: 1
4. Draw a circle after the background color is filled in the while loop.  Use the dictionary, c,  to set the initial coordinates of the circle.
5. Increment your dictionary's value at y by adding the value that's in the key velocity_y.
"""

"""<tt060.py

Now it is time to get our buttons to do something.  We turn our attention to the 
last two (or our original four) basic GUI tasks -- writing event handler 
routines to do the actual work of our program, and binding the event handler 
routines to widgets and events.

Note that in this program we have abandoned all the buttons that we created in 
our last program, and have returned to a simpler situation in which our GUI 
contains only two buttons: "OK" and "Cancel". 

As you will remember from the discussion in our first program, one of the basic 
GUI task is "binding".  "Binding" is the process of defining a connection or 
relationship between (usually):

   * a widget,
   * a type of event, and 
   * an "event handler". 

An "event handler" is a method or subroutine that handles events when they 
occur. [In Java, event handlers are called "listeners".  I like this name, 
because it suggests exactly what they do -- "listen" for events, and respond to 
them.] 

In Tkinter, the way that you create this binding is through the bind() method 
that is a feature of all Tkinter widgets.  You use the bind() method in a 
statement of the form:

	widget.bind(event_type_name, event_handler_name)


This kind of binding is called "event binding".  

[There is another way of binding an event_handler to a widget.  It is called 
"command binding" and we will look at it a couple of programs from now.  But for 
now, let's look at event binding.  Once we understand what event binding is, it 
will make it easier to explain command binding.]

Before we begin, we need to point out a possible point of confusion.  The word 
"button" can be used to refer to two entirely different things: (1) a button 
widget -- a GUI component that is displayed on the computer monitor -- and (2) a 
button on your mouse -- the kind of button that you press with your finger.  In 
order to avoid confusion, I will usually try to distinguish them by referring to 
"button widget" or "mouse button" rather than simply to "button".

(1)
We bind "<Button-1>" events (clicks of the left mouse button) on the button1
widget to the "self.button1Click" method.  When button1 is left-clicked with the mouse,
the self.button1Click() method will be invoked to handle the event.

(3) 
Note that, although they aren't specified on the "bind" operation, self.button1Click()
will be passed two arguments.  The first, of course, will be "self", which is always the first
argument to all class methods in Python.  The second will be an event object.  This technique of binding
and event (that is, using the bind() method) always implicitly passes an event object as
an argument.

In Python/Tkinter, when an event occurs, it takes the form of an event object.  An 
event object is extremely useful, because it carries with it all sorts of useful information
and methods.  You can examine the event object to find out what kind of event occurred, 
the widget where it occurred, and other useful bits of information.

(4)
So, what do we want to happen when button1 is clicked?  Well, in this case we have 
it do something quite simple.  It simply changes its color from green to yellow, and
back again.

(2)
Let's make button2 (the "Goodbye!" button) actually do some useful work.  We will make
it shut down the window.  So we bind a left-mouse click in button2 to the button2Click()
method, and 

(6) 
We have the button2Click() method destroy the root window, the parent window of 
myapp.  This will have a ripple effect, and will destroy all the children and 
descendents of the root.  In short, every part of the GUI will be destroyed.

Of course, to do this, myapp has to know who its parent is.  So (7) we add code 
to its constructor to allow myapp to remember its parent.


PROGRAM BEHAVIOR

When you run this program, you will see two buttons. Clicking on the "OK" button 
will change its color.  Clicking on the "Cancel" button will shut down the 
application.

When our GUI is open, if you hit the TAB key on the keyboard, you will notice 
that the keyboard focus tabs between the two buttons.  But if you hit the 
ENTER/RETURN key on the keyboard, nothing happens.  That is because we have 
bound only mouse clicks, not keyboard events, to our buttons.  Our next task 
will be to bind keyboard events to the buttons, also.

Finally, notice that because the text of one button is shorter than the text of the 
other, the two buttons are of different sizes.  This is rather ugly.  We will 
fix that in a later program.

[revised: 2002-10-01]
>"""

from Tkinter import *
import os
from time import sleep

# Import pySerial : needed to access the Arduino microcontroller
import serial

startup = 1
num = 47
num0 = 0

# Port Name
# To find out the correct port type the line below into the terminal
# python -m serial.tools.list_ports
board = '/dev/cu.usbmodem1421'
# board = '/dev/ttyACM0'

# Baud Rate
# Match baud rate with the rate used in the Arduino sketch and the Max patch
baud = 9600

# Define the connected port
arduino = serial.Serial(board, baud, timeout=1)

class MyApp:
	def __init__(self, parent):

		self.myParent = parent  ### (7) remember my parent, the root
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="OK", background= "green")
		self.button1.pack(side=LEFT)	
		self.button1.bind("<Button-1>", self.button1Click) ### (1)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Cancel", background="red")   
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Button-1>", self.button2Click) ### (2)

	def button1Click(self, event):    ### (3)

		# When the button is clicked (down motion, not button release) 
		# the number '1' will be sent to the Arduino via the serial port
		arduino.write('1')	

		# Create a delay between the write and read operation to avoid
		# clogging the Arduino port
		sleep(0.1)		

		# Receive the response from the Arduino which was initiated via
		# the button click. The output is printed to the console for debugging
		output = arduino.readline()
		print output

		# Each button press should send back it's own unique number
		# This is needed so you can differentiate between specific clicks
		if output == '49':
			print 'ok - pressed'
	
	def button2Click(self, event):  ### (5)
		
		# When the button is clicked (down motion, not button release) 
		# the number '1' will be sent to the Arduino via the serial port
		arduino.write('2')	

		# Create a delay between the write and read operation to avoid
		# clogging the Arduino port
		sleep(0.1)

		# Receive the response from the Arduino which was initiated via
		# the button click. The output is printed to the console for debugging
		output = arduino.readline()
		print output

		# Each button press should send back it's own unique number
		# This is needed so you can differentiate between specific clicks		
		if output == '50':
			print 'cancel - pressed'	

# run Tk application
root = Tk()
myapp = MyApp(root)
root.mainloop()
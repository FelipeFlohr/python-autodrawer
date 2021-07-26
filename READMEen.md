# Python Autodrawer for Paint 3D

 A script designed for autodrawing pictures in Paint 3D. Right now the program is entirely written in Brazilian Portuguese, although you can easily use it without any knowledge about Portuguese. Check out the introduction for the script.

## 1. Requirements

- [Windows 10+](https://www.microsoft.com/software-download/windows10)
- [Paint 3D](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?source=lp&activetab=pivot:overviewtab)
- [Python 3.8+](https://www.python.org/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Keyboard](https://pypi.org/project/keyboard/)
- [Pillow](https://pypi.org/project/Pillow/)

## 2. How to use it

:warning:  **IT IS VERY IMPORTANT FOR YOU TO READ THIS PART** :warning:

### 2.1 The first step

 The first step is to run the script and then close. Once you did it, a file called **config.ini** will be on the root folder of the script, open it. Now we are going to see the parameters to change inside the file.

### 2.2 The "config.ini" file

The **config.ini** is the file for changing the parameters. Let's take a look on what we can change here :arrow_heading_down:

1.  `photo`  The file you want to draw on Paint 3D. images/photo.png by default. Must be inside the _images_ folder by default.

2. `monitor_x`  The X size of your resolution. If you don't know the X size of your resolution, you can run the get_resolution.py inside the _tools_ folder to get it. 1920 by default. Must be an integer.

3. `monitor_y`  The Y size of your resolution. If you don't know the Y size of your resolution, you can run the get_resolution.py inside the _tools_ folder to get it. 1080 by default. Must be an integer.

4.  `canvas_topleftx`  The X position of the top left corner of your canvas. 434 by default. Must be an integer. We will cover about "canvas" later.

5.  `canvas_toplefty`  The Y position of the top left corner of your canvas. 315 by default. Must be an integer. We will cover about "canvas" later.

6.  `canvas_bottomrightx`  The X position of the Bottom Right Corner of your canvas. 1273 by default. Must be an integer. We will cover about "canvas" later.

7.  `canvas_bottomrighty`  The Y position of the Bottom Right Corner of your canvas. 862 by default. Must be an integer. We will cover about "canvas" later.

8.  `canvas_zoom`  Paint 3D's zoom value. 33 by default. Must be an integer. We will cover about "canvas" later.

9. `canvas_zoompos`  A tuple with two values. The first one is the X position of the zoom selector on the screen. The second one is the Y value of the zoom selector on the screen. (1576, 102) by default. Must be a tuple.

9.  `keyboard_interruptionKey`  The keyboard key to interrupt the program. 'space' by default. Must be a key compatible with [PyAutoGUI's keys](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys).

10.  `colorSelector_rpos`  A tuple with two values. The first one is the X position of the R value in the color picker. The second one is the Y position of the R value in the color selector. (1145, 493) by default. Must be a tuple.

11.  `colorSelector_gpos`  A tuple with two values. The first one is the X position of the G value in the color picker. The second one is the Y position of the G value in the color selector. (1145, 550) by default. Must be a tuple.

12.  `colorSelector_bpos`  A tuple with two values. The first one is the X position of the B value in the color picker. The second one is the Y position of the B value in the color selector. (1145, 606) by default. Must be a tuple.

13.  `colorSelector_okbutton`  A tuple with two values. The first one is the X position of the OK button in the color picker. The second one is the Y position of the OK button in the color selector. (851, 728) by default. Must be a tuple.

14.  `colorPalette_colorpos`  A tuple with two values. The first one is the X position of the color to be changed in the color palette. The second one is the Y position of the color to be changed in the color palette. (1695, 997) by default. Must be a tuple.

15.  `draw_tool`  The tool you want to use. The available tools are: "pencil, crayon, pixelpen". 'pencil' by default.

16.  `draw_thickness`  The thickness of the tool. 6 by default. Must be an integer > 0.

17. `draw_opacity`  The opacity of the tool. 60 by default. Must be an integer > 0 and < 101.

19.  `draw_thicknesspos`  A tuple with two values. The first one is the X position of the thickness selector on the screen. The second one is the Y position of the thickness selector on the screen. (1866, 285) by default. Must be a tuple.

20.  `draw_opacitypos`  A tuple with two values. The first one is the X position of the opacity selector on the screen. The second one is the Y position of the opacity selector on the screen. (1863, 365) by default. Must be a tuple.

21.  `delay`  The delay value of drawing pixels on the canvas. :warning: **WARNING** :warning:: Lower values might crash/glitch Paint 3D. If you are experiencing glitches even with the default value, please INCREASE the value. 0.01 by default. Must be a float.

### 2.2.1 Understanding the parameters with Paint 3D

Take a look on the screenshot below.

![](README/example4.png)

Notice that each number represents a topic above with the respective positions. Also, take a look on the 14th topic (the `colorPalette_colorpos` parameter): if it is your first time using Paint 3D and/or you haven't created a custom color yet, just press the add button and create a custom color (it can be any color, just create). Now, take a look on the screenshot below.

![](README/example5.png)

If you right click on your custom color and click on _edit_, this color editor will open. And again: each number is related to a topic above. To get the screen positions, the next topic will cover this.

### 2.2.2 Getting the screen positions

As you may see, the X and Y position of the values inside the _config.ini_ file are designed specifically for my resolution (1920x1080, Full HD), so if you have a different resolution, you'll need to change some values. To get the screen coordinates, there's a script inside the _tools_ folder called *get_x_y.py* that will help you. So, run it (I would recommend open it with Command Prompt) and press Control (can be both left or right) to get the current XY cursor position. Check out the screenshot below.

![](README/example1.png)

Notice that the X and Y position in the prompt are both 0, that's because my cursor was at the top left edge (anyways, the cursor wasn't captured in the screenshot). Obviously, if you change the cursor's position, the coordinates will change too.

### 2.3  Understanding "canvas" | PT-BR: Entendendo o "canvas"

Canvas is the drawable area that the script will be using for the drawing. Take a look at the screenshot below.

![](README/example2.png)

I loaded up a simple image: an A4 paper flipped horizontally with a black border in a black background. The point is: I just want the script to draw within the borders, so, how do I do this? It's easy: just take the top left corner and bottom right corner XY position and set it up on the `canvas_topleftx`, `canvas_toplefty`, `canvas_bottomrightx`, `canvas_bottomrighty` parameters inside the _config.ini_ file. If you want to check the drawable area you have, just run the *draw_drawingarea.py* script that it will automatically draw the borders for you. Check the example below.

![](README/example3.png)

Once I runned the *draw_drawingarea.py* script, a red border was drawn representing the drawable area I have. The program will only be able to draw within this area. Also, the drawing will be in the center of the canvas. Also, notice that the image is 4000x2250px and my zoom is set to 33% because it is the better choice for me. Obviously, if you have a different image and/or a different resolution, you'll need to change the parameters inside _config.ini_.

## 3.  Running the script | PT-BR: Rodando o script

Once you set every parameter and coordinate on _config.ini_ and the main file (if your resolution is not 1920x1080), just run the script and change to the Paint 3D as your active window. The script will run without any problems if you followed every step above. You can see the script running on the video below.

[![Video](README/thumbnail.png)](https://www.youtube.com/watch?v=mbPgQSFNbo4 "Video")

If you followed the steps above, probably you'll not find any problems, but, if you find, it is probably related to the screen coordinates, so be aware that you may need to change it inside *config.ini* and the main file.

## 4. FAQ

Q: Paint 3D is crashing/slowing down/glitching, how do I solve?

- A:  As written in the _config.ini_, this is probably related to the `delay` parameter. You may need to increase the value to stop slowing down Paint 3D.

Q:  Can you briefly explain how this script works?

- A:  This script works by iterating with each pixel on your desirable picture, then, putting the R/G/B/A values inside a list. With this list, the script will automatically use the keyboard and cursor (like a Macro) to work with Paint 3D and automatically draw on the canvas.

Q:  What are the default values designed for?

- A:  The default values are designed for a 1920x1080 monitor, running on a 4000x2250px canvas. So, if you want to quickly use the script, just change the `photo` parameter inside *config.ini* and set the canvas to 4000x2250px on Paint 3D.

Q:  There's a bug I want to report, how can I reach you?

- A:  You can open a discussion here in this repository or reach me on my email: *felipeflohrlol@gmail.com*. Feel free to call me there.

Q:  Why did you made this? This is useless. | **PT-BR**: Por que você fez isso? Isso é inútil.

- A:  The reason I made this script was because my art teacher was sending a lot of homework to do (seriously, a lot), and since I'm having online classes I thought of doing this script as a way to help me doing the homework.

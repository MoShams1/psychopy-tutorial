"""
Mo Shams <m.shams.ahmar@gmail.com
Nov 2023

Objectives:
    1- Load package
    2- Set up monitor and window
    3- Create visual objects
    4- Draw visual objects and flip frames
"""

from psychopy import monitors, visual

# -----------------------------------------------------------------------------
# /// Print variables and arrays

my_number = 2023

print('My variable is:')
print(my_number)

print(f'My variable is: {my_number}')

my_string = 'November'
print(my_string)

print(f'Date: {my_string}, {my_number}')

# -----------------------------------------------------------------------------
# /// Set up monitor and window

my_monitor = monitors.Monitor(name='primary',
                              width=28.6,
                              distance=57)
my_monitor.setSizePix([1440, 900])

my_window = visual.Window(monitor=my_monitor,
                          units='deg',
                          size=[1440, 600],
                          pos=[0, 0],
                          color='gray',
                          fullscr=False)

# -----------------------------------------------------------------------------
# /// Create visual items

my_disc = visual.Circle(win=my_window,
                        radius=1,
                        fillColor='black',
                        pos=[0, 0])

my_block = visual.Rect(win=my_window,
                       width=1,
                       height=1,
                       fillColor='blue',
                       pos=[0, -3],
                       ori=0)

my_text = visual.TextStim(win=my_window,
                          text='Autumn',
                          pos=[0, 3],
                          color='goldenrod',
                          height=.5,
                          ori=-45)

my_image_src = 'ring_noise.png'
my_image = visual.ImageStim(win=my_window,
                            image=my_image_src,
                            size=5,
                            pos=[-5, 0])

# -----------------------------------------------------------------------------
# /// Run stimulus

for iframe in range(300):
    my_disc.draw()
    my_block.draw()
    my_text.draw()
    my_image.draw()

    my_window.flip()

# -----------------------------------------------------------------------------

my_window.close()

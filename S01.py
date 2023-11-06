from psychopy import monitors, visual

# -----------------------------------------------------------------------------
# /// Set up monitor and window

monitor = monitors.Monitor('prim',
                           width=28.6,
                           distance=57)
monitor.setSizePix([1440, 900])

win = visual.Window(monitor=monitor,
                    units='deg',
                    size=[1440, 450],
                    pos=[0, 0],
                    color='gray')

# -----------------------------------------------------------------------------
# /// Create visual items

my_disc = visual.Circle(win,
                        radius=1,
                        fillColor='black',
                        pos=[0, 1])

my_block = visual.Rect(win,
                       size=[1, 1],
                       fillColor='blue',
                       pos=[0, -2])

# -----------------------------------------------------------------------------
# /// Run stimulus

for iframe in range(60):
    my_disc.draw()
    my_block.draw()
    win.flip()

# -----------------------------------------------------------------------------

win.close()

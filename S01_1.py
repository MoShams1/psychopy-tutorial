from psychopy import monitors, visual

# ----------------------------------------------------
# /// Setup monitor and window

my_monitor = monitors.Monitor(name='primary_monitor',
                              width=28.6,
                              distance=57)

my_window = visual.Window(monitor=my_monitor,
                          size=[600, 300],
                          color=[0, 0, 0],
                          units='deg')
# ----------------------------------------------------
# /// Run stimulus

for i in range(120):
    my_window.flip()

# ----------------------------------------------------
# Terminate
my_window.close()


from psychopy import monitors, visual

monitor = monitors.Monitor('prim',
                           width=28.6,
                           distance=57)
monitor.setSizePix([1440, 900])

win = visual.Window(monitor=monitor,
                    units='deg',
                    size=[1440, 450],
                    pos=[0, 0],
                    color='gray')

my_circle = visual.Circle(win,
                          radius=2,
                          fillColor='black',
                          pos=[0, 0])

for iframe in range(60):
    my_circle.draw()
    win.flip()

win.close()

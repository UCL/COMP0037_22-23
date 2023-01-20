from .graphics import *
from .graphics import _root

import pyscreenshot as ImageGrab

class GridDrawer(object):

    def __init__(self, grid, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels = None):
        
        self._grid = grid
        width = grid.width()
        height = grid.height()

        # Make sure that the height of the window is less than the specified maximum
        self._cell_size = max(10, maximum_grid_drawer_window_height_in_pixels / height)

        # Create the window
        pixel_width =  width * self._cell_size
        pixel_height = height * self._cell_size
        
        self._win = GraphWin(grid.name(), pixel_width, pixel_height, autoflush = False)
        
        # If the x and y coordinates are specified, then set the geometry; this is a bit of a hack
        if top_left_in_pixels is not None:
            self._win.master.geometry('%dx%d+%d+%d' % (pixel_width, pixel_height, \
                                                       top_left_in_pixels[0], top_left_in_pixels[1]))
        
        # Allocate the cells
        self._rectangles = [[Rectangle(Point(i * self._cell_size, (height - j - 1) * self._cell_size), \
                                      Point((i+1) * self._cell_size, (height - j) * self._cell_size)) \
                            for i in range(width)] \
                           for j in range(height)]

        for i in range(width):
            for j in range(height):
                self._rectangles[j][i].draw(self._win)

    def reset(self):
        pass
    
    # Save the window
    def save_screenshot(self, filename):
        # From https://stackoverflow.com/questions/66672786
        x=self._win.winfo_rootx()
        y=self._win.winfo_rooty()
        x1=x+self._win.winfo_width()
        y1=y+self._win.winfo_height()
        screenshot_rgba = ImageGrab.grab().crop((x,y,x1,y1))
        screenshot_rgb = screenshot_rgba.convert("RGB")
        screenshot_rgb.save(filename)
               
    def update(self):
        raise NotImplementedError()
    
    def wait_for_key_press(self):
        self._win.getKey()

import pygame
#from cfd import cfd
from environment import Environment

################
# Main Program #
################

env = Environment(500, 500)
#runcfd = cfd(,env)

while(True):
    # Wait for shape to be drawn
    #-------------------------
    env.checkExited()

    # Draw Shape
    env.addContour()

    #if(runCFDclicked):
    # Perform CFD
    #------------
    #TODO
    #cfd.performCFD(winddirection, env.contours)

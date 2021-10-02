import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#As we know, a Cube has 8 vertices and 12 edges
"""All we have to do, is define the basic structure of an 
object and feed it to OpenGL, which will create the appropriate 
3D Model for it
"""

#8 Vertices. Each vertex is a tuple
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

#Each node has 3 edges in a cube
#12 edges. Each tuple is an edge.
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

#6 Faces in a Cube
faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    )

colors = (
    (255, 0, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 255, 255),
    (255, 255, 0),
    )
def Cube():
    glBegin(GL_QUADS)
    x = 0
    for face in faces:
        glColor3fv(colors[x]) #Setting up the color
        x += 1
        x %= len(colors)
        for vertex in face:
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES) #Since our 3d Model is just a bunch of lines
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) #First : Field of view, Second : Aspect Ratio : width/height(Both have already been set in the display),
    # 3rd : Clipping Plane, #4th : A large number

    glTranslatef(0.0,0.0,-5) #If this was 0,0,0 then we would be fully zoomed in to the cube.This function is zooming out in the z axis by 5 units

    glRotatef(0,0,0,0) #Angle of rotation, x,y,z coordinates of a vector

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(2, 4, 3, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

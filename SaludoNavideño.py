import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)
)

aristas = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4)
)

def draw_pyramid():
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    for arista in aristas:
        for vertex in arista:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_cylinder():
    glColor3f(0.5, 0.35, 0.05)
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    glRotatef(-90, 1, 0, 0) 
    gluCylinder(quadric, 0.5, 0.5, 2, 32, 32)
    gluDeleteQuadric(quadric)

def render_text(text, position):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, False, (255,0,0))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    glRasterPos2d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def draw_stack_of_pyramids(num_pyramids):
    for i in range(num_pyramids):
        glPushMatrix()
        glTranslatef(0, i * 2, 0) 
        glScalef(3, 3, 3) 
        glRotatef(1, 0, 1, 0)
        draw_pyramid()  
        glPopMatrix()
    glPushMatrix()
    glTranslatef(0, num_pyramids * -1.5, 0)
    draw_cylinder()
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_stack_of_pyramids(3)
        render_text("Feliz Navidad", (-3, -8))
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

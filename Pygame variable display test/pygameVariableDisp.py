#The purpose of this code is to figure out how to render text and images to a display
#resolution agnostic
#Default screen resolution will be 1920 x 1080 internally, but should correctly size to whatever
#the monitor resolution is

#importations
import sys, pygame

clock = pygame.time.Clock()
pygame.init()

#setting internal resolution and the internal screen surface
int_width = 1920
int_height = 1080
int_canvas = pygame.Surface((int_width, int_height))

#setting initial window size, can be ignored when drawing full screen
window_width = 640
window_height = 480
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

#Can put whatever else is needed for the program

#initialize variables
running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.quit()
            running = False
        elif event.type == pygame.VIDEORESIZE:
            #exclusively for windowed applications, can safely be ignored
            window_width, window_height = event.w, event.h
            screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE | pygame.SCALED)
        
        #Drawing stuff starts here
        #blank canvas
        int_canvas.fill((0, 128, 128))

        #Draw the internal canvas, drawn in relation to the internal screen not the actual screen
        pygame.draw.rect(int_canvas, (255, 100, 100), (100, 100, 200, 150))

        #resolution scaling
        scaled_surface = pygame.transform.scale(int_canvas, (window_width, window_height))

        screen.blit(scaled_surface, (0,0))

        pygame.display.flip()
        clock.tick(60)




import math
import time
import random
import pygame
pygame.init()

WIDTH, HEIGHT = 1542, 800

WIN= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Personalized Aim Trainer")

TARGET_INCREMENT=1000
TARGET_EVENT=pygame.USEREVENT

TARGET_PADDING=30
BG_COLOR=(0, 50, 60)
Lives=3
Top_bar_height=50

Label_Font=pygame.font.SysFont("Comicsans",24)



class Target:
    Max_Size = 20
    Growth_Rate = 0.2
    Color = (173, 216, 230)  # Light blue color for circles
    Second_Color = (240, 248, 255)  # Slightly different light color

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        self.spawn_time = pygame.time.get_ticks()  # Record spawn time

    def update(self):
        if self.size + self.Growth_Rate >= self.Max_Size:
            self.grow = False
        if self.grow:
            self.size += self.Growth_Rate
        else:
            self.size -= self.Growth_Rate

    def draw(self, win):
        # Light blue circle layers
        pygame.draw.circle(win, self.Color, (self.x, self.y), int(self.size))
        pygame.draw.circle(win, self.Second_Color, (self.x, self.y), int(self.size * 0.8))
        pygame.draw.circle(win, self.Color, (self.x, self.y), int(self.size * 0.6))
        pygame.draw.circle(win, self.Second_Color, (self.x, self.y), int(self.size * 0.4))

       
    def collide(self,x,y):
        dis=math.sqrt((self.x-x)**2+(self.y-y)**2) 
        return dis<= self.size
    
def draw(win,targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)

    


def format_time(secs):
    milli=math.floor(int(secs*1000%1000)/100)
    seconds=int(round(secs%60,1))
    minutes=int(secs//60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_top_bar(win, elapsed_time,target_pressed, misses):
    pygame.draw.rect(win,"gray", (0,0, WIDTH, Top_bar_height))
    time_label=Label_Font.render(f"Time: {format_time(elapsed_time)}",1,"black")
    
    speed= round(target_pressed/ elapsed_time,1)
    speed_label=Label_Font.render(f"Speed:{speed} t/s",1,"black")

    hits_label=Label_Font.render(f"Hits:{target_pressed} ",1,"black")
    
    lives_label=Label_Font.render(f"Lives:{Lives-misses} ",1,"black")

    win.blit(time_label,(5,5))
    win.blit(speed_label,(200,5))
    win.blit(hits_label,(450,5))
    win.blit(lives_label,(650,5))

def end_screen(win,elapsed_time, target_pressed, clicks):
    win.fill(BG_COLOR)

    time_label = Label_Font.render(f"Time: {format_time(elapsed_time)}", 1, "white")
    speed = round(target_pressed / elapsed_time, 1)
    speed_label = Label_Font.render(f"Speed: {speed} t/s", 1, "white")
    hits_label = Label_Font.render(f"Hits: {target_pressed} ", 1, "white")
    accuracy = round(target_pressed / clicks * 100, 1)
    accuracy_label = Label_Font.render(f"Accuracy: {accuracy}% ", 1, "white")

    rect_width = 250
    rect_height = 50
    padding = 10  # Optional padding for better spacing between the labels

    # Draw the labels with fixed-size rectangles
    def draw_label_with_fixed_rect(win, label, x, y):
        label_rect = label.get_rect(center=(x + rect_width // 2, y + rect_height // 2))
        pygame.draw.rect(win, (255, 255, 255), (x, y, rect_width, rect_height), 2)  # White border
        win.blit(label, label_rect)  # Draw the label inside the centered rectangle

    # Coordinates for placing the fixed-size rectangles
    x_pos = WIDTH // 2 - rect_width // 2  # Horizontally center the rectangles
    y_pos = [100, 200, 300, 400]  # Vertical positions for time, speed, hits, and accuracy

    # Draw each label within a fixed-size rectangle
    draw_label_with_fixed_rect(win, time_label, x_pos, y_pos[0])
    draw_label_with_fixed_rect(win, speed_label, x_pos, y_pos[1])
    draw_label_with_fixed_rect(win, hits_label, x_pos, y_pos[2])
    draw_label_with_fixed_rect(win, accuracy_label, x_pos, y_pos[3])
    
    
    # Add the motivational message
    motivational_font = pygame.font.SysFont("Impact", 48)
    motivational_text = motivational_font.render("You can do better!", 1, (192,192,192))
    
    win.blit(motivational_text, (get_middle(motivational_text), 500))

    pygame.display.update()

    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN:
                quit()

def get_middle(surface):
    return WIDTH/2-surface.get_width()/2
    

def main():
    run =True
    targets=[]
    clock=pygame.time.Clock()
    target_pressed=0
    clicks=0
    start_time=time.time()
    misses=0

    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)

    while run:
        clock.tick(60)
        click=False
        mouse_pos=pygame.mouse.get_pos()
        elapsed_time= time.time() - start_time
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break

            if event.type==TARGET_EVENT:
                x=random.randint(TARGET_PADDING+Top_bar_height,WIDTH-TARGET_PADDING)
                y=random.randint(TARGET_PADDING+Top_bar_height,HEIGHT-TARGET_PADDING)
                target=Target(x,y)
                targets.append(target)

            if event.type==pygame.MOUSEBUTTONDOWN:
                click=True
                clicks+=1
        
        for target in targets:
            target.update()

            if target.size<=0:
                targets.remove(target)
                misses+=1


            if click and target.collide(*mouse_pos):
                targets.remove(target)
                target_pressed+=1

        if misses>=Lives:
            end_screen(WIN,elapsed_time,target_pressed,clicks)


        draw(WIN,targets)
        draw_top_bar(WIN,elapsed_time, target_pressed, misses)


        pygame.display.update()

    pygame.quit()

if __name__=="__main__":
    main()
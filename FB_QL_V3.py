import pygame
import time
import os
import random
import datetime
import sys
import matplotlib.pyplot as plt
from matplotlib import style

from FB_QL_Bot import Bot

bot = Bot()

pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800
SCORES = []
EPISODE = 10000
MAX_SCORE = 25

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

def getNextUpdateTime():
    return datetime.datetime.now() + datetime.timedelta(minutes=5)


NEXT_UPDATE_TIME = getNextUpdateTime()

'''This class creates the bird object and the move functions for the bird'''
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    '''x, y are the starting coordinates of the bird'''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    '''The Bird moves in a vertical manner, each time the jump function is called, the bird "jumps" up a certain velocity'''

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    '''If the jump is not called, then the bird will start to fall towards the ground'''

    def move(self):
        self.tick_count += 1
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    '''Function that draws what is happening to the bird'''

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


'''Creates the pipe structure of the game'''


class Pipe:
    GAP = 275  # Gap between the pipes, can be larger or smaller

    '''The x refers to the x-coordinate, we don't need the y-coordinate for the pipes as they are constant'''

    def __init__(self, x, vel):
        self.x = x
        self.vel = vel
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    '''Randomly set the height of the pipes with the gap in between'''

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    '''The pipes move to the left based on the velocity'''

    def move(self):
        self.x -= self.vel

    '''Draw the pipes moving'''

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    '''Set the action for bird/pipe collision'''

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - int(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - int(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        else:
            return False


'''Creates a scrolling ground to show movement'''


class Base:
    WIDTH = BASE_IMG.get_width()  # Set the width to the screen width
    IMG = BASE_IMG

    def __init__(self, y, vel):
        self.y = y
        self.vel = vel
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


'''Draw the full window with all actions represented'''


def draw_window(win, birds, pipes, base, score):
    win.blit(BG_IMG, (0, 0))
    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    base.draw(win)

    '''Draw the birds that are currently in the game'''
    # for bird in birds:
    # bird.draw(win)
    birds.draw(win)
    pygame.display.update()


'''The main functionality of the game'''


def mainGame():
    vel = 8
    bird = Bird(200, 200)
    base = Base(730, vel)
    pipes = [Pipe(700, vel)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    run = True
    add_pipe = False

    while run:
        clock.tick(3000)

        if bot.act(bird.x, bird.y, bird.vel, pipes[0]) == 1:
            bird.jump()

        rem = []
        '''Moves the pipes, generates more and checks for collisions'''
        for pipe in pipes:
            if pipe.collide(bird):
                #print(score)
                bot.update_scores()
                updateQtable(score)
                return True

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            # Uncomment if you want to add in speed ups
            # if score % 5 == 0:
            #    vel += 2
            #    base = Base(730, vel)
            pipes.append(Pipe(WIN_WIDTH, vel))
            add_pipe = False

        for r in rem:
            pipes.remove(r)

        if bird.y + bird.img.get_height() > 730 or bird.y + bird.img.get_height() < 0:
            #print(score)
            bot.update_scores()
            updateQtable(score)
            return True

        if score > MAX_SCORE:
            return False

        bird.move()
        base.move()
        #draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()

def updateQtable(score):
    global NEXT_UPDATE_TIME

    print("Game " + str(bot.gameCNT) + ": " + str(score))

    justUpdate = False
    if score > 5 or datetime.datetime.now() > NEXT_UPDATE_TIME:
        bot.dump_qvalues(force=True)
        justUpdate = True
        NEXT_UPDATE_TIME = getNextUpdateTime()

    if score > max(SCORES, default=0) and score > 100_000:
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$ NEW RECORD: %d $$$$$$$$" % score)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

    SCORES.append(score)

    if bot.gameCNT >= EPISODE:
        if not justUpdate: bot.dump_qvalues(force=True)
        showPerformance()
        pygame.quit()
        sys.exit()

# from matplotlib.ticker import MaxNLocator
def showPerformance():
    average = []
    num = 0
    sum_s = 0

    for s in SCORES:
        num += 1
        sum_s += s
        average.append(sum_s / num)

    print("\nEpisode: {}, highest score: {}, average: {}".format(num, max(SCORES), average[-1]))
    plt.figure(1)
    # plt.gca().get_xaxis().set_major_formatter(MaxNLocator(integer=True))
    plt.scatter(range(1, num + 1), SCORES, c="green", s=3)
    plt.plot(range(1, num + 1), average, 'b')
    plt.xlim((1, num))
    plt.ylim((0, int(max(SCORES) * 1.1)))

    plt.title("Score distribution")
    plt.xlabel("Episode")
    plt.ylabel("Score")
    plt.show()

KeepGoing = True
while KeepGoing:
    KeepGoing = mainGame()

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:41:24 2020

@author: art
"""


'''Imports for Flappy Bird'''
import pygame
import time
import os
import random

'''Imports for Q-Learning'''
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style


'''Flappy Bird Code Start'''
'''From tutorials by Tech with Tim'''
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

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

    def action(self, action):
        print('action: ', action)
        if action == 1:
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
    GAP = 250  # Gap between the pipes, can be larger or smaller
    VEL = 8  # the speed the pipes are moving, a constant 10 now but can be scaled based on time in game

    '''The x refers to the x-coordinate, we don't need the y-coordinate for the pipes as they are constant'''

    def __init__(self, x):
        self.x = x
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
        self.x -= self.VEL

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
    VEL = 8  # Again, this is set but must be the same as the pipe velocity
    WIDTH = BASE_IMG.get_width()  # Set the width to the screen width
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

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
class FlappyBirdEnv():
    PIPE_COLLISION_PENALTY = 300
    GROUND_SKY_PENALTY = 500
    PASS_THROUGH_REWARD = 1
    OBSERVATION_SPACE_VALUES = (WIN_WIDTH, WIN_HEIGHT, 3)
    REWARD_THRESHOLD = 100
    RETURN_IMAGES = True
    clock = pygame.time.Clock()
    episode_step = 0
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def reset(self):
        self.bird = Bird(200, 200)
        self.base = Base(730)
        self.pipes = [Pipe(700)]
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.score = 0
        self.run = True
        self.add_pipe = False
        self.episode_step = 0
        self.observation = ((round(self.bird.x / WIN_WIDTH * 100) - round((self.pipes[0].x - 232) / WIN_WIDTH * 100)), (round(self.bird.y / WIN_HEIGHT * 100) - round(self.pipes[0].bottom /WIN_HEIGHT * 100)))

        '''if self.RETURN_IMAGES:
            self.observation = np.array(self.get_image())
        else:
            self.observation = (self.bird.x - self.pipes[0].x)'''
        return self.observation

    def step(self, action):
        self.clock.tick(3000)
        self.episode_step += 1
        self.bird.action(action)

        '''for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()'''
        done = False
        add_pipe = False
        reward = 0
        #while not done:
        rem = []
        '''Moves the pipes, generates more and checks for collisions'''
        for pipe in self.pipes:
            if pipe.collide(self.bird):
                reward = -self.PIPE_COLLISION_PENALTY
                #self.reset()

            if not pipe.passed and pipe.x < self.bird.x:
                pipe.passed = True
                add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            self.score += 1
            reward = self.PASS_THROUGH_REWARD
            self.pipes.append(Pipe(WIN_WIDTH))
            self.add_pipe = False

        for r in rem:
            self.pipes.remove(r)

        if self.bird.y + self.bird.img.get_height() > 730 or self.bird.y + self.bird.img.get_height() < 0:
            reward = -self.GROUND_SKY_PENALTY

        self.bird.move()
        self.base.move()

        done = False
        if reward == self.REWARD_THRESHOLD or reward < 0 or self.episode_step >= 200:
            done = True

        if self.RETURN_IMAGES:
            new_observation = ((round(self.bird.x / WIN_WIDTH * 100) - round((self.pipes[0].x - 232) / WIN_WIDTH * 100)), (round(self.bird.y / WIN_HEIGHT * 100) - round(self.pipes[0].bottom /WIN_HEIGHT * 100)))

        draw_window(self.win, self.bird, self.pipes, self.base, self.score)

        return new_observation, reward, done

'''    def render(self):
        img = self.get_image()
        img = img.resize((300, 300))
        cv2.imshow("image", np.array(img))
        cv2.waitKey(1)
    def get_image(self):
        env = np.zeros((WIN_WIDTH, WIN_HEIGHT, 3), dtype=np.uint8)
        img = Image.fromarray(env, 'RGB')
        return img'''


'''End of Flappy Bird Code'''

SIZE = 110
NUM_EPISODES = 1000
SHOW_EVERY = 50
epsilon = 0.9
EPS_DECAY = 0.9998

start_q_table = None

LEARNING_RATE = 0.1
DISCOUNT = 0.95

episode_rewards = []

if start_q_table is None:
    q_table = {}
    for x_diff in range(-SIZE, SIZE):
            for y_diff in range(-SIZE, SIZE):
                    q_table[(x_diff,y_diff)] = [np.random.uniform(0, 1) for i in range(0,2)]
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

print(start_q_table)
env = FlappyBirdEnv()
for episode in range(NUM_EPISODES):
    print(episode)
    if (episode+1) % SHOW_EVERY == 0:
        print(f"on # {episode}, epsilon: {epsilon}")
        print(f"{SHOW_EVERY} ep mean {np.mean(episode_rewards[-SHOW_EVERY:])}")
        print(q_table)
        show = True
    else:
        show = False

    env.reset()

    episode_reward = 0
    for i in range(1000000):
        if np.random.random() > epsilon:
            action = np.argmax(q_table[env.observation])
        else:
            action = np.random.randint(0, 8)
            if action == 1:
              action = 1
            else:
              action =0

        new_obs, reward, done = env.step(action)
        print(new_obs)
        print(reward)
        max_future_q = np.max(q_table[new_obs])
        current_q = q_table[env.observation][action]

        if reward > 0:
            new_q = 1
        elif reward == -300:
            new_q = -300
        elif reward == -500:
            new_q = -500
        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

        q_table[env.observation][action] = new_q

        episode_reward += reward
        if reward < 0:
            break

    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,)) / SHOW_EVERY, mode="valid")

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"reward {SHOW_EVERY}ma")
plt.xlabel("Episode #")
plt.show()

with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)

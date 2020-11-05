import json
import random

class Bot(object):
    '''
    The Bot class that applies the Qlearning logic to Flappy bird game
    After every iteration (iteration = 1 game that ends with the bird dying) updates Q values
    '''

    def __init__(self, episodes = 10000, discount = 0.9, lr = 0.3):
        self.gameCNT = 0  # Game count of current run, incremented after every death
        self.discount = discount
        self.r = {0: 1, 1: -1000}  # Reward function
        self.lr = lr
        self.load_qvalues()
        self.last_state = "0_0_0"  # initial position, MUST NOT be one of any other possible state
        self.initStateIfNull(self.last_state)
        self.last_action = 0
        self.moves = []
        self.episodes = episodes

    def load_qvalues(self):
        """
        Load q values from a JSON file
        """
        self.qvalues = {}
        try:
            fil = open("q_values.json", "r")
        except IOError:
            return
        self.qvalues = json.load(fil)
        fil.close()

    # save q-values during the game, the bird is still alive, just to reduce the memory consumption
    def save_qvalues(self):
        if len(self.moves) > self.episodes:
            history = list(reversed(self.moves[:95000]))
            for exp in history:
                state, act, new_state = exp
                self.qvalues[state][act] = (1 - self.lr) * self.qvalues[state][act] + \
                                           self.lr * (self.r[0] + self.discount * max(self.qvalues[new_state][0:2]))
            self.moves = self.moves[95000:]

    def act(self, x, y, vel, pipe):
        """
        Chooses the best action with respect to the current state - Chooses 0 (don't flap) to tie-break
        """
        state = self.get_state(x, y, vel, pipe)

        self.moves.append(
            (self.last_state, self.last_action, state)
        )  # Add the experience to the history

        self.save_qvalues()

        if self.qvalues[state][0] >= self.qvalues[state][1]:
            action = 0
        else:
            action = 1

        self.last_state = state  # Update the last_state with the current state
        self.last_action = action
        # print("%s -> %d" % (state, action))
        return action

    def get_state(self, x, y, vel, pipe):
        """
        format:
            x0_y0_v
        (x, y): coordinates of player (top left point)
        x0: diff of x to pipe0, [-50, ...]
        y0: diff of y to pipe0
        v: current velocity
        """
        pipe0 = pipe

        x0 = pipe.x - x
        y0 = pipe.bottom - y

        if x0 < -40:
            x0 = int(x0)
        elif x0 < 140:
            x0 = int(x0) - (int(x0) % 10)
        else:
            x0 = int(x0) - (int(x0) % 70)

        if -180 < y0 < 180:
            y0 = int(y0) - (int(y0) % 10)
        else:
            y0 = int(y0) - (int(y0) % 60)

        state = str(int(x0)) + "_" + str(int(y0)) + "_" + str(int(vel))
        self.initStateIfNull(state)
        return state

    def initStateIfNull(self, state):
        if self.qvalues.get(state) == None:
            self.qvalues[state] = [0, 0]  # [Q of no action, Q of flap action, Num of enter]
            num = len(self.qvalues.keys())
            if num > 20000 and num % 1000 == 0:
                print("======== Total state: {} ========".format(num))
            if num > 30000:
                print("======== New state: {0:14s}, Total: {1} ========".format(state, num))

    def update_scores(self, printLogs=False):
        """
        Update qvalues via iterating over experiences
        """
        history = list(reversed(self.moves))

        # Q-learning score updates
        # Flag if the bird died in the top pipe
        high_death_flag = True if int(history[0][2].split("_")[1]) > 120 else False

        t = 0
        last_flap = True  # penalty for last flap action
        for exp in history:
            t += 1
            state = exp[0]
            act = exp[1]
            new_state = exp[2]
            #print(len(self.qvalues))
            self.qvalues[state][1] += 1

            # Select reward
            if t <= 2:
                cur_reward = self.r[1]
                if act: last_flap = False
            elif (last_flap or high_death_flag) and act:
                cur_reward = self.r[1]
                high_death_flag = False
                last_flap = False
            else:
                cur_reward = self.r[0]

            self.qvalues[state][act] = (1 - self.lr) * self.qvalues[state][act] + \
                                       self.lr * (cur_reward + self.discount * max(self.qvalues[new_state][0:2]))

        printLogs = False
        if printLogs: self.showSteps(self.moves)
        self.gameCNT += 1  # increase game count
        self.moves = []  # clear history after updating strategies

    def dump_qvalues(self, force=False):
        """
        Dump the qvalues to the JSON file
        """
        if force:
            print("******** Saving Q-table(%d keys) to local file... ********" % len(self.qvalues.keys()))
            fil = open("q_values.json", "w")
            json.dump(self.qvalues, fil)
            fil.close()
            print("******** Q-table(%d keys) updated on local file ********" % len(self.qvalues.keys()))
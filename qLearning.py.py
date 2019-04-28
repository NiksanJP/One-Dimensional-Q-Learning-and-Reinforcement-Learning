import numpy as np
import time
import random

random.seed(42)

class env_:
    def __init__(self):
        self.stateSize = 12
        
        self.agent = "O"
        self.agent_Location = 0
        
        self.state = ""
        self.Treasure = "T"
        
    def getCurrentState(self):
        self.state = ""
        for i in range(self.stateSize):
            if i == self.agent_Location+1:
                self.state += "O"
            else:
                self.state += "-"
        self.state += self.Treasure
        currentState = self.state
        return currentState
    
    def getState(self):
        state = self.stateSize - self.agent_Location 
        return state
    
    def environmentReact(self, action):
        R = 0
        if action == "left":
            if self.agent_Location != 0:  
                self.agent_Location -= 1
            R = 0
        else:        
            if action == "right":
                self.agent_Location += 1
                if self.agent_Location == self.stateSize:
                    R = 1
                else:
                    R = 0
        state = self.stateSize - self.agent_Location 
        return R, state
    
    def reset(self):
        self.__init__()

class agent:
    def __init__(self):
        self.learningRate = 0.1
        self.discountRate = 0.9
        self.epsilon = 0.9
        self.actions = ['left', 'right']
        self.size = 12
        self.decay = 0.1
        
        self.table = self.createQTable(self.actions, self.size)
        
    def createQTable(self, actions, size):
        table = np.zeros((self.size + 1, len(actions)))
        return table

    def getTable(self):
        return self.table
    
    def buildTable(self):
        self.table = self.createQTable(self.actions, self.size)
        
    def chooseAction(self, state):
        table = self.getTable()
        state_actions = table[state, :]
        print(state_actions)
        if (np.random.uniform() > self.epsilon) or ((state_actions == 0).all()):
            action = np.random.choice(self.actions)
            print("RANDOM ACTION = ", action)
        else:
            action = np.argmax(self.table[state, :])
            if action == 0:
                action = "left"
            elif action == 1:
                action = "right"
            print("CHOOSEN ACTION = ", action)
        return action
    
    def learn(self, state, action, reward, new_state):
        if action == "left":
            action = 0
        elif action == "right":
            action = 1
        predict = self.table[state, action]
        target = reward + self.epsilon * np.max(self.table[new_state, :])
        self.table[state, action] = self.table[state, action] + self.learningRate*(target - predict)
  
env = env_()
agent1 = agent()

for episode in range(30):
    state = env.getState()
    for steps in range(100):
        interaction = 'Episode %s: total_steps = %s' % (episode+1, steps)
        print('\r{}'.format(interaction), end='')
        print()

        action = agent1.chooseAction(state)
        
        reward, new_state = env.environmentReact(action)
        print("REWARD : ", reward)
        agent1.learn(state, action, reward, new_state)
        
        state = new_state
            
        print(env.getCurrentState())
        
        time.sleep(0.05)
        
        if reward == 1:
            env.reset()
            time.sleep(1)
            print('\r                                ', end='')
            break
        
            
    
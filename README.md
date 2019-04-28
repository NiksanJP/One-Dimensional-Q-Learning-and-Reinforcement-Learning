# One-Dimensional-Q-Learning-and-Reinforcement-Learning
Bellman equation gives a reward for every correct step. The Reinforcement Learning (RL) program I wrote follows this principle of the equation. The board is not small so it might take some to learning.

# Prerequisits
1. numpy  pip install numpy
2. time
3. random

# Maths
Maths is the BEST! Here we go
Bellman Equation
This equation makes use of the Table called Q table which is like a cheat sheet for the agent to choose the next KNOWN move, unkown moves are just made to random moves. In this equation to make it simple we will use 3 parts of predict, target and Q table it self

Here we will get the Predict
predict = table[state, action]

Now get the TARGET
target = reward + epsilon X max(table[new_state, end])
The reward is given by the table and the epsilon is predefined by the author
max(table[new_state, end]) will give the maximum value from the table to end

Here we will update the table
table[state, action] = table[state, action] + learningRate X (target - predict)


# How to run
Open qLearning.py file and run it

# Conclusion
The following program shows great potential in learning but it is like trainging a blind man to drive where it is very hard to train as it requires visuals. Hence using Deep Convolutional Neural Networks that uses visuals will be the easier.

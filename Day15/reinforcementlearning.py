import gymnasium as gym    #type:ignore
import numpy as np

class EmployeeSchedulingEnv(gym.Env):
    def __init__(self):
        self.employees = 4
        self.state = np.zeros(self.employees)
        self.action_space = gym.spaces.Discrete(3)

    def reset(self,seed=None,options=None):
        self.state=np.zeros(self.employees)
        return self.state,{}
    def step(self,action):
        employee = np.random.randint(0,self.employees)
        self.state[employee]+=1
        # reward calculation
        if self.state[employee] <= 8:
            reward=10
        else:
            reward=-10
        done = np.max(self.state)>=10
        return (self.state,reward,done,False,{})

env = EmployeeSchedulingEnv()
state,_=env.reset()
total_reward=0

for episode in range(100):
    action = env.action_space.sample()
    state,reward,done,_,_=env.step(action)
    total_reward += reward
    if done:
        break

print("Final Schedule:")
print(state)

print("Total Reward:",total_reward)
print("\nPerformance Evaluation:")


if total_reward > 50:
    print("Good Scheduling Performance")
else:
    print("Needs Improvement")




###    OUTPUT    ####

# Final Schedule:
# [10.  5.  4.  6.]
# Total Reward: 210

# Performance Evaluation:
# Good Scheduling Performance
import gym
import gym_flock

env_name = "FlockingLeader-v0"
env = gym.make(env_name)

while True:
    state = env.reset()
    episode_reward = 0
    done = False
    while not done:
        action = env.env.controller(False)
        next_state, reward, done, _ = env.step(action)
        episode_reward += reward
        state = next_state
        env.render()

    print(episode_reward)

env.close()
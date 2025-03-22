""" Integrating Ale Environments """

import os
import ale_py
import logging
import os.path as osp
import gymnasium as gym
from gymnasium.wrappers import RecordEpisodeStatistics, RecordVideo

# unnecessary but helpful for IDEs
gym.register_envs(ale_py)  

class AleEnv:
    def __init__(self, env_name="Breakout-v5", record_video=False, render_mode="human",
                log_dir=None, record_stats=False, stage="training"):
        # initiating environment for stage
        self.env = gym.make(f'ALE/{env_name}', render_mode=render_mode) 
        if record_video:
            self.env = RecordVideo(self.env, video_folder=log_dir, name_prefix=stage,
                                    episode_trigger=lambda x: x % training_period == 0)
        if record_stats: self.env = RecordEpisodeStatistics(self.env)

        self._observation_space = self.env.observation_space
        self._action_space = self.env.action_space
        logging.info(f"Initiate environment with observation space: \n{self.env.observation_space}")
        logging.info(f"Initiate environment with action space: \n{self.env.action_space}")

    @property
    def observation_space(self):
        return self._observation_space

    @property
    def action_space(self):
        return self._action_space

    def reset(self):
        obs, info = self.env.reset()
        return obs, info 

    def step(self, action):
        next_obs, reward, done, truncated, info = self.env.step(action)
        episode_over = done or truncated
        return {"S'": next_obs, "R": reward, "OVER:" episode_over, "Info": info}

    def render(self, mode='human', close=False):
        return self.env._render(mode, close)
        # self.env.render()

    def terminate(self):
        self.env.close()
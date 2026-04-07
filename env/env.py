import random
from typing import Tuple, Dict, Any
from env.models import Observation, Reward


class GigShieldEnv:
    def __init__(self, target_earnings: int = 500, max_steps: int = 10):
        self.target = target_earnings
        self.max_steps = max_steps
        self.current_step = 0
        self.state_data = None

    def reset(self) -> Dict[str, Any]:
        self.current_step = 0
        self.state_data = {
            "weather": random.choice(["clear", "rainy"]),
            "demand": round(random.uniform(0.3, 1.0), 2),
            "distance": random.randint(1, 10),
            "earnings_today": 0,
            "fatigue": 0.0
        }
        return Observation(**self.state_data)

    def step(self, action: str) -> Tuple[Dict[str, Any], float, bool, Dict]:

        self.current_step += 1
        reward = 0.0
        done = False
        error = None

        weather = self.state_data["weather"]
        demand = self.state_data["demand"]

        # --- ACTION LOGIC ---
        if action == "accept_job":

            if weather == "clear":
                base_earning = 100
                reward += 1.0
            else:
                base_earning = 60
                reward -= 0.4

            bonus = base_earning * demand
            total_earning = int(base_earning + bonus)

            self.state_data["earnings_today"] += total_earning

        elif action == "reject_job":
            if weather == "rainy":
                reward += 0.5
            else:
                reward -= 0.2

        elif action == "wait":
            reward -= 0.3

        else:
            error = "invalid_action"
            reward -= 1.0

        # --- ADVANCED REWARD SHAPING (CRITICAL FIX) ---
        if demand > 0.8:
            reward += 0.3  # high demand bonus

        self.state_data["fatigue"] += 0.1

        if self.state_data["fatigue"] > 0.7:
            reward -= 0.2  # fatigue penalty

        if self.state_data["fatigue"] > 1:
            reward -= 0.5  # burnout penalty

        # --- ENV UPDATE ---
        self.state_data["weather"] = random.choice(["clear", "rainy"])
        self.state_data["demand"] = round(random.uniform(0.3, 1.0), 2)

        # --- DONE CONDITIONS ---
        if self.state_data["earnings_today"] >= self.target:
            done = True
            reward += 1.0

        if self.current_step >= self.max_steps:
            done = True

        # --- USE REWARD MODEL (CRITICAL FIX) ---
        reward_obj = Reward(
            value=round(reward, 2),
            done=done,
            info={"error": error}
        )

        return Observation(**self.state_data), reward_obj.value, reward_obj.done, reward_obj.info

    def state(self) -> Dict[str, Any]:
        return Observation(**self.state_data)
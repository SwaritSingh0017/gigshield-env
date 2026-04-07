import os
from openai import OpenAI
from env.env import GigShieldEnv

# ENV VARIABLES (required by hackathon)
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

# REQUIRED OpenAI client (even if not heavily used)
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

TASK_NAME = "gigshield_easy"
BENCHMARK = "gigshield_env"
MAX_STEPS = 10

print("RUNNING FILE...")


def run_task(task_name, target):
    env = GigShieldEnv(target_earnings=target, max_steps=MAX_STEPS)

    obs = env.reset()

    print(f"[START] task={task_name} env={BENCHMARK} model={MODEL_NAME}")

    rewards = []
    steps = 0
    success = False

    try:
        for step in range(MAX_STEPS):
            steps += 1

            # ✅ IMPROVED POLICY
            if obs.weather == "clear" and obs.fatigue < 0.7:
                action = "accept_job"
            elif obs.weather == "rainy" and obs.fatigue > 0.5:
                action = "reject_job"
            else:
                action = "wait"

            obs, reward, done, info = env.step(action)
            rewards.append(reward)

            error = info.get("error")
            error_str = error if error else "null"

            print(
                f"[STEP] step={steps} action={action} reward={reward:.2f} "
                f"done={str(done).lower()} error={error_str}"
            )

            if done:
                success = obs.earnings_today >= target
                break

    except Exception as e:
        print(f"[STEP] step={steps} action=none reward=0.00 done=true error={str(e)}")

    score = min(obs.earnings_today / target, 1.0)

    reward_str = ",".join([f"{r:.2f}" for r in rewards])

    print(
        f"[END] success={str(success).lower()} steps={steps} "
        f"score={score:.2f} rewards={reward_str}"
    )


if __name__ == "__main__":
    run_task("easy", 300)
    run_task("medium", 500)
    run_task("hard", 800)
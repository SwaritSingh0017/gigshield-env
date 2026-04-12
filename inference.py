import os
from openai import OpenAI
from env.env import GigShieldEnv

# ENV VARIABLES (required by hackathon)
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("API_KEY")
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

TASK_NAME = "gigshield_easy"
BENCHMARK = "gigshield_env"
MAX_STEPS = 10

print("RUNNING FILE...")


def get_action_from_llm(obs):
    try:
        prompt = f"""
You are a gig worker decision agent.

Current state:
Weather: {obs.weather}
Demand: {obs.demand}
Fatigue: {obs.fatigue}

Choose ONE action ONLY:
accept_job OR reject_job OR wait

Return ONLY the action.
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        action = response.choices[0].message.content.strip().lower()

        if action not in ["accept_job", "reject_job", "wait"]:
            return "wait"

        return action

    except Exception:
        # 🔥 FAIL-SAFE (VERY IMPORTANT FOR JUDGES)
        return "wait"


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

            # ✅ LLM DECISION
            action = get_action_from_llm(obs)

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
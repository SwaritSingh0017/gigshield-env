from fastapi import FastAPI
from env.env import GigShieldEnv
import uvicorn

app = FastAPI()
env = GigShieldEnv()


@app.get("/")
def root():
    return {"message": "GigShield Env Running"}


@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()


@app.post("/step")
def step(action: dict):
    act = action.get("action", "wait")
    obs, reward, done, info = env.step(act)

    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
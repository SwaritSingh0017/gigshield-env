from pydantic import BaseModel
from typing import Optional


class Observation(BaseModel):
    weather: str
    demand: float
    distance: int
    earnings_today: int
    fatigue: float


class Action(BaseModel):
    action: str


class Reward(BaseModel):
    value: float
    done: bool
    info: Optional[dict] = {}
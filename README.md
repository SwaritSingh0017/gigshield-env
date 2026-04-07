---
title: GigShield Env
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: server/app.py
pinned: false
---

# 🚀 GigShield: AI Environment for Gig Worker Decision Intelligence

> "No claims. No delays. Just smarter decisions."

GigShield is a real-world reinforcement learning environment that simulates how gig workers (delivery riders, drivers) make decisions under uncertainty — balancing income, risk, and fatigue.

---

## 🌍 Why This Matters

Gig workers face daily uncertainty:
- Weather disruptions 🌧️  
- Fluctuating demand 📉  
- Physical fatigue ⚡  
- Income instability 💸  

This environment enables AI agents to learn optimal decision-making strategies in such dynamic conditions.

---

## 🧠 Core Idea

An AI agent acts as a gig worker and must decide:
- Accept a job  
- Reject a job  
- Wait  

Goal:
Maximize earnings while minimizing risk and burnout.

---

## ⚙️ Environment Design

### 📊 Observation Space

- weather: clear / rainy  
- demand: float (0.3 → 1.0)  
- distance: job distance  
- earnings_today: total earnings  
- fatigue: worker exhaustion  

---

### 🎮 Action Space

- accept_job → take the job  
- reject_job → skip risky job  
- wait → delay decision  

---

## 💰 Reward Design (Key Highlight)

- +1.0 → smart decision (clear weather job)  
- -0.4 → risky decision (rainy job)  
- +0.5 → intelligent rejection  
- -0.3 → idle waiting penalty  
- +0.3 → high demand bonus  
- -0.2 → fatigue penalty  
- +1.0 → task completion bonus  

This provides continuous learning signals instead of binary outcomes.

---

## 🧪 Tasks & Difficulty

- Easy → Earn ₹300 in stable conditions  
- Medium → Earn ₹500 with mixed conditions  
- Hard → Earn ₹800 under high uncertainty  

---

## 🤖 Baseline Agent

A simple heuristic agent:
- adapts to weather  
- manages fatigue  
- avoids risky decisions  

Achieves consistent high performance.

---

## 🏗️ System Architecture

- RL Environment (OpenEnv compliant)  
- FastAPI backend  
- Docker deployment  
- Hugging Face Spaces hosting  

---

## 🔌 API Endpoints

GET /reset  
→ initialize environment  

POST /step  
→ perform action  
Example:
{
  "action": "accept_job"
}

---

## 📈 Real-World Applications

- Delivery optimization (Swiggy, Zomato)  
- Ride-sharing AI (Uber, Ola)  
- Logistics decision systems  
- Autonomous planning agents  

---

## 🎯 Innovation Highlights

- Real-world simulation (not a toy problem)  
- Meaningful reward shaping  
- Multi-step decision-making  
- Human-like constraints (fatigue, risk)  
- Fully OpenEnv compliant  

---

## 🚀 Deployment

Live Environment:
https://swarit17-gigshield-env.hf.space

---

## 🧠 Future Scope

- Multi-agent simulation  
- Real-time weather integration  
- Personalized strategies  
- Full RL training pipelines  

---

## 👨‍💻 Author

Swarit Singh  

---

## 🏁 Final Thought

This environment models real-world human decision-making under uncertainty, enabling smarter AI systems for logistics and gig economies.
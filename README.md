---
title: GigShield Env
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: server/app.py
pinned: false
---

# 🚀 GigShield Environment

AI-powered reinforcement learning environment simulating gig workers making decisions under uncertainty.

## 💡 Problem
Gig workers face unpredictable income due to:
- weather conditions
- fluctuating demand
- fatigue

## 🎯 Goal
Train agents to maximize earnings while minimizing risk.

## ⚙️ Features
- Real-world simulation
- Reward shaping
- Multi-level tasks (easy, medium, hard)
- OpenEnv compliant

## 🧪 API Endpoints
- `/reset` → initialize environment
- `/step` → perform action

## 📊 Reward Design Philosophy

The reward function is shaped to reflect real-world gig work trade-offs:
- Encourages accepting jobs in favorable conditions
- Penalizes risky decisions (e.g., bad weather)
- Incorporates fatigue as a long-term constraint
- Provides partial rewards to guide agent learning

This ensures stable and meaningful learning signals across episodes.
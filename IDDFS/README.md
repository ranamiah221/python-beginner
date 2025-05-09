# 🧠 Iterative Deepening Depth-First Search (IDDFS) – Lab Report 02

## 📌 Project Summary

This project demonstrates the implementation of the **Iterative Deepening Depth-First Search (IDDFS)** algorithm in a maze-solving context. IDDFS merges the depth-limited precision of **DFS** with the completeness of **BFS**, making it highly effective for scenarios where the solution depth is unknown.

This project is part of the **Artificial Intelligence Lab** (CSE 316) under the **Green University of Bangladesh** curriculum.

---

## 🎯 Objectives

- Understand the principle of IDDFS, combining DFS and BFS traits.
- Implement depth-limited search with increasing depth levels.
- Solve a grid-based maze to find a valid path from start to goal.
- Record traversal order and indicate success or failure clearly.

---


## 🔧 How It Works

1. The user inputs the size and layout of the maze (`0 = path`, `1 = wall`).
2. The user provides starting and target coordinates.
3. The program applies IDDFS with increasing depth limits until:
   - A valid path is found, or
   - The depth limit reaches the maximum possible (rows × cols).
4. If a path is found, it displays the traversal order and the number of steps.

---




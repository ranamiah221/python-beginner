# 🎨 Graph Coloring Using Backtracking in Python

This project implements a **Graph Coloring** algorithm using **Backtracking** to determine whether an undirected graph can be colored using **K colors** such that no two adjacent vertices share the same color.

---

## 📌 Problem Statement

Given a graph with `N` vertices and `M` edges, and a number `K`, determine whether it's possible to assign colors (from 1 to K) to each vertex such that no two connected vertices have the same color.

---
## 🔍 Input Format

Where:
- `N` is the number of vertices (labeled from 0 to N−1)
- `M` is the number of edges
- `K` is the number of available colors
- Each `u v` line defines an undirected edge between vertex `u` and vertex `v`


## 🧠 Algorithm

This solution uses **Backtracking**:
1. Try assigning each color (1 to K) to the current vertex.
2. Check if it conflicts with adjacent vertices.
3. If no conflict, move to the next vertex.
4. If coloring fails, backtrack and try a different color.
5. Repeat until either a solution is found or all possibilities are exhausted.
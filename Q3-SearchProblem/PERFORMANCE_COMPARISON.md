# Performance Comparison of Search Algorithms

## Algorithms Implemented

The following uninformed search algorithms were implemented to solve the **Missionaries and Cannibals problem**:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Depth-Limited Search (DLS)
- Iterative Deepening Search (IDS)

The comparison was based on the following metrics:

- Solution depth
- Number of nodes expanded
- Execution time

---

## Observed Results

| Algorithm | Solution Depth | Nodes Expanded | Time (ms) |
|----------|---------------|---------------|-----------|
| BFS | 11 | 14 | 0.0634 |
| DFS | 11 | 11 | 0.0434 |
| DLS | 11 | 14 | 0.0525 |
| IDS | 11 | 103 | 0.4370 |

---

## Discussion

Breadth-First Search explores the state space level by level and guarantees an optimal solution when step costs are equal. In this problem, BFS expanded 14 nodes before reaching the goal state.

Depth-First Search expanded fewer nodes in this execution and completed slightly faster because it explored a branch that directly led to a valid solution. However, DFS does not guarantee optimality in general problems.

Depth-Limited Search behaves similarly to DFS but restricts the search depth to avoid exploring infinitely deep branches.

Iterative Deepening Search repeatedly performs depth-limited searches with increasing depth limits. Because earlier levels are explored multiple times, IDS expanded more nodes and required more time compared to the other algorithms.

---

## Conclusion

All four algorithms successfully found a solution with a depth of 11 moves. BFS guarantees the optimal solution, while DFS required the fewest node expansions in this execution. IDS combines the advantages of BFS and DFS in theory but resulted in the highest number of node expansions due to repeated searches.

# Cheat Sheet for the Leet Python

<!--toc:start-->

- [Cheat Sheet for the Leet Python](#cheat-sheet-for-the-leet-python)
  - [List](#list)
    - [Uncommon maneuvers](#uncommon-maneuvers)
  - [String](#string)
    - [Alphabet to index](#alphabet-to-index)
    - [Permutation in String](#permutation-in-string)
  - [Graph](#graph)
    - [Simulate Reachability](#simulate-reachability)
    - [Multi-Source Reachability](#multi-source-reachability)
  - [Others](#others)
  <!--toc:end-->

## List

### Uncommon maneuvers

- List repetition: `[0] * 3 -> [0, 0, 0]`

## String

### Alphabet to index

Ascii # of letter - ascii of a to get the index

- `ord(char) - ord('a')`
  - ord: The ord() function returns the number representing the Unicode code of a specified character.

### Permutation in String

Similar to anagrams where hash maps of a ~ z are used to determine between two strings, except add sliding window. See [Permutation_in_String](./567-Permutation_in_String/permu_string.py).

## Graph

### Simulate Reachability

- Use a visited matrix w/ dfs or bfs

### Multi-Source Reachability

See [Pacific Atlantic Water Flow](./417-Pacific_Atlantic_Waterflow/)

- Start from source edge/boundaries and propagate
- Combine results depending on problem (by union or intersection)

## DP

### Staircase DP Patterns (Cheat Sheet)

- **State:** `dp[i]` → Best way to reach step `i` (min/max cost, # ways, etc.).  
- **Transition:** Usually `dp[i]` depends on `dp[i-1]`, `dp[i-2]`.  
- **Base Case:** Set `dp[0]`, `dp[1]` explicitly.  
- **Optimize Space:** Use `O(1)` space with two variables (`prev1, prev2`).  
- **Common Problems:** **#70 Climbing Stairs** → Ways to reach `n`, **#746 Min Cost Climbing Stairs** → Min cost to reach top, **#55, #45 Jump Game** → Min/max jumps to finish, **#198, #213 House Robber** → Skip adjacent steps.  

💡 **Pattern:** **Stair-like problems use DP with previous step dependencies.**

## Others

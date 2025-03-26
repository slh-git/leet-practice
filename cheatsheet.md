# Cheat Sheet for the Leet Python

<!--toc:start-->
- [Cheat Sheet for the Leet Python](#cheat-sheet-for-the-leet-python)
  - [Dictionary](#dictionary)
  - [Float](#float)
    - [Infinities](#infinities)
  - [List](#list)
    - [Useful List Manipulations](#useful-list-manipulations)
  - [String](#string)
    - [Alphabet to index](#alphabet-to-index)
    - [Permutation in String](#permutation-in-string)
  - [Stack](#stack)
  - [Heap](#heap)
    - [Max Heap](#max-heap)
  - [Graph](#graph)
    - [Simulate Reachability](#simulate-reachability)
    - [Multi-Source Reachability](#multi-source-reachability)
  - [DP](#dp)
    - [Staircase DP Patterns (Cheat Sheet)](#staircase-dp-patterns-cheat-sheet)
  - [Hash Maps](#hash-maps)
  - [XOR](#xor)
  - [Others](#others)
<!--toc:end-->

## Dictionary

- Can use anything immutable as key, eg: **tuple, frozen** set. See [39-Valid_Sudoku](./36-Valid_Sudoku/valid_sudoku_1pass.py)

## Float

### Infinities

- float("-inf"), float("inf")

## List

### Useful List Manipulations

- List repetition: `[0] * 3 -> [0, 0, 0]`
- Use enumerate in for loop: `for i, val in enumerate(arr):` to get index and value
- Merge two lists into list of pairs etc. `pair = [[l1, l2] for l1, l2 in zip(list1, list2)]`

## String

### Alphabet to index

ASCII# of letter - ASCII of a to get the index

- `ord(char) - ord('a')`
  - ord: The ord() function returns the number representing the Unicode code of a specified character.

### Permutation in String

Similar to anagrams where hash maps of a ~ z are used to determine between two strings, except add sliding window. See [Permutation_in_String](./567-Permutation_in_String/permu_string.py).

## Stack

- Good for merging/combining elems, keep track of most relevant item (eg: [853 Car Fleet](./853-Car_Fleet/car_fleet_stack.py))

## Heap

Use `import heapq` and `heapq.heapify(<list>)` `heapq.heappush(<list>, <value>)` `heapq.heappop(<list>)`

> [!NOTE]
> This is a min heap, to use max heap, multiply values by -1

### Max Heap

> [!NOTE]
> Python heapq no max heap, we can convert positive values to negative and use min heap if all values are positive

- See [Last Stone Weight](./1046-Last_Stone_Weight/last_stone_weight.py) for example

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

## Hash Maps

- Usually when past value is needed for O(1) lookup.
- Keywords: Difference, Sum, Frequency, Compliments, etc.

## XOR

See [268 Missing Number](268-Missing_Number/missing_num_xor.py)

- `xor ^= x ^ y`

## Others

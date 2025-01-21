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

## Others

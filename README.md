DSASTUDY 📚
https://docs.google.com/document/d/1uiz-vzixtnyBzakkyJwgZx40EkCq0nbJfQeaPwzKFTw/edit?tab=t.0

A complete guide to important Data Structures and Arrays for coding interviews (FAANG, product-based companies, startups).

🧱 Important Data Structures
1. Arrays

Must Know: Traversal, Insertion, Deletion

Problems:

Find max/min

Reverse array

Kadane’s Algorithm (max subarray sum)

Two Sum, Move Zeroes, Merge Sorted Arrays

Concepts: Prefix sum, Sliding window

2. Strings

Must Know: Palindrome check, Anagrams

Problems:

String reversal, Substring search

Character frequency, Removing duplicates

Pattern Matching (KMP, Rabin-Karp basics)

String compression, rotation

3. Linked List

Must Know: Singly, Doubly, and Circular Linked Lists

Problems:

Reverse a linked list

Detect cycle (Floyd’s algorithm)

Middle element, Intersection point

Merge two sorted lists

4. Stacks

Must Know: Implementation using array/linked list

Problems:

Balanced parentheses

Next Greater Element

Min Stack

Evaluate Postfix/Prefix

Stock Span Problem

5. Queues

Must Know: Normal Queue, Circular Queue, Priority Queue

Problems:

Implement queue using stacks

Rotten Oranges (BFS)

Sliding Window Maximum

6. Trees

Must Know: Binary Tree & Binary Search Tree (BST)

Traversals: Inorder, Preorder, Postorder, Level Order

Problems:

Height / Diameter

Lowest Common Ancestor (LCA)

Symmetric Tree

Path Sum

Serialize/Deserialize Tree

7. Heaps (Priority Queues)

Must Know: Min-Heap, Max-Heap

Problems:

Kth largest/smallest element

Heap sort

Merge K sorted lists

Top K frequent elements

8. Hashing (HashMap / HashSet)

Must Know: Counting frequency, duplicates

Problems:

Two Sum

Subarray with given sum

Longest consecutive sequence

Group Anagrams

9. Graphs

Must Know: Representations: Adjacency List / Matrix

Traversals: BFS, DFS

Algorithms:

Dijkstra, Bellman-Ford, Floyd-Warshall

Topological Sort

Union-Find (Disjoint Sets)

Minimum Spanning Tree (Prim’s, Kruskal’s)

Detect cycles (directed/undirected)

10. Recursion & Backtracking

Must Know: Factorial, Fibonacci

Problems:

Subsets, Permutations

N-Queens, Sudoku Solver

Rat in a Maze, Word Search

11. Dynamic Programming (DP)

Must Know: Fibonacci, Knapsack, Subset Sum

Problems:

Longest Common Subsequence / Substring

Longest Increasing Subsequence (LIS)

Matrix Chain Multiplication

Coin Change, Edit Distance

12. Advanced / Optional

Trie (prefix tree): Autocomplete, Word Search

Segment Tree / Fenwick Tree (BIT): Range queries

Disjoint Set Union (DSU): Connected components

LRU Cache: Using LinkedHashMap or DLL + HashMap

🧱 ARRAYS — Full Interview Guide
1️⃣ Concepts & Theory

What is an Array?

Linear data structure storing elements in contiguous memory locations.

Access elements using index (starting from 0).

Common Operations:

Operation	Time Complexity	Description
Access	O(1)	Direct index access
Search	O(n)	Linear search
Insert (end)	O(1)	Append element
Insert (middle)	O(n)	Shift elements
Delete (middle)	O(n)	Shift elements back

Types of Arrays:

1D Array → [1,2,3,4,5]

2D Array (Matrix) → [[1,2,3],[4,5,6],[7,8,9]]

Dynamic Array (Python List / C++ Vector) → Resizes automatically

2️⃣ Problem Types (with Examples)
🟢 Basic Problems

Find max and min element

Reverse an array

Find element in array (linear search)

Count frequency of elements

Remove duplicates (sorted array)

Rotate array (left/right)

Find second largest / smallest

Check if array is sorted

🟠 Prefix Sum & Subarray Problems

Prefix sum array creation

Subarray sum = K (using HashMap)

Maximum Subarray Sum (Kadane’s Algorithm)

Equilibrium index (left sum = right sum)

Count subarrays with equal 0s and 1s

Range sum queries (with prefix sum)

Trapping Rain Water problem

Product of array except self

🔵 Two-Pointer / Sliding Window Problems

Pair with given sum in sorted array

Remove duplicates from sorted array

Move all zeroes to end

Find max sum subarray of size K

Longest subarray with sum ≤ K

Container with most water

Minimum window subarray

🟣 Sorting & Rearrangement

Sort 0s, 1s, and 2s (Dutch National Flag)

Find missing number in sequence

Find duplicate number (Floyd’s cycle or XOR)

Merge two sorted arrays

Rearrange positive & negative numbers alternately

Find k-th largest/smallest (using heap or sort)

🔴 Searching Algorithms

Binary Search (iterative & recursive)

Search in rotated sorted array

First and last occurrence of element

Count occurrences of element (using binary search)

Find peak element

Square root using binary search

⚫ Matrix (2D Array) Problems

Transpose of matrix

Rotate matrix by 90 degrees

Spiral traversal

Search in sorted matrix

Set matrix zeroes

Find path sum (for DP linkage later)

⚪ Advanced / Trickier Array Patterns

Maximum product subarray

Longest consecutive sequence (using HashSet)

Subarray sum divisible by K

Find all triplets with sum = 0 (3Sum)

Majority element (Moore’s Voting)

Next permutation

Merge intervals

Best time to buy & sell stock (multiple variants)

🚀 Common Patterns / Tricks
Pattern	Where Used	Description
Prefix Sum	Range queries, subarray sum	Precompute sums to answer queries fast
Sliding Window	Fixed/variable length subarrays	Maintain a window of size K
Two Pointer	Sorted arrays / removing elements	Move left/right pointers intelligently
Kadane’s Algo	Max subarray sum	Keep running sum with reset condition
Binary Search	Sorted arrays	Divide and conquer for efficiency
Hashing	Count / check presence	Use dict or map for O(1) lookups
XOR Trick	Missing/duplicate number	XOR all elements cleverly

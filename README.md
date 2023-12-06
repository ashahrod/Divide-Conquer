# Divide and Conquer: Efficient Algorithm for Finding Missing Elements

## Overview

This project focuses on designing a highly efficient algorithm to identify a missing element in a sorted sequence of integers. The problem is approached through divide and conquer strategies, providing both logarithmic and linear time solutions.

## Approach Details

### Part 1: Finding Missing Elements
Given a sorted sequence of integers, the task is to identify the missing element. A naïve linear approach is introduced for context.

### Part 2: Binary-Search-Based Approach
Assuming distinct elements, the goal is to design a divide and conquer algorithm with a time complexity of O(log n) to find the missing element. Avoid unnecessary computation by discarding subproblems using binary search principles.

### Part 3: Merge-Sort-Based Approach
Generalizing the problem to allow non-distinct elements, propose an O(n) complexity algorithm based on merge-sort principles. This approach solves all subproblems due to the nature of the problem.

### Usage Example

```bash
$ ./compile.sh
$ ./run.sh input.txt

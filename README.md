# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions

Hash functions should:
- Take any data as input and output a number
- Be a pure function or consistent / deterministic e.g. for the same input, return the same output
- Return numbers in a specific range (to minimize collisions)

2. Collision resolution

Open addressing with linear probing
- On encountering a collision, iterate through the buckets until an empty slot is found (loop back to beginning if needed)
- Problem with linear probing is that it causes clustering: with collisions in the same area of the table, more items group around that one area instead of evenly distributing
- Quadratic probing skips slots to minimize clustering
Chaining
- Each bucket is a reference to a chain or linked list of items
- Compared to linear probing, on average, each bucket is likely to have fewer items

3. Performance of basic hash table operations

- On average, search, insert, and delete is `O(1)` and `O(n)` at worst
- In the worst case, close to all values are hashed to the same index
- Hash tables trade space for time

4. Load factor

- Load factor = number of items in hash table / number of buckets
- Max load factor for linear probing is 1
- Max load factor for chaining can be greater than 1

5. Automatic resizing

- Automatic resizing can improve performance of hash table, and done when load factor is too big or small
- Generally: double when load factor is > 0.7 or halve when when around 0.2
- Create a new hash table, then rehash all elements to the new table

6. Various use cases for hash tables

Hash tables can be used if quick access is needed.
- Lookups: map one thing to another thing
- Duplicate prevention: check if a thing has already been recorded
- Caching: save results of expensive computations

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request


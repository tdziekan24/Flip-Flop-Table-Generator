### Flip-Flop Table Generator
##### v1.0 by Tomasz Dziekański, February 5th 2025

---
#### 1. What the program does:
The program automatically creates flip-flop input functions as tables from a state-transition table of a Moore machine encoded in binary. It supports **D**, **T**, **RS** and **JK** flip-flops.

---
#### 2. Why this program exists:
Because I couldn't find any tools that perform this specific task, and it is extremely hard for a human not to make any mistakes. It also barely requires any thinking while being extremely time-consuming and should not be done by a human.

---
#### 3. Creating a .json file
- The table must be a list of lists (rows) of strings (states);
- Each row must be equal in length and that length must be a power of **2**;
- Each state must be denoted by a binary string (set length, assume its length to be **n**; bits) or a string of hyphens (any length, including 0), which represent the empty states;
- The table must contain precisely **2^n** rows.

Below is an example of a correctly entered list:
```json
[
    ["000", "001", "010", "011"],
    ["100", "101", "110", "111"],
    ["010", "010", "111", "110"],
    ["010", "010", "110", "101"],
    ["001", "001", "110", "111"],
    ["000", "000", "111", "001"],
    ["---", "---", "---", "---"],
    ["---", "--", "-", ""]
]
```
---
#### 4. Running the program:
1. Download the files from the repository
2. Enter the directory with the files
3. Type the following command:
    ```bash
    python main.py [file name] [flip-flop type]
    ```
4. For more information on the options, run
    ```bash
    python main.py --help
    ```

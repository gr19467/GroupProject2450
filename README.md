# GroupProject2450

# UVSim - BasicML Virtual Machine

## How to Run

1. Open a terminal.
2. Run `python uvsim.py`.
3. Enter the program file when prompted (e.g., `Test1.txt`).
4. The UVSim will execute the instructions in the file.

## Input File Format

- Each line in the input file should contain a **signed four-digit number**.
- Instructions are stored sequentially in memory.
- The **last line** of the file should be `-99999` to mark the end.

## Supported Commands

| Opcode | Instruction | Description                          |
| ------ | ----------- | ------------------------------------ |
| 10XX   | READ        | Read input into memory[XX]           |
| 11XX   | WRITE       | Print memory[XX]                     |
| 20XX   | LOAD        | Load memory[XX] into accumulator     |
| 21XX   | STORE       | Store accumulator into memory[XX]    |
| 30XX   | ADD         | Add memory[XX] to accumulator        |
| 31XX   | SUBTRACT    | Subtract memory[XX] from accumulator |
| 32XX   | DIVIDE      | Divide accumulator by memory[XX]     |
| 33XX   | MULTIPLY    | Multiply accumulator by memory[XX]   |
| 40XX   | BRANCH      | Jump to memory[XX]                   |
| 41XX   | BRANCHNEG   | Jump if accumulator is negative      |
| 42XX   | BRANCHZERO  | Jump if accumulator is zero          |
| 43XX   | HALT        | Stop execution                       |

## Running Unit Tests

To run the unit tests, execute:

```
python -m unittest uvsim.py
```

When prompted to select a file, select "Test1.txt"

This will automatically verify all functionalities.

## Error Handling

- **Division by zero** is detected and will halt execution.
- **Invalid opcodes** will print an error and stop execution.
<<<<<<< HEAD
- **Out-of-bounds memory access** is prevented.
=======
- **Out-of-bounds memory access** is prevented.
>>>>>>> origin/main

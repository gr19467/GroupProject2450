# GroupProject2450

# UVSim - BasicML Virtual Machine

## How to Run

1. Open a terminal.
2. Run `python uvsim.py`.
3. Enter the program file when prompted (e.g., `Test1.txt`).
4. The UVSim will execute the instructions in the file.

## Input File Format

- Each line in the input file should contain a **signed six-digit number**.
- Instructions are stored sequentially in memory (up to 250 lines).
- The **last line** of the file should be `-99999` to mark the end.

## Supported Commands

| Opcode | Instruction | Description                          |
|--------| ----------- | ------------------------------------ |
| 010XXX | READ        | Read input into memory[XX]           |
| 011XXX | WRITE       | Print memory[XX]                     |
| 020XXX | LOAD        | Load memory[XX] into accumulator     |
| 021XXX | STORE       | Store accumulator into memory[XX]    |
| 030XXX | ADD         | Add memory[XX] to accumulator        |
| 031XXX | SUBTRACT    | Subtract memory[XX] from accumulator |
| 032XXX | DIVIDE      | Divide accumulator by memory[XX]     |
| 033XXX | MULTIPLY    | Multiply accumulator by memory[XX]   |
| 040XXX | BRANCH      | Jump to memory[XX]                   |
| 041XXX | BRANCHNEG   | Jump if accumulator is negative      |
| 042XXX | BRANCHZERO  | Jump if accumulator is zero          |
| 043XXX | HALT        | Stop execution                       |

## File Format Compatibility
UVSIM now supports both 4-digit and 6-digit instruction formats.

- Files in 4-digit format can be **converted to** 6-digit using the built-in conversion tool.
- Converted files have leading zeroes added to the opcode and address.
- All instructions within a file must match the same format (mixing 4-digit and 6-digit is not allowed)

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
- **Out-of-bounds memory access** is prevented.
>>>>>>> origin/main

# UVSim - High-Level Functionality Document

## **System Overview**

UVSim (Universal Virtual Simulator) is a virtual machine designed for computer science students to learn machine language and computer architecture. It simulates a simple CPU with an accumulator register and a 100-word memory, executing BasicML instructions. Programs are loaded from a file into memory and executed sequentially unless modified by branching instructions.

## **User Stories**

### **1. A Student Runs UVSim to Learn Machine Language**

As a computer science student,  
I want to execute my BasicML programs on UVSim,  
So that I can learn how machine language works through hands-on execution.

### **2. A Teacher Tests Student Programs**

As a computer science professor,  
I want to verify students' machine code execution using UVSim,  
So that I can ensure they understand machine instructions and program flow.

## **Use Cases**

### **1. Load a Value into Memory**

**Description:** The user loads a specific value into memory at a designated address.
**Steps:**

1. User provides an instruction with opcode `21XX`.
2. The value stored in the accumulator is saved to memory at location `XX`.
3. The system confirms the storage.

### **2. Retrieve a Value from Memory**

**Description:** The user loads a value from memory into the accumulator.
**Steps:**

1. User provides an instruction with opcode `20XX`.
2. The value at memory location `XX` is copied into the accumulator.
3. The system updates the accumulator value.

### **3. Perform Addition**

**Description:** The system adds a value from memory to the accumulator.
**Steps:**

1. User provides an instruction with opcode `30XX`.
2. The value at memory location `XX` is added to the accumulator.
3. The system stores the result in the accumulator.

### **4. Perform Subtraction**

**Description:** The system subtracts a value in memory from the accumulator.
**Steps:**

1. User provides an instruction with opcode `31XX`.
2. The value at memory location `XX` is subtracted from the accumulator.
3. The system updates the accumulator with the new value.

### **5. Perform Multiplication**

**Description:** The system multiplies the accumulator by a value in memory.
**Steps:**

1. User provides an instruction with opcode `33XX`.
2. The value at memory location `XX` is multiplied by the accumulator.
3. The system updates the accumulator with the result.

### **6. Perform Division**

**Description:** The system divides the accumulator by a value in memory, handling division by zero.
**Steps:**

1. User provides an instruction with opcode `32XX`.
2. The system checks if the divisor is zero. If yes, execution halts with an error message.
3. Otherwise, the system performs the division and updates the accumulator.

### **7. Branching to a Memory Address**

**Description:** The system jumps execution to a different memory address unconditionally.
**Steps:**

1. User provides an instruction with opcode `40XX`.
2. The instruction counter updates to `XX`.
3. Execution continues from the new memory location.

### **8. Branching on Negative Value**

**Description:** The system jumps to a new memory address if the accumulator contains a negative value.
**Steps:**

1. User provides an instruction with opcode `41XX`.
2. If the accumulator is negative, the instruction counter updates to `XX`.
3. Execution continues from the new memory location.

### **9. Branching on Zero Value**

**Description:** The system jumps to a new memory address if the accumulator contains zero.
**Steps:**

1. User provides an instruction with opcode `42XX`.
2. If the accumulator is zero, the instruction counter updates to `XX`.
3. Execution continues from the new memory location.

### **10. Writing to Output**

**Description:** The system prints a value stored in memory to the screen.
**Steps:**

1. User provides an instruction with opcode `11XX`.
2. The system retrieves the value at memory location `XX`.
3. The value is printed to the console.

### **11. Reading from Input**

**Description:** The system takes user input and stores it in memory.
**Steps:**

1. User provides an instruction with opcode `10XX`.
2. The system prompts the user for an input value.
3. The value is stored at memory location `XX`.

### **12. Halt Execution**

**Description:** The system stops executing instructions when a halt command is encountered.
**Steps:**

1. User provides an instruction with opcode `43XX`.
2. The system sets the `running` flag to `False`.
3. Execution stops immediately.

### **13. Handling Invalid Opcodes**

**Description:** The system detects an invalid opcode and terminates execution with an error.
**Steps:**

1. The system encounters an unrecognized opcode.
2. An error message is printed.
3. Execution halts to prevent unexpected behavior.

### **14. Handling Out-of-Bounds Memory Access**

**Description:** The system prevents memory accesses beyond allocated space.
**Steps:**

1. The user attempts to load/store data in an invalid memory location (outside 0-99).
2. The system detects the issue and prevents execution from continuing.
3. An error message is displayed, and execution stops.

### **15. Execution of a Full Program from File**

**Description:** The system reads and executes a complete BasicML program from a file.
**Steps:**

1. The user provides the filename containing BasicML instructions.
2. The system loads instructions into memory.
3. The system executes instructions sequentially until encountering `HALT` or an error.

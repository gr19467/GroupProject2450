# UVSim - High-Level Functionality Document

## **System Overview**

UVSim (Universal Virtual Simulator) is a virtual machine designed for computer science students to learn machine language and computer architecture. It simulates a simple CPU with an accumulator register and a 250-word memory, executing BasicML instructions. Programs are loaded from a file into memory and executed sequentially unless modified by branching instructions.

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

1. User provides an instruction with opcode `021XXX`.
2. The value stored in the accumulator is saved to memory at location `XXX`.
3. The system confirms the storage.

### **2. Retrieve a Value from Memory**

**Description:** The user loads a value from memory into the accumulator.
**Steps:**

1. User provides an instruction with opcode `020XXX`.
2. The value at memory location `XXX` is copied into the accumulator.
3. The system updates the accumulator value.

### **3. Perform Addition**

**Description:** The system adds a value from memory to the accumulator.
**Steps:**

1. User provides an instruction with opcode `030XXX`.
2. The value at memory location `XXX` is added to the accumulator.
3. The system stores the result in the accumulator.

### **4. Perform Subtraction**

**Description:** The system subtracts a value in memory from the accumulator.
**Steps:**

1. User provides an instruction with opcode `031XXX`.
2. The value at memory location `XXX` is subtracted from the accumulator.
3. The system updates the accumulator with the new value.

### **5. Perform Multiplication**

**Description:** The system multiplies the accumulator by a value in memory.
**Steps:**

1. User provides an instruction with opcode `033XXX`.
2. The value at memory location `XXX` is multiplied by the accumulator.
3. The system updates the accumulator with the result.

### **6. Perform Division**

**Description:** The system divides the accumulator by a value in memory, handling division by zero.
**Steps:**

1. User provides an instruction with opcode `032XXX`.
2. The system checks if the divisor is zero. If yes, execution halts with an error message.
3. Otherwise, the system performs the division and updates the accumulator.

### **7. Branching to a Memory Address**

**Description:** The system jumps execution to a different memory address unconditionally.
**Steps:**

1. User provides an instruction with opcode `040XXX`.
2. The instruction counter updates to `XXX`.
3. Execution continues from the new memory location.

### **8. Branching on Negative Value**

**Description:** The system jumps to a new memory address if the accumulator contains a negative value.
**Steps:**

1. User provides an instruction with opcode `041XXX`.
2. If the accumulator is negative, the instruction counter updates to `XXX`.
3. Execution continues from the new memory location.

### **9. Branching on Zero Value**

**Description:** The system jumps to a new memory address if the accumulator contains zero.
**Steps:**

1. User provides an instruction with opcode `042XXX`.
2. If the accumulator is zero, the instruction counter updates to `XX`.
3. Execution continues from the new memory location.

### **10. Writing to Output**

**Description:** The system prints a value stored in memory to the screen.
**Steps:**

1. User provides an instruction with opcode `011XXX`.
2. The system retrieves the value at memory location `XXX`.
3. The value is printed to the console.

### **11. Reading from Input**

**Description:** The system takes user input and stores it in memory.
**Steps:**

1. User provides an instruction with opcode `010XXX`.
2. The system prompts the user for an input value.
3. The value is stored at memory location `XXX`.

### **12. Halt Execution**

**Description:** The system stops executing instructions when a halt command is encountered.
**Steps:**

1. User provides an instruction with opcode `043XXX`.
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

1. The user attempts to load/store data in an invalid memory location (outside 0-249).
2. The system detects the issue and prevents execution from continuing.
3. An error message is displayed, and execution stops.

### **15. Execution of a Full Program from File**

**Description:** The system reads and executes a complete BasicML program from a file.
**Steps:**

1. The user provides the filename containing BasicML instructions.
2. The system loads instructions into memory.
3. The system executes instructions sequentially until encountering `HALT` or an error.

### **16. Convert Old Format File**
**Description:** The system reads and converts from a 4-digit to a 6-digit format version of the file.
**Steps:**

1. The user selects a 4-digit format file.
2. The system adds leading zeroes to each opcode and address.
3. The system writes a 6-digit format version of the file.

## **17. Open Multiple Files**
**Description:** The system creates a new file tab allowing editing/running multiple files in one app instance
**Steps:**

1. The user selects "Open File"
2. A new file tab is created.
3. The user can edit/run multiple files simultaneously within one app instance

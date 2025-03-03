# Simulator class - James
class Simulator:
    def __init__(self):
        # Define registers
        self.accumulator = 0  # Accumulator register
        self.instruction_counter = 0  # Program counter
        self.instruction_register = 0  # Current instruction register
        self.operation_code = 0  # Current operation code
        self.operand = 0  # Current operand

        # Define memory and index
        self.memory = [0] * 100  # 100-word memory
        self.index = 0  # Memory index

        # List of SML instructions
        self.instructions = {
            10: "READ",
            11: "WRITE",
            20: "LOAD",
            21: "STORE",
            30: "ADD",
            31: "SUBTRACT",
            32: "DIVIDE",
            33: "MULTIPLY",
            40: "BRANCH",
            41: "BRANCH_NEG",
            42: "BRANCH_ZERO",
            43: "HALT"
        }

    def load_program(self, program):
        """Load a program into memory."""
        for i, instruction in enumerate(program):
            if instruction == -99999:
                break
            self.memory[i] = instruction
        self.index = i  # Set memory index

    def reset(self):
        """Reset the simulator to its initial state."""
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0
        self.memory = [0] * 100
        self.index = 0


# run_simulator() function - Jonah
def run_simulator(simulator):
    """Run the simulator."""
    simulator.reset()
    print_instructions()
    program = []
    while True:
        instruction = input(f"{simulator.instruction_counter} ? ")
        if instruction == "-99999":
            break
        try:
            program.append(int(instruction))
            simulator.instruction_counter += 1
        except ValueError:
            print("Invalid input. Please enter an integer.")
    simulator.load_program(program)
    execute(simulator)


# Print user instructions - Gaby
def print_instructions():
    print("Welcome to UVSim! \n"
          "Please enter your program one instruction \n"
          "or data word at a time into the input text field. \n"
          "I will display the location number and a question mark, \n"
          "then you type in the word for that location. To stop \n"
          "input, enter -99999.")


# validate() function - Jonah
def validate(value):
    """Validate input value."""
    try:
        int(value)
        return True
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False


# test_overflow() function - Jonah
def test_overflow(accumulator):
    """Test for accumulator overflow."""
    if accumulator > 9999 or accumulator < -9999:
        print("Error: Accumulator overflow.")
        return True
    return False


# Execute() function - Gaby
def execute(simulator):
    """Execute the program in memory."""
    print("***Program execution begins***")
    while simulator.instruction_counter <= simulator.index:
        # Fetch instruction
        simulator.instruction_register = simulator.memory[simulator.instruction_counter]
        simulator.operation_code = simulator.instruction_register // 100
        simulator.operand = simulator.instruction_register % 100

        simulator.instruction_counter += 1

        # Execute instruction
        if simulator.operation_code == 10:  # READ
            value = input(f"Enter an integer for memory location {simulator.operand}: ")
            if validate(value):
                simulator.memory[simulator.operand] = int(value)
        elif simulator.operation_code == 11:  # WRITE
            print(simulator.memory[simulator.operand])
        elif simulator.operation_code == 20:  # LOAD
            simulator.accumulator = simulator.memory[simulator.operand]
        elif simulator.operation_code == 21:  # STORE
            simulator.memory[simulator.operand] = simulator.accumulator
        elif simulator.operation_code == 30:  # ADD
            simulator.accumulator += simulator.memory[simulator.operand]
            if test_overflow(simulator.accumulator):
                break
        elif simulator.operation_code == 31:  # SUBTRACT
            simulator.accumulator -= simulator.memory[simulator.operand]
            if test_overflow(simulator.accumulator):
                break
        elif simulator.operation_code == 32:  # DIVIDE
            if simulator.memory[simulator.operand] == 0:
                print("Error: Division by zero.")
                break
            simulator.accumulator //= simulator.memory[simulator.operand]
        elif simulator.operation_code == 33:  # MULTIPLY
            simulator.accumulator *= simulator.memory[simulator.operand]
            if test_overflow(simulator.accumulator):
                break
        elif simulator.operation_code == 40:  # BRANCH
            simulator.instruction_counter = simulator.operand
        elif simulator.operation_code == 41:  # BRANCH_NEG
            if simulator.accumulator < 0:
                simulator.instruction_counter = simulator.operand
        elif simulator.operation_code == 42:  # BRANCH_ZERO
            if simulator.accumulator == 0:
                simulator.instruction_counter = simulator.operand
        elif simulator.operation_code == 43:  # HALT
            print("***Program execution terminated***")
            break
        else:
            print("Fatal error: Invalid operation code.")
            break


# Unit Tests - Cortland
# TODO: Add unit tests for each operation code and edge cases.

# Example usage
if __name__ == "__main__":
    sim = Simulator()
    run_simulator(sim)



'''
Note: This is a branch meant to demonstrate edits made by Jonah in the second milestone; and much of this code has been modified 
- from the original; I modified several bugs such as saving an array with nonetype and an off-by-one in the opcode counter.
'''

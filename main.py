'''
THIS IS HERE FOR DEMONSTRATION PURPOSES - AN UNPUSHED UPDATE MADE FOR MILESTONE 2 BY JONAH ON FEB 12, 2025. DON'T MERGE THIS 
WITH THE MAIN BRANCH
file info at https://imgur.com/a/timestamping-25tDYUx
'''



# Simulator class - James
#   list of SML instructions
#   define registers
#   define memory and index
class Simulator:
    READ = 10
    WRITE = 11
    LOAD = 20
    STORE = 21
    ADD = 30
    SUBTRACT = 31
    DIVIDE = 32
    MULTIPLY = 33
    BRANCH = 40
    BRANCHNEG = 41
    BRANCHZERO = 42
    HALT = 43

    def __init__(self):
        self.memory = [0]*100 #jonah-modified to init memory with 0s
        self.accumulator = 0 #jonah-modified to init to 0 rather than none
        self.index = 0

# run_simulator() function - Jonah
def run_simulator():
    simulator=Simulator()
    print_instructions()
    while True:
        user_input = input(f"{simulator.index:02d} ? ")
        if user_input == "-99999":
            break
        try:
            instruction = int(user_input)
            if validate(instruction):
                simulator.memory[simulator.index] = instruction
                simulator.index += 1
            else:
                print("Invalid instruction. Please enter a valid instruction.") #jonah-modified to add validate and error message
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
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
def validate(instruction):
    operation_code = instruction // 100
    operand = instruction % 100
    
    valid_operations = [
        Simulator.READ, Simulator.WRITE, Simulator.LOAD, Simulator.STORE,
        Simulator.ADD, Simulator.SUBTRACT, Simulator.DIVIDE, Simulator.MULTIPLY,
        Simulator.BRANCH, Simulator.BRANCHNEG, Simulator.BRANCHZERO, Simulator.HALT
    ]
    
    if operation_code not in valid_operations:
        return False
    
    if operand < 0 or operand >= 100:
        return False
    
    return True

# test_overflow() function - Jonah
def test_overflow(value):
    # Assuming a 4-digit accumulator, so the range is -9999 to 9999
    return value < -9999 or value > 9999


# Execute() function - Gaby
def execute(simulator):
    print("***Program execution begins***")
    instruction_counter = 0
    
    while instruction_counter < simulator.index:
        instruction_register = simulator.memory[instruction_counter]
        operation_code = instruction_register // 100
        operand = instruction_register % 100

        instruction_counter += 1

        if operation_code == simulator.READ:
            print("Enter an integer:")
            simulator.memory[operand] = int(input())
        elif operation_code == simulator.WRITE:
            print(simulator.memory[operand])
        elif operation_code == simulator.LOAD:
            simulator.accumulator = simulator.memory[operand]
        elif operation_code == simulator.STORE:
            simulator.memory[operand] = simulator.accumulator
        elif operation_code == simulator.ADD:
            simulator.accumulator += simulator.memory[operand]
            if test_overflow(simulator.accumulator):
                print("Overflow error occurred.")
                return
        elif operation_code == simulator.SUBTRACT:
            simulator.accumulator -= simulator.memory[operand]
            if test_overflow(simulator.accumulator):
                print("Overflow error occurred.")
                return
        elif operation_code == simulator.MULTIPLY:
            simulator.accumulator *= simulator.memory[operand]
            if test_overflow(simulator.accumulator):
                print("Overflow error occurred.")
                return
        elif operation_code == simulator.DIVIDE:
            if simulator.memory[operand] == 0:
                print("Error: Division by zero.")
                return
            simulator.accumulator //= simulator.memory[operand]
        elif operation_code == simulator.BRANCH:
            instruction_counter = operand
        elif operation_code == simulator.BRANCHNEG:
            if simulator.accumulator < 0:
                instruction_counter = operand
        elif operation_code == simulator.BRANCHZERO:
            if simulator.accumulator == 0:
                instruction_counter = operand
        elif operation_code == simulator.HALT:
            print("*** Program execution terminated ***")
            return
        else:
            print("Fatal error: Invalid operation code.")
            return
#execute() code MODIFIED by Jonah - lmk if you want this reverted

# Unit Tests - Cortland


if __name__ == "__main__":
    run_simulator()

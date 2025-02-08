# Simulator class - James
#   list of SML instructions

#   define registers

#   define memory and index

# run_simulator() function - Jonah

# Print user instructions - Gaby
def print_instructions():
    print("Welcome to UVSim! \n"
          "Please enter your program one instruction \n"
          "or data word at a time into the input text field. \n"
          "I will display the location number and a question mark, \n"
          "then you type in the word for that location. To stop \n"
          "input, enter -99999.")


# validate() function - Jonah

# test_overflow() function - Jonah
def test_overflow():
    return


# Execute() function - Gaby
def execute():  # all elif statements with only return will be written later
    print("***Program execution begins***")
    while (instruction_counter < index):
        instruction_register = memory[instruction_counter]
        operation_code = instruction_register / 100
        operand = instruction_register % 100

        instruction_counter += 1

        if operation_code == "READ":
            print("Enter an integer:")
            memory[operand] = int(input())
        elif operation_code == "WRITE":
            print(memory[operand])
        elif operation_code == "LOAD":
            return
        elif operation_code == "STORE":
            return
        elif operation_code == "ADD":  # adds a memory address into the accumulator
            accumulator += memory[operand]

            if (test_overflow()):
                return
        elif operation_code == "SUBTRACT":
            return
        elif operation_code == "MULTIPLY":
            return
        elif operation_code == "DIVIDE":
            return
        elif operation_code == "BRANCH":
            return
        elif operation_code == "BRANCH_NEG":
            return
        elif operation_code == "BRANCH_ZERO":
            return
        elif operation_code == "HALT":
            return
        else:
            print("Fatal error: Invalid operation code.")
            return

# Unit Tests - Cortland

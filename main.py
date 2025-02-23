import unittest

# === PM (Cortland) ===
# todo: Oversee project progress, ensure SRS collection and final merge.
# todo: Manage GitHub branches and final submission.
# todo: Coordinate with team for code integration.

# === DEV 2 (Gaby) ===
# todo: Refactor UVSim to support GUI integration (decouple input/output).
# todo: Ensure all logic is modular and supports event-driven GUI interactions.

class UVSim:
    def __init__(self):
        self.memory = [0] * 100  # 100-word memory
        self.accumulator = 0  # Single register
        self.instruction_counter = 0  # Program counter
        self.running = True
# run_simulator() function - Jonah
def run_simulator():
    pass

    def load_program(self, filename):
        """Loads a program from a file into memory."""
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if int(line.strip()) == -99999:
                    break  # End of program
                self.memory[i] = int(line.strip())

    def execute(self):
        """Executes instructions in memory."""
        while self.running:
            instruction = self.memory[self.instruction_counter]
            opcode, operand = divmod(instruction, 100)

            if opcode == 10:  # READ
                if self.input_value is not None:
                    self.memory[operand] = self.input_value
                    self.input_value = None
            elif opcode == 11:  # WRITE
                self.output.append(self.memory[operand])
            elif opcode == 20:  # LOAD
                self.accumulator = self.memory[operand]
            elif opcode == 21:  # STORE
                self.memory[operand] = self.accumulator
            elif opcode == 30:  # ADD
                self.accumulator += self.memory[operand]
            elif opcode == 31:  # SUBTRACT
                self.accumulator -= self.memory[operand]
            elif opcode == 32:  # DIVIDE
                if self.memory[operand] == 0:
                    self.output.append("error: Division by zero")
                    self.running = False
                    continue
                self.accumulator //= self.memory[operand]
            elif opcode == 33:  # MULTIPLY
                self.accumulator *= self.memory[operand]
            elif opcode == 40:  # BRANCH
                self.instruction_counter = operand
                continue
            elif opcode == 41:  # BRANCHNEG
                if self.accumulator < 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 42:  # BRANCHZERO
                if self.accumulator == 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 43:  # HALT
                self.running = False
                break
            else:
                print(f"Unknown opcode {opcode} at address {self.instruction_counter}")
                self.running = False
                break

            self.instruction_counter += 1

if __name__ == "__main__":
    # === DEV 1 (Jonah) ===
    # todo: Replace command-line input/output with GUI elements.
    # todo: Create input fields for loading files and displaying memory state.
    # todo: Integrate 'Run Program' button to trigger UVSim execution.

    sim = UVSim()
    filename = input("Enter program file: ")  # === DEV 1: Replace with file picker in GUI
    sim.load_program(filename)
    sim.execute()


# === DEV 3 (James) ===
# todo: Expand unit tests to include GUI interactions.
# todo: Lead SRS documentation and ensure team follows functional requirements.

class TestUVSim(unittest.TestCase):
    def setUp(self):
        self.sim = UVSim()

    def test_load(self):
        self.sim.memory[10] = 25
        self.sim.execute()
        self.assertEqual(self.sim.memory[10], 25)

    def test_addition(self):
        self.sim.accumulator = 10
        self.sim.memory[5] = 15
        self.sim.memory[0] = 3005  # ADD 5
        self.sim.execute()
        self.assertEqual(self.sim.accumulator, 25)

    def test_subtraction(self):
        self.sim.accumulator = 50
        self.sim.memory[5] = 20
        self.sim.memory[0] = 3105  # SUBTRACT 5
        self.sim.execute()
        self.assertEqual(self.sim.accumulator, 30)

    def test_divide_by_zero(self):
        self.sim.accumulator = 50
        self.sim.memory[5] = 0
        self.sim.memory[0] = 3205  # DIVIDE 5
        self.sim.execute()
        self.assertEqual(self.sim.running, False)

    def test_store(self):
        self.sim.accumulator = 99
        self.sim.memory[0] = 2105  # STORE 5
        self.sim.execute()
        self.assertEqual(self.sim.memory[5], 99)

    def test_halt(self):
        self.sim.memory[0] = 4300  # HALT
        self.sim.execute()
        self.assertEqual(self.sim.running, False)

    def test_multiply(self):
        self.sim.accumulator = 5
        self.sim.memory[5] = 4
        self.sim.memory[0] = 3305  # MULTIPLY 5
        self.sim.execute()
        self.assertEqual(self.sim.accumulator, 20)

    def test_branch(self):
        self.sim.memory[0] = 4005  # BRANCH 5
        self.sim.memory[5] = 4300  # HALT
        self.sim.execute()
        self.assertEqual(self.sim.instruction_counter, 5)

    def test_branchneg(self):
        self.sim.accumulator = -1
        self.sim.memory[0] = 4105  # BRANCHNEG 5
        self.sim.memory[5] = 4300  # HALT
        self.sim.execute()
        self.assertEqual(self.sim.instruction_counter, 5)

    def test_branchzero(self):
        self.sim.accumulator = 0
        self.sim.memory[0] = 4205  # BRANCHZERO 5
        self.sim.memory[5] = 4300  # HALT
        self.sim.execute()
        self.assertEqual(self.sim.instruction_counter, 5)

    def test_invalid_opcode(self):
        self.sim.memory[0] = 9999  # Invalid opcode
        self.sim.execute()
        self.assertEqual(self.sim.running, False)

    def test_memory_bounds(self):
        self.sim.memory[0] = 2099  # Try to access memory location 99
        self.sim.execute()
        self.assertEqual(self.sim.accumulator, 0)  # Should load 0 from empty memory
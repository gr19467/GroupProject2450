import tkinter as tk
from tkinter import filedialog,messagebox
import unittest

# === PM (Cortland) ===
# TODO: Oversee project progress, ensure SRS collection and final merge.
# TODO: Manage GitHub branches and final submission.
# TODO: Coordinate with team for code integration.

# === DEV 2 (Gaby) ===
# TODO: Refactor UVSim to support GUI integration (decouple input/output).
# TODO: Ensure all logic is modular and supports event-driven GUI interactions.

class UVSim:
    def __init__(self):
        self.memory = [0] * 100  # 100-word memory
        self.accumulator = 0  # Single register
        self.instruction_counter = 0  # Program counter
        self.running = True
        self.input_value = None # Store input for GUI integration
        self.output = [] # Store output for GUI retrieval

    def set_input_value(self, value):
        """Sets input value for the next READ operation"""
        self.input_value = value

    def get_output(self):
        """Returns all output stored"""
        return self.output

    def load_program(self, filename):
        """Loads a program from a file into memory"""
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if int(line.strip()) == -99999:
                    break
                self.memory [i] = int(line.strip())

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
                self.output.append(f"Error: Unknown opcode {opcode} at address {self.instruction_counter}")
                self.running = False
                break

            self.instruction_counter += 1

class UVSimGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("UVSim GUI")
        self.sim=UVSim()

        self.file_label=tk.Label(root,text="Program File:")
        self.file_label.pack(pady=5)

        self.file_entry = tk.Entry(root, width=40)
        self.file_entry.pack(pady=5)
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)
        
                # Input field for READ operation
        self.input_label = tk.Label(root, text="Input Value (for READ operation):")
        self.input_label.pack(pady=5)
        
        self.input_entry = tk.Entry(root, width=20)
        self.input_entry.pack(pady=5)

          # Run button
        self.run_button = tk.Button(root, text="Run Program", command=self.run_program)
        self.run_button.pack(pady=10)

        # Output display
        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack(pady=5)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=5)

    def browse_file(self):
        filename=filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
        if filename:
            self.file_entry.delete(0,tk.END)
            self.file_entry.insert(0,filename)

    def run_program(self):
        self.output_text.delete(1.0,tk.END)
        filename=self.file_entry.get()
        if not filename:
            messagebox.showerror("Error","Please select a program file.")
            return

        try:
            self.sim.load_program(filename)
        except Exception as e:
            messagebox.showerror("Error", f"failed to load program: {e}")
            return
        input_value=self.input_entry.get()
        if input_value:
            try:
                self.sim.set_input_value(int(input_value))
            except ValueError:
                messagebox.showerror("Error","Input value must be an integer.")
                return
            self.sim.execute()
            output=self.sim.get_output()
            for line in output:
                self.output_text.insert(tk.END,f"{line}\n")

if __name__ == "__main__":
    # === DEV 1 (Jonah) ===
    # TODO: Replace command-line input/output with GUI elements.
    # TODO: Create input fields for loading files and displaying memory state.
    # TODO: Integrate 'Run Program' button to trigger UVSim execution.
    root=tk.Tk()
    gui=UVSimGUI(root)
    root.mainloop()

# === DEV 3 (James) ===
# TODO: Expand unit tests to include GUI interactions.
# TODO: Lead SRS documentation and ensure team follows functional requirements.

# validate() function - Jonah
def validate():
    input_value = gui.input_entry.get()
    if input_value:
        try:
            int(input_value)
            return True
        except ValueError:
            messagebox.showerror("Error", "Input value must be an integer.")
            return False
    return True

class TestUVSim(unittest.TestCase):
    def setUp(self):
        self.sim = UVSim()
        self.root = tk.Tk()
        self.gui = UVSimGUI(self.root)

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
    
    def test_gui_browse(self):
        self.gui.file_entry.insert(0, "Test1.txt")
        filename = self.gui.file_entry.get()
        self.assertEqual(filename, "Test1.txt")

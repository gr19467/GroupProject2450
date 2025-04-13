import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import unittest

# === Scrum Master (Gaby) ===
# TODO Update design document to reflect changes
# TODO Update unit tests, use cases, requirements
# TODO Update README.md

# === James ===
# Memory Expansion and Addressing
# TODO Modify internal memory to 250 lines (000-250)
# TODO Update memory validation to reject addresses outside range
# TODO Ensure application can handle six digit math operations correctly

# === Cortland ===
# From 4 to 6 digits
# TODO Implement support for 6-digit word format files
# TODO Implement a converter from 4 to 6 digits
# TODO Prevent mixing formats within a file

# === Jonah ===
# File and GUI changes
# TODO Design and implement a way to handle multiple files in the same app instance (GUI tabs)
# TODO Allow editing, switching, and running each file independently
# TODO Ensure file maximum of 250 lines
# TODO Fix teacher comment from last milestone:
# (3) -5 I have trouble repeating this function on my computer.
# "The client wants to be able to save and load files from any user-specified folder
# (not just a fixed default system folder)."

class UVSim:
    def __init__(self):
        self.memory = [0] * 250  # 100-word memory
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

    def load_program(self, code_text):
        """Loads and validates a 4-digit or 6-digit program into memory"""
        lines = code_text.strip().split("\n")

        if len(lines) > 250:
            self.output.append("Error: Too many lines. Max is 250.")
            self.running = False
            return

        digit_format = None  # Track if it's 4 or 6 digit format

        for i, line in enumerate(lines):
            line = line.strip()
            if line == "":
                continue
            if line == "-99999" or line == "-099999":  # handle both format endings
                break

            if not line.lstrip("+-").isdigit():
                self.output.append(f"Error: Invalid numeric input at line {i+1}: {line}")
                self.running = False
                return

            # Determine and lock file format
            if digit_format is None:
                digit_format = len(line)
            elif len(line) != digit_format:
                self.output.append(f"Error: Mixed formats detected at line {i+1}.")
                self.running = False
                return

            if digit_format == 4:
                self.memory[i] = int(line)
            elif digit_format == 6:
                self.memory[i] = int(line)
            else:
                self.output.append(f"Error: Unsupported instruction length at line {i+1}.")
                self.running = False
                return

    def execute(self):
        """Executes instructions in memory."""
        while self.running:
            instruction = self.memory[self.instruction_counter]
            opcode, operand = divmod(instruction, 10000)

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
        self.primary_color = "#4C721D"
        self.alt_color = "#FFFFFF"
        self.root.configure(bg=self.primary_color)
        self.sim=UVSim()

        self.file_label=tk.Label(root,text="Program File:", bg=self.primary_color)
        self.file_label.pack(pady=5)

        self.file_entry = tk.Entry(root, width=40)
        self.file_entry.pack(pady=5)
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, bg=self.alt_color)
        self.browse_button.pack(pady=5)
        
                # Input field for READ operation
        self.input_label = tk.Label(root, text="Input Value (for READ operation):", bg=self.primary_color)
        self.input_label.pack(pady=5)
        
        self.input_entry = tk.Entry(root, width=20)
        self.input_entry.pack(pady=5)

        # Add Code Editor Textbox
        self.editor_label = tk.Label(root, text="Code Editor:", bg=self.primary_color)
        self.editor_label.pack(pady=5)

        # Frame for Text + Scrollbar
        editor_frame = tk.Frame(root)
        editor_frame.pack(pady=5)

        self.code_editor = tk.Text(editor_frame, height=15, width=50, wrap=tk.NONE)
        self.code_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_y = tk.Scrollbar(editor_frame, orient=tk.VERTICAL, command=self.code_editor.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.code_editor.config(yscrollcommand=scrollbar_y.set)

          # Run button
        self.run_button = tk.Button(root, text="Run Program", command=self.run_program, bg=self.alt_color)
        self.run_button.pack(pady=10)

        # Output display
        self.output_label = tk.Label(root, text="Output:", bg=self.primary_color)
        self.output_label.pack(pady=5)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=5)
        
        #Button to change primary color
        self.primary_color_button = tk.Button(root, text="Change Primary Color", command=self.change_primary_color, bg=self.alt_color)
        self.primary_color_button.pack(pady=(10, 1))
        
        #Button to change alternate color
        self.alt_color_button = tk.Button(root, text="Change Alternate Color", command=self.change_alt_color, bg=self.alt_color)
        self.alt_color_button.pack(pady=10)

        self.convert_button = tk.Button(root, text="Convert 4→6 Digits", command=self.convert_4_to_6, bg=self.alt_color)
        self.convert_button.pack(pady=5)

    def browse_file(self):
        filename=filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
        if filename:
            self.file_entry.delete(0,tk.END)
            self.file_entry.insert(0,filename)
            with open(filename, 'r') as file:
                content = file.read()
                self.code_editor.delete(1.0, tk.END)
                self.code_editor.insert(tk.END, content)

    def convert_4_to_6(self):
        """Converts 4-digit lines in the code editor to 6-digit lines"""
        lines = self.code_editor.get("1.0", tk.END).strip().split("\n")
        converted_lines = []

        for line in lines:
            line = line.strip()
            if line == "":
                continue
            if line == "-99999":
                converted_lines.append("-099999")
                continue
            if not line.lstrip("+-").isdigit():
                messagebox.showerror("Error", f"Invalid instruction: {line}")
                return
            if len(line) != 4:
                messagebox.showerror("Error", f"Line is not 4-digit: {line}")
                return

            sign = "+" if not line.startswith("-") else "-"
            number = line.lstrip("+-")
            converted_lines.append(f"{sign}00{number}")

        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, "\n".join(converted_lines))
        messagebox.showinfo("Success", "File converted to 6-digit format.")

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
    
    def change_primary_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color:
            self.primary_color = color[1]
            self.root.configure(bg=self.primary_color)
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.config(bg=self.primary_color)
    
    def change_alt_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color:
            self.alt_color = color[1]
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(bg=self.alt_color)

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

if __name__ == "__main__":
    root=tk.Tk()
    gui=UVSimGUI(root)
    root.mainloop()

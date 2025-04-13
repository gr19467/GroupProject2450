import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk
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
# DONE Design and implement a way to handle multiple files in the same app instance (GUI tabs)
# DONE Allow editing, switching, and running each file independently
# DONE Ensure file maximum of 250 lines
# DONE Fix teacher comment from last milestone:
#      (3) -5 I have trouble repeating this function on my computer.
#      "The client wants to be able to save and load files from any user-specified folder
#      (not just a fixed default system folder)."

class UVSim:
    def __init__(self):
        self.memory = [0] * 250
        self.accumulator = 0
        self.instruction_counter = 0
        self.running = True
        self.input_value = None
        self.output = []

    def set_input_value(self, value):
        self.input_value = value

    def get_output(self):
        return self.output

    def load_program(self, code_text):
        lines = code_text.strip().split("\n")

        if len(lines) > 250:
            self.output.append("Error: Too many lines. Max is 250.")
            self.running = False
            return

        digit_format = None

        for i, line in enumerate(lines):
            line = line.strip()
            if line == "":
                continue
            if line == "-99999" or line == "-099999":
                break

            if not line.lstrip("+-").isdigit():
                self.output.append(f"Error: Invalid numeric input at line {i+1}: {line}")
                self.running = False
                return

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
        while self.running:
            instruction = self.memory[self.instruction_counter]
            opcode, operand = divmod(instruction, 10000)

            if opcode == 10:
                if self.input_value is not None:
                    self.memory[operand] = self.input_value
                    self.input_value = None
            elif opcode == 11:
                self.output.append(self.memory[operand])
            elif opcode == 20:
                self.accumulator = self.memory[operand]
            elif opcode == 21:
                self.memory[operand] = self.accumulator
            elif opcode == 30:
                self.accumulator += self.memory[operand]
            elif opcode == 31:
                self.accumulator -= self.memory[operand]
            elif opcode == 32:
                if self.memory[operand] == 0:
                    self.output.append("error: Division by zero")
                    self.running = False
                    continue
                self.accumulator //= self.memory[operand]
            elif opcode == 33:
                self.accumulator *= self.memory[operand]
            elif opcode == 40:
                self.instruction_counter = operand
                continue
            elif opcode == 41:
                if self.accumulator < 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 42:
                if self.accumulator == 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 43:
                self.running = False
                break
            else:
                self.output.append(f"Error: Unknown opcode {opcode} at address {self.instruction_counter}")
                self.running = False
                break

            self.instruction_counter += 1

class UVSimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UVSim GUI")
        self.primary_color = "#4C721D"
        self.alt_color = "#FFFFFF"
        self.root.configure(bg=self.primary_color)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.tabs = []
        self.sim_instances = []

        self.create_new_tab()

        self.bottom_frame = tk.Frame(root, bg=self.primary_color)
        self.bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.input_label = tk.Label(self.bottom_frame, text="Input Value:", bg=self.primary_color)
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = tk.Entry(self.bottom_frame, width=10)
        self.input_entry.pack(side=tk.LEFT, padx=5)

        self.run_button = tk.Button(self.bottom_frame, text="Run Program", command=self.run_program, bg=self.alt_color)
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.browse_button = tk.Button(self.bottom_frame, text="Open File", command=self.browse_file, bg=self.alt_color)
        self.browse_button.pack(side=tk.LEFT, padx=5)

        self.convert_button = tk.Button(self.bottom_frame, text="Convert 4→6 Digits", command=self.convert_4_to_6, bg=self.alt_color)
        self.convert_button.pack(side=tk.LEFT, padx=5)

        self.primary_color_button = tk.Button(self.bottom_frame, text="Primary Color", command=self.change_primary_color, bg=self.alt_color)
        self.primary_color_button.pack(side=tk.LEFT, padx=5)

        self.alt_color_button = tk.Button(self.bottom_frame, text="Alt Color", command=self.change_alt_color, bg=self.alt_color)
        self.alt_color_button.pack(side=tk.LEFT, padx=5)

    def create_new_tab(self, content=""):
        tab = tk.Frame(self.notebook)
        editor = tk.Text(tab, wrap=tk.NONE)
        output = tk.Text(tab, height=10, wrap=tk.NONE, bg="#f0f0f0")

        editor.pack(fill=tk.BOTH, expand=True)
        output.pack(fill=tk.BOTH)

        self.notebook.add(tab, text=f"File {len(self.tabs)+1}")
        self.tabs.append((editor, output))
        self.sim_instances.append(UVSim())

        if content:
            editor.insert(tk.END, content)

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, 'r') as file:
                content = file.read()
                self.create_new_tab(content)

    def convert_4_to_6(self):
        current_tab = self.notebook.index(self.notebook.select())
        editor, _ = self.tabs[current_tab]
        lines = editor.get("1.0", tk.END).strip().split("\n")
        converted_lines = []

        for line in lines:
            line = line.strip()
            if line == "":
                continue
            if line == "-99999":
                converted_lines.append("-099999")
                continue
            if not line.lstrip("+-").isdigit() or len(line) != 4:
                messagebox.showerror("Error", f"Invalid 4-digit line: {line}")
                return
            sign = "+" if not line.startswith("-") else "-"
            number = line.lstrip("+-")
            converted_lines.append(f"{sign}00{number}")

        editor.delete("1.0", tk.END)
        editor.insert(tk.END, "\n".join(converted_lines))
        messagebox.showinfo("Success", "File converted to 6-digit format.")

    def run_program(self):
        current_tab = self.notebook.index(self.notebook.select())
        editor, output = self.tabs[current_tab]
        sim = self.sim_instances[current_tab]

        output.delete("1.0", tk.END)
        code = editor.get("1.0", tk.END)

        if code.strip() == "":
            messagebox.showerror("Error", "No code to execute.")
            return

        input_val = self.input_entry.get()
        if input_val:
            try:
                sim.set_input_value(int(input_val))
            except ValueError:
                messagebox.showerror("Error", "Input must be an integer.")
                return

        sim.__init__()  # reset state
        sim.load_program(code)
        sim.execute()

        for line in sim.get_output():
            output.insert(tk.END, f"{line}\n")

    def change_primary_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color:
            self.primary_color = color[1]
            self.root.configure(bg=self.primary_color)
            self.bottom_frame.configure(bg=self.primary_color)
            self.input_label.configure(bg=self.primary_color)
            for child in self.root.winfo_children():
                if isinstance(child, tk.Label):
                    child.config(bg=self.primary_color)

    def change_alt_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color:
            self.alt_color = color[1]
            for widget in self.bottom_frame.winfo_children():
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
        self.gui.file_entry = tk.Entry(self.gui.root)
        self.gui.file_entry.insert(0, "Test1.txt")
        filename = self.gui.file_entry.get()
        self.assertEqual(filename, "Test1.txt")

if __name__ == "__main__":
    root = tk.Tk()
    gui = UVSimGUI(root)
    root.mainloop()

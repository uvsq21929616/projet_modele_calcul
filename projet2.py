class RAM:
    def __init__(self, program):
        self.registers = {'i0': len(program), 'i1': 0} # dictionnaire des registres (i0 et i1)
        self.program = program # instructions du programme

    def execute(self):
        pc = 0  
        while pc < len(self.program):
            instruction = self.program[pc].split()
            opcode = instruction[0]
            if opcode == "ADD":
                self.ADD(instruction)
            elif opcode == "SUB":
                self.SUB(instruction)
            elif opcode == "MUL":
                self.MUL(instruction)
            elif opcode == "DIV":
                self.DIV(instruction)
            elif opcode == "JUMP":
                pc = int(instruction[1]) - 1 
            elif opcode == "JE":
                if self.registers[instruction[1]] == self.registers[instruction[2]]:
                    pc = int(instruction[3]) - 1
            elif opcode == "TERMINE":
                return
            pc += 1

    def ADD(self, instruction):
        self.registers[instruction[1]] += self.registers[instruction[2]]

    def SUB(self, instruction):
        self.registers[instruction[1]] -= self.registers[instruction[2]]

    def MUL(self, instruction):
        self.registers[instruction[1]] *= self.registers[instruction[2]]

    def DIV(self, instruction):
        self.registers[instruction[1]] //= self.registers[instruction[2]]


def read_program(filename, input_word):
    with open(filename, 'r') as file:
        instructions = [line.strip() for line in file.readlines()]
    instructions.insert(0, f'i1 {input_word}')  
    return instructions

program_data = read_program("fichier.txt", 1)
print(program_data)
ram = RAM(program_data)
ram.execute()
print(ram.registers)

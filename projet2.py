class RAM:
    def __init__(self, programme):
        self.pos = programme[0]['i0']
        self.registre = programme[0]
        self.instructions = programme[1]

    def order(self, instruction):
        #print(instruction)
        if 'ADD' in instruction:
            self.ADD(instruction)
        
        elif 'SUB' in instruction:
            self.SUB(instruction)

        elif 'MUL' in instruction:
            self.MUL(instruction)  

        elif 'DIV' in instruction:
            self.DIV(instruction)

        elif 'JUMP' in instruction  :
            self.JUMP(instruction)

        elif 'JE' in instruction:
            self.JE(instruction)

        elif 'JL' in instruction:
            self.JL(instruction)

        elif 'terminé' in instruction:
            self.termine(instruction)
        
        else:
            print('error')

    def ADD(self, instruction):
        print(instruction)
        txt = instruction
        print(txt)
        self.pos += 1
        self.order(self.instructions[self.pos])

    def SUB(self, instruction):
        print(instruction)
        self.pos += 1
        self.order(self.instructions[self.pos])

    def MUL(self, instruction):
        print(instruction)
        self.pos += 1
        self.order(self.instructions[self.pos])

    def DIV(self, instruction):
        print(instruction)
        self.pos += 1
        self.order(self.instructions[self.pos])

    def JUMP(self, instruction):
        print(instruction)
        self.pos += 1
        self.order(self.instructions[self.pos])

    def JE(self, instruction):
        print(instruction)
        self.pos += 1
        self.order(self.instructions[self.pos])

    def termine(self, instruction):
        print(instruction)
        self.pos += 1
        return self.registre
    


def read_program(fichier, mot):
    programme = [
        {'i0': 0, 'i1': mot},  # Register initialization
        []
    ]

    with open(fichier, 'r') as file: 
        for line in file:
            line = line.strip()  # Remove redundant line and the last character ('\n')
            programme[1].append(line)  # Append each instruction to the list inside programme
    return programme

programme = read_program("fichier.txt", 1)
print(programme)
ram = RAM(programme)
print(ram.instructions)
#print(ram.registre)
#print(ram.pos)
ram.order(ram.instructions[0])
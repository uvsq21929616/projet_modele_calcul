#!/usr/bin/env python


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
        #print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("ADD", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        #print(registres)
        if str.isdigit(registres[0]):
            if str.isdigit(registres[1]):
                result = int(registres[0])+int(registres[1])
                #print(result)
                self.registre[registres[2]] = result
                self.pos +=1
                #print(self.registre)
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) + self.registre[registres[1]]
                    #print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    #print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[1].replace("@", "")
                    index = self.registre[registres[1]]
                    clé = list(self.registre.keys())[index]
                    result = int(registres[0]) + self.registre[clé]
                    #print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    #print(self.registre)
        else:
            if str.isdigit(registres[1]):
                if '@' not in registres[0]:
                    result = int(self.registre[registres[0]])+int(registres[1])
                    #print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    #print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    result = int(self.registre[clé])+int(registres[1])
                    #print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    #print(self.registre)

            else:
                if '@' not in registres[0]:
                    if '@' not in registres[0]:
                        result = int(self.registre[registres[0]])+int(registres[1])
                        #print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        #print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[0].replace("@", "")
                        index = self.registre[registres[0]]
                        clé = list(self.registre.keys())[index]
                        result = int(self.registre[clé])+int(registres[1])
                        #print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        #print(self.registre)
                        result = int(self.registre[registres[0]])+int(registres[1])
                        #print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])

                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    if '@' not in registres[0]:
                        result = int(self.registre[registres[0]])+int(self.registre[clé])
                        #print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        #print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[0].replace("@", "")
                        index2 = self.registre[registres[0]]
                        clé2 = list(self.registre.keys())[index2]
                        result = int(self.registre[clé2])+int(self.registre[clé])
                        #print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        #self.order(self.instructions[self.pos])

    def SUB(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("SUB", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        if str.isdigit(registres[0]):
            if str.isdigit(registres[1]):
                result = int(registres[0])-int(registres[1])
                print(result)
                self.registre[registres[2]] = result
                self.pos +=1
                print(self.registre)
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) - self.registre[registres[1]]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[1].replace("@", "")
                    index = self.registre[registres[1]]
                    clé = list(self.registre.keys())[index]
                    result = int(registres[0]) - self.registre[clé]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)

        else:
            if str.isdigit(registres[1]):
                if "@" not in registres[0]:
                    result = int(self.registre[registres[0]])-int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[1]]
                    clé = list(self.registre.keys())[index]
                    result = int(self.registre[clé]) -int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
            else:
                if "@" not in registres[0]:
                    if "@" not in registres[1]:
                        result = int(self.registre[registres[0]]) - int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[1].replace("@", "")
                        index = self.registre[registres[1]]
                        clé = list(self.registre.keys())[index]
                        result = int(self.registre[registres[0]]) - int(self.registre[clé])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                else:
                    if "@" not in registres[1]:
                        registres[0].replace("@", "")
                        index = self.registre[registres[0]]
                        clé = list(self.registre.keys())[index]
                        result = int(self.registre[clé]) - int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[0].replace("@", "")
                        index = self.registre[registres[0]]
                        clé = list(self.registre.keys())[index]
                        registres[1].replace("@", "")
                        index2 = self.registre[registres[1]]
                        clé2 = list(self.registre.keys())[index]
                        result = int(self.registre[clé]) - int(self.registre[clé2])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])

    def MUL(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("MUL", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        if str.isdigit(registres[0]):
            if str.isdigit(registres[1]):
                result = int(registres[0])*int(registres[1])
                print(result)
                self.registre[registres[2]] = result
                self.pos +=1
                print(self.registre)
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) * self.registre[registres[1]]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[1].replace("@", "")
                    index = self.registre[registres[1]]
                    clé = list(self.registre.keys())[index]
                    result = int(registres[0]) * self.registre[clé]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)

        else:
            if str.isdigit(registres[1]):
                if "@" not in registres[0]:
                    result = int(self.registre[registres[0]])*int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[1]]
                    clé = list(self.registre.keys())[index]
                    result = int(self.registre[clé]) *int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
            else:
                if "@" not in registres[0]:
                    if "@" not in registres[1]:
                        result = int(self.registre[registres[0]]) * int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[1].replace("@", "")
                        index = self.registre[registres[1]]
                        clé = list(self.registre.keys())[index]
                        result = int(self.registre[registres[0]]) * int(self.registre[clé])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                else:
                    if "@" not in registres[1]:
                        registres[0].replace("@", "")
                        index = self.registre[registres[0]]
                        clé = list(self.registre.keys())[index]
                        result = int(self.registre[clé]) * int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[0].replace("@", "")
                        index = self.registre[registres[0]]
                        clé = list(self.registre.keys())[index]
                        registres[1].replace("@", "")
                        index2 = self.registre[registres[1]]
                        clé2 = list(self.registre.keys())[index]
                        result = int(self.registre[clé]) * int(self.registre[clé2])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])

    def DIV(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("DIV", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        if str.isdigit(registres[0]):
            if str.isdigit(registres[1]):
                result = int(registres[0]) // int(registres[1])
                print(result)
                self.registre[registres[2]] = result
                self.pos +=1
                print(self.registre)
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) // self.registre[registres[1]]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[1].replace("@", "")
                    index = self.registre[registres[1]]
                    clé = list(self.registre.keys())[index]
                    result = int(registres[0]) // self.registre[clé]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)

        else:
            if str.isdigit(registres[1]):
                if "@" not in registres[0]:
                    result = int(self.registre[registres[0]])// int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[1]]
                    clé = list(self.registre.keys())[index]
                    result = int(self.registre[clé]) // int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
            else:
                if "@" not in registres[0]:
                    if "@" not in registres[1]:
                        result = int(self.registre[registres[0]]) // int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[1].replace("@", "")
                        index = self.registre[registres[1]]
                        clé = list(self.registre.keys())[index]
                        result = int(self.registre[registres[0]]) // int(self.registre[clé])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                else:
                    if "@" not in registres[1]:
                        registres[0].replace("@", "")
                        index = self.registre[registres[0]]
                        clé = list(self.registre.keys())[index]
                        result = int(self.registre[clé]) // int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])
                    else:
                        registres[0].replace("@", "")
                        index = self.registre[registres[0]]
                        clé = list(self.registre.keys())[index]
                        registres[1].replace("@", "")
                        index2 = self.registre[registres[1]]
                        clé2 = list(self.registre.keys())[index]
                        result = int(self.registre[clé]) // int(self.registre[clé2])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        #self.order(self.instructions[self.pos])

    def JUMP(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("JUMP", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        self.pos += int(registres[0])
        #self.order(self.instructions[self.pos])

    def JE(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("JE", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        if registres[1].isdigit():
            if "@" not in registres[0]:
                if self.registre[registres[0]] == int(registres[1]):
                    #print(int(registres[2]))
                    self.pos += int(registres[2])
                    #print(self.pos)
                else:
                    self.pos +=1
                #self.order(self.instructions[self.pos])
            else:
                registres[0].replace("@", "")
                index = self.registre[registres[0]]
                clé = list(self.registre.keys())[index]
                if self.registre[clé] == int(registres[1]):
                    #print(int(registres[2]))
                    self.pos += int(registres[2])
                    #print(self.pos)
                else:
                    self.pos +=1
                #self.order(self.instructions[self.pos])
        else:
            if "@" not in registres[1]:
                if "@" not in registres[0]:
                    if self.registre[registres[0]] == self.registre[registres[1]]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        #print(self.pos)
                    else:
                        self.pos +=1
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    if self.registre[clé] == self.registre[registres[1]]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        #print(self.pos)
                    else:
                        self.pos +=1
                    #self.order(self.instructions[self.pos])
            else:
                registres[1].remplace("@", "")
                index2 = self.registre[registres[1]]
                clé2 = list(self.registre.keys())[index]
                if "@" not in registres[0]:
                    if self.registre[registres[0]] == self.registre[clé2]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        #print(self.pos)
                    else:
                        self.pos +=1
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    if self.registre[clé] == self.registre[clé2]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        #print(self.pos)
                    else:
                        self.pos +=1
                    #self.order(self.instructions[self.pos])

    def JL(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("JL", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        if "@" not in registres[0]:
            if self.registre[registres[0]] >= int(registres[1]):
                print(int(registres[2]))
                self.pos += int(registres[2])
                print(self.pos)
            else:
                self.pos +=1
        else:
            registres[0].replace("@", "")
            index = self.registre[registres[0]]
            clé = list(self.registre.keys())[index]
            if self.registre[clé] >= int(registres[1]):
                print(int(registres[2]))
                self.pos += int(registres[2])
                print(self.pos)
            else:
                self.pos +=1

        #self.order(self.instructions[self.pos])

    def termine(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        self.pos += 1
        return self.registre



def read_program(fichier, mots):
    #prend en entrée un fichier contenant le programme de la machine ram
    #et une liste contenant le ou les mots d'entrées contenus dans une liste

    #initialisation du programme
    programme = [
        {'i0': 0},  # initialise le registre
        []          # initialise le programme
    ]
    for i in range(len(mots)):
        programme[0]['i'+str(i+1)] = mots[i]
    print(programme[0])
    with open(fichier, 'r') as file: 
        for line in file:
            line = line.strip()  # enlève le caractère '\n'
            programme[1].append(line)  # ajoute chaque instruction au programme de la ram
    return programme


def etape_suivante(ram, config):
    # Prend en argument une machine RAM et une configuration [pos, registre]
    ram.pos = config[0]
    ram.registre = config[1]
    # Run one step
    ram.order(ram.instructions[ram.pos])
    # Return the updated position and register
    return [ram.pos, ram.registre]

def marche_ram(ram, mot):
    """
    fonction prenant en argument une marchine ram et un mot,
    rentrant le mot dans la machine ram et faisant fonctionner
    la machine jusqu'à exécution du programme."""
    ram.registre['i1'] = mot
    print("registre initial:", ram.registre)
    while True:
        current_instruction = ram.instructions[ram.pos]
        print("instruction:", current_instruction)
        if 'terminé' in current_instruction:
            print("Programme terminé.")
            break
        ram.order(current_instruction)
        print("registre mis à jour:", ram.registre)
        print("position mise à jour:", ram.pos)


programme = read_program("machine_a_puissance_b.txt", [2, 5])

ram = RAM(programme)

marche_ram(ram, 2)

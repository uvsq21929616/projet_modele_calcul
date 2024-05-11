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
                self.registre['i0'] = self.pos
                #print(self.registre)
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) + self.registre[registres[1]]
                    #print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos
                    #print(self.registre)
        else:
            if str.isdigit(registres[1]):
                if '@' not in registres[0]:
                    result = int(self.registre[registres[0]])+int(registres[1])
                    #print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos
                    #print(self.registre)

            else:
                if '@' not in registres[0]:
                    if '@' not in registres[0]:
                        result = int(self.registre[registres[0]])+int(registres[1])
                        #print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                self.registre['i0'] = self.pos
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) - self.registre[registres[1]]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos

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
                    self.registre['i0'] = self.pos
            else:
                if "@" not in registres[0]:
                    if "@" not in registres[1]:
                        result = int(self.registre[registres[0]]) - int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                self.registre['i0'] = self.pos
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) * self.registre[registres[1]]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos

        else:
            if str.isdigit(registres[1]):
                if "@" not in registres[0]:
                    result = int(self.registre[registres[0]])*int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos
            else:
                if "@" not in registres[0]:
                    if "@" not in registres[1]:
                        result = int(self.registre[registres[0]]) * int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                self.registre['i0'] = self.pos
                #self.order(self.instructions[self.pos])
            else:
                if '@' not in registres[1]:
                    result = int(registres[0]) // self.registre[registres[1]]
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos

        else:
            if str.isdigit(registres[1]):
                if "@" not in registres[0]:
                    result = int(self.registre[registres[0]])// int(registres[1])
                    print(result)
                    self.registre[registres[2]] = result
                    self.pos +=1
                    print(self.registre)
                    self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos
            else:
                if "@" not in registres[0]:
                    if "@" not in registres[1]:
                        result = int(self.registre[registres[0]]) // int(self.registre[registres[1]])
                        print(result)
                        self.registre[registres[2]] = result
                        self.pos +=1
                        print(self.registre)
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
                        self.registre['i0'] = self.pos
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
        self.registre['i0'] = self.pos
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
                    self.registre['i0'] = self.pos
                    #print(self.pos)
                else:
                    self.pos +=1
                    self.registre['i0'] = self.pos
                #self.order(self.instructions[self.pos])
            else:
                registres[0].replace("@", "")
                index = self.registre[registres[0]]
                clé = list(self.registre.keys())[index]
                if self.registre[clé] == int(registres[1]):
                    #print(int(registres[2]))
                    self.pos += int(registres[2])
                    self.registre['i0'] = self.pos
                    #print(self.pos)
                else:
                    self.pos +=1
                    self.registre['i0'] = self.pos
                #self.order(self.instructions[self.pos])
        else:
            if "@" not in registres[1]:
                if "@" not in registres[0]:
                    if self.registre[registres[0]] == self.registre[registres[1]]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    if self.registre[clé] == self.registre[registres[1]]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])
            else:
                registres[1].remplace("@", "")
                index2 = self.registre[registres[1]]
                clé2 = list(self.registre.keys())[index]
                if "@" not in registres[0]:
                    if self.registre[registres[0]] == self.registre[clé2]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    if self.registre[clé] == self.registre[clé2]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])

    def JL(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("JL", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        if registres[1].isdigit():
            if "@" not in registres[0]:
                if self.registre[registres[0]] <= int(registres[1]):
                    #print(int(registres[2]))
                    self.pos += int(registres[2])
                    self.registre['i0'] = self.pos
                    #print(self.pos)
                else:
                    self.pos +=1
                    self.registre['i0'] = self.pos
                #self.order(self.instructions[self.pos])
            else:
                registres[0].replace("@", "")
                index = self.registre[registres[0]]
                clé = list(self.registre.keys())[index]
                if self.registre[clé] <= int(registres[1]):
                    #print(int(registres[2]))
                    self.pos += int(registres[2])
                    self.registre['i0'] = self.pos
                    #print(self.pos)
                else:
                    self.pos +=1
                    self.registre['i0'] = self.pos
                #self.order(self.instructions[self.pos])
        else:
            if "@" not in registres[1]:
                if "@" not in registres[0]:
                    if self.registre[registres[0]] <= self.registre[registres[1]]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    if self.registre[clé] <= self.registre[registres[1]]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])
            else:
                registres[1].remplace("@", "")
                index2 = self.registre[registres[1]]
                clé2 = list(self.registre.keys())[index]
                if "@" not in registres[0]:
                    if self.registre[registres[0]] <= self.registre[clé2]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])
                else:
                    registres[0].replace("@", "")
                    index = self.registre[registres[0]]
                    clé = list(self.registre.keys())[index]
                    if self.registre[clé] <= self.registre[clé2]:
                        #print(int(registres[2]))
                        self.pos += int(registres[2])
                        self.registre['i0'] = self.pos
                        #print(self.pos)
                    else:
                        self.pos +=1
                        self.registre['i0'] = self.pos
                    #self.order(self.instructions[self.pos])

    def termine(self, instruction):
        print(instruction)
        print(self.pos, self.registre)
        self.pos += 1
        self.registre['i0'] = self.pos
        return self.registre


class RAM_AUTOMATE(RAM):
    def __init__(self, programme):
        super().__init__(programme)

    
    def order(self, instruction):
        if "FIND" in instruction:
            self.FIND(instruction)
        elif "ADD" in instruction:
            self.ADD(instruction)
        elif "JE" in instruction:
            self.JE(instruction)
        elif "JUMP" in instruction:
            self.JUMP(instruction)
        elif "motreconnu" in instruction:
            self.termine(instruction)
        elif "nonreconnu" in instruction:
            self.nonreconnu(instruction)

    def FIND(self, instruction):
        print(instruction)
        #print(self.pos, self.registre)
        self.pos += 1
        txt = instruction
        txt = txt.replace("ADD", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        lettre_mot = self.registre['i1'][0]
        lettre_pile = self.registre['i2'][-1]
        etat = self.registre['i3']
        index1 = 7
        index2 = 8
        index3 = 9
        i = 0
        while True:
            if (index2) > len(self.registre.keys()):
                    print("ereur ! transition pas dans l'automate!")
                    break
            else:
                if self.registre['i'+str(index1)] == etat:
                    if  self.registre['i'+str(index2)] == lettre_mot and self.registre['i'+str(index3)] == lettre_pile:
                        self.registre['i4'] = self.registre['i'+str(index3+1)]
                        self.registre['i5'] = self.registre['i'+str(index3+2)]
                        print(lettre_mot, lettre_pile, self.registre['i'+str(index1)], self.registre['i'+str(index2)]), 
                        break
                    else: 
                        index1 += 5
                        index2 += 5
                        index3 += 5
                else: 
                    index1 += 5
                    index2 += 5
                    index3 += 5
            

    def ADD(self, instruction):
        print(instruction)
        self.pos += 1
        #print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("ADD", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        for lettre in self.registre[registres[1]]:
            if lettre == '1':
                self.registre['i2'] += '1'
            elif lettre == '2':
                self.registre['i2'] = self.registre['i2'][:-1]
        self.registre['i3'] = self.registre['i5']
        self.registre['i1'] = self.registre['i1'][1:]

    def JE(self, instruction):
        print(instruction)
        self.pos += 1
        #print(self.pos, self.registre)
        txt = instruction
        txt = txt.replace("JE", "") 
        txt = txt[1:-1]
        registres = txt.split(",")
        print(registres)
        if self.registre[registres[0]] == registres[1]:
            self.pos += int(registres[2])
        else:
            self.pos += 1

    def nonreconnu(self, instruction):
        self.pos += 1
        print("mot non reconnu")
        return self.registre
    
    def termine(self, instruction):
        self.pos += 1
        print("motreconnu")
        return self.registre
    


#### Simulaltion
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
        if 'terminé' in current_instruction or "motreconnu" in current_instruction:
            print("Programme terminé.")
            break
        ram.order(current_instruction)
        print("registre mis à jour:", ram.registre)
        print("position mise à jour:", ram.pos)


"""programme = read_program("machine_a_puissance_b.txt", [2, 5])
ram = RAM(programme)
marche_ram(ram, 2)"""

tableau = [5, 3, 1, 4, 2]
programme = read_program("machine_tri_bulles.txt", tableau)
ram = RAM(programme)
marche_ram(ram, 5)
tableau_trié = []
for elem in list(ram.registre.keys())[1:6]:
    tableau_trié.append(ram.registre[elem])
print("Tableau trié :", tableau_trié)

### Automates à piles
def lire_automate(liste_transition, mot, fichier):
    """
    une transition de la liste ressemble à ceci:
    - état initial
    - lettre lue
    - lettre du dessus de la pile
    - lettre à écrire sur la pile
    - etat final
    """
    registre = {
        'i0': 0, # correspond à la position dans la machine ram
        'i1': str(mot), # correspond au mot qu'on lit
        'i2': '0', # correspond à la pile
        'i3': '0', # correspond à l'état
        'i4': '0', # correspond à la lettre à ajouter sur la pile : 1, on empile 1, 2, on dépile 1
        'i5': '0', #correspond à l'état suivant
        'i6': len(liste_transition) # correspond au nombre de transitions
    }
    #print(len(liste_transition))
    index = 7
    for transition in liste_transition: # on ajoute chaque élément des transitions au registre
        #print(transition)
        for elem in transition:
            i = 'i'+str(index)
            registre[i] =str(elem)
            index += 1
    programme = [registre, []]
    with open(fichier, "r") as file:
        for line in file:
            line = line.strip()
            programme[1].append(line)
    return programme


def marche_automate(ram):
    print("registre initial:", ram.registre)
    while True:
        current_instruction = ram.instructions[ram.pos]
        print("instruction:", current_instruction)
        if "motreconnu" in current_instruction:
            print("Programme terminé.")
            break
        ram.order(current_instruction)
        print("registre mis à jour:", ram.registre)
        print("position mise à jour:", ram.pos)

#print(lire_automate([[0, 1, 0, 2, 1, 1, 1], [0, 1, 1, 2, 1, 1, 0]], 0, "automate_a_pile.txt"))

"""programme_automate = lire_automate([[0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 2, 2], [2, 0, 1, 2, 2], [2, '', 0, 0, 1]], 111000, "automate_a_pile.txt")
ram_automate = RAM_AUTOMATE(programme_automate)
print(ram_automate.instructions)
print(ram_automate.registre)
print(ram_automate)
marche_automate(ram_automate)
etape_suivante(ram_automate, [2, {'i0': 0, 'i1': 0, 'i2': 0, 'i3': 0, 'i4': 0, 'i5': 0, 'i6': 1, 'i7': 0, 'i8': 2, 'i9': 1, 'i10': 1, 'i11': 1, 'i12': 0, 'i13': 1, 'i14': 1, 'i15': 2, 'i16': 1, 'i17': 1, 'i18': 0}])
print(ram_automate.pos)"""

#### Optimisation
def graphe_ram(fichier):
    programme = []
    with open(fichier, 'r') as file: 
        for line in file:
            line = line.strip()  # enlève le caractère '\n'
            programme.append(line)  # ajoute chaque instruction au programme de la ram
    successeurs = {}
    for instruction in programme:
        successeurs[instruction] = []
    for i in range(len(programme)):
        if 'JE' not in programme[i] and 'JUMP' not in programme[i] and 'JL' not in programme[i] and "terminé" not in programme[i]:
            successeurs[programme[i]].append(programme[i+1])
        elif 'terminé' in programme[i]:
            print(successeurs)
            return successeurs
        elif 'JUMP' in programme[i]:
            txt = programme[i]
            txt = txt.replace("JUMP", "")
            txt = txt.replace("(", "")
            txt = txt.replace(")", "")
            print(txt)
            successeurs[programme[i]].append(programme[i+int(txt)])
        elif 'JE' in programme[i]:
            txt = programme[i]
            txt = txt.replace("JE", "")
            txt = txt.replace("(", "")
            txt = txt.replace(")", "")
            txt = txt.split(",")
            successeurs[programme[i]].append(programme[i+1])
            successeurs[programme[i]].append(programme[i+int(txt[2])])

        elif 'JL' in programme[i]:
            txt = programme[i]
            txt = txt.replace("JL", "")
            txt = txt.replace("(", "")
            txt = txt.replace(")", "")
            txt = txt.split(",")
            successeurs[programme[i]].append(programme[i+1])
            successeurs[programme[i]].append(programme[i+int(txt[2])])    
    return successeurs

def code_mort_ram(fichier):
    successeurs = graphe_ram(fichier)
    programme = []
    with open(fichier, "r") as f_in, open("code_nettoyé.txt", "w") as f_out:
        for line in f_in:
            line = line.strip()  # enlève le caractère '\n'
            programme.append(line)  # ajoute chaque instruction au programme de la ram
        f_out.write(programme[0])
        print(programme[0])
        f_out.write("\n")
        print(successeurs.values())
        for instruction in programme[1:]:
            i = 0
            for value in successeurs.values():
                if instruction in value:
                    print(instruction)
                    i = 1
            if i == 0:
                print(instruction + " code mort")
            if i == 1:
                f_out.write(instruction)
                f_out.write("\n")

def combiner_instruction(fichier):
    successeurs = graphe_ram(fichier)
    programme = []
    with open(fichier, "r") as f_in, open("code_combiné.txt", "w") as f_out:
        for line in f_in:
            line = line.strip()  # enlève le caractère '\n'
            programme.append(line)  # ajoute chaque instruction au programme de la ram
        print(programme)
        for i, instruction in enumerate(programme):
            print(successeurs[programme[i]])
            if len(successeurs[programme[i]]) ==  1:
                print(programme[i], successeurs[programme[i]][0])
                if "ADD" in programme[i] and "ADD" in successeurs[programme[i]][0]:
                    txt1 = programme[i]
                    txt1 = txt1.replace("ADD(","")
                    txt1 = txt1.replace(")","")
                    txt1 = txt1.split(",")
                    print(txt1)
                    txt2 = successeurs[programme[i]][0]
                    txt2 = txt2.replace("ADD(","")
                    txt2 = txt2.replace(")","")
                    txt2 = txt2.split(",")
                    print(txt2)
                    if txt1[2] == txt2[2]:
                        if txt2[0].isdigit():
                            programme.remove(programme[i])
                        elif txt2[0] != txt2[2]:
                            pass
                        else:
                            if txt1[0].isdigit():
                                result = int(txt1[0]) + int(txt1[1]) +int(txt2[1])
                                print(result)
                                txt = "ADD(0,"+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = txt
                                del(programme[i+1])
                            else:
                                result = int(txt1[1]) + int(txt2[1])
                                print(result)
                                txt = "ADD("+txt2[0]+","+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = [txt]
                                del(programme[i+1])

                if "SUB" in programme[i] and "SUB" in successeurs[programme[i]][0]:
                    txt1 = programme[i]
                    txt1 = txt1.replace("SUB(","")
                    txt1 = txt1.replace(")","")
                    txt1 = txt1.split(",")
                    print(txt1)
                    txt2 = successeurs[programme[i]][0]
                    txt2 = txt2.replace("SUB(","")
                    txt2 = txt2.replace(")","")
                    txt2 = txt2.split(",")
                    print(txt2)
                    if txt1[2] == txt2[2]:
                        if txt2[0].isdigit():
                            programme.remove(programme[i])
                        elif txt2[0] != txt2[2]:
                            pass
                        else:
                            if txt1[0].isdigit():
                                result = int(txt1[0]) - int(txt1[1]) - int(txt2[1])
                                print(result)
                                txt = "SUB(0,"+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = txt
                                del(programme[i+1])
                            else:
                                result = int(txt1[1]) + int(txt2[1])
                                print(result)
                                txt = "SUB("+txt2[0]+","+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = txt
                                del(programme[i+1])
                if "MUL" in programme[i] and "MUL" in successeurs[programme[i]][0]:
                    txt1 = programme[i]
                    txt1 = txt1.replace("MUL(","")
                    txt1 = txt1.replace(")","")
                    txt1 = txt1.split(",")
                    print(txt1)
                    txt2 = successeurs[programme[i]][0]
                    txt2 = txt2.replace("MUL(","")
                    txt2 = txt2.replace(")","")
                    txt2 = txt2.split(",")
                    print(txt2)
                    if txt1[2] == txt2[2]:
                        if txt2[0].isdigit():
                            programme.remove(programme[i])
                        elif txt2[0] != txt2[2]:
                            pass
                        else:
                            if txt1[0].isdigit():
                                result = int(txt1[0]) * int(txt1[1]) * int(txt2[1])
                                print(result)
                                txt = "MUL(0,"+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = txt
                                del(programme[i+1])
                            else:
                                result = int(txt1[1]) + int(txt2[1])
                                print(result)
                                txt = "MUL("+txt2[0]+","+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = txt
                                del(programme[i+1])
                if "DIV" in programme[i] and "DIV" in successeurs[programme[i]][0]:
                    txt1 = programme[i]
                    txt1 = txt1.replace("DIV(","")
                    txt1 = txt1.replace(")","")
                    txt1 = txt1.split(",")
                    print(txt1)
                    txt2 = successeurs[programme[i]][0]
                    txt2 = txt2.replace("DIV(","")
                    txt2 = txt2.replace(")","")
                    txt2 = txt2.split(",")
                    print(txt2)
                    if txt1[2] == txt2[2]:
                        if txt2[0].isdigit():
                            programme.remove(programme[i])
                        elif txt2[0] != txt2[2]:
                            pass
                        else:
                            if txt1[0].isdigit():
                                result = int(txt1[0]) * int(txt1[1]) * int(txt2[1])
                                print(result)
                                txt = "DIV(0,"+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = txt
                                del(programme[i+1])
                            else:
                                result = int(txt1[1]) * int(txt2[1])
                                print(result)
                                txt = "DIV("+txt2[0]+","+str(result)+","+txt2[2]+")"
                                print(txt)
                                programme[i] = txt
                                del(programme[i+1])
        for i in range(len(programme)-1):
                f_out.write(programme[i])
                f_out.write("\n")
        f_out.write(programme[-1])
    print(programme)

"""code_mort_ram("fichier.txt")
combiner_instruction("machine_a_puissance_b.txt")
"""
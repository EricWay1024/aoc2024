lines = open("../input/17.in").read().split('\n')

class Computer:
    def __init__(self, reg_a, reg_b, reg_c, program):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.program = program
        self.pointer = 0
        self.output = []
    
    def combo_operand(self, i):
        if 0 <= i <= 3:
            return i 
        if i == 4:
            return self.reg_a
        if i == 5:
            return self.reg_b
        if i == 6:
            return self.reg_c
        
        raise ValueError("Invalid combo operand.")
    
    def do(self, opcode, operand):
        new_pointer = self.pointer + 2
        if opcode in [0, 6, 7]:
            a = self.reg_a
            b = 1 << self.combo_operand(operand)
            z = a // b
            if opcode == 0:
                self.reg_a = z
            elif opcode == 6:
                self.reg_b = z
            else:
                self.reg_c = z
        elif opcode == 1:
            self.reg_b ^= operand
        elif opcode == 2:
            self.reg_b = self.combo_operand(operand) % 8
        elif opcode == 3:
            if self.reg_a != 0:
                new_pointer = operand
        elif opcode == 4:
            self.reg_b ^= self.reg_c
        elif opcode == 5:
            self.output.append(self.combo_operand(operand) % 8)
        
        self.pointer = new_pointer
    
    def run(self):
        while self.pointer < len(self.program):
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            self.do(opcode, operand)

    def result(self):
        return ",".join(map(str, self.output))


program = [2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0]

c = Computer(
    reg_a=45483412,
    reg_b=0,
    reg_c=0,
    program=program
)

c.run()
print(c.result())

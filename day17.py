from typing import List
 
def computer(registers, program) -> list[int]:
    a,b,c = registers
    output = []
    pointer = 0
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        match opcode:
            case 0:
                value = operand if operand <= 3 else [a,b,c][operand-4]
                a = a >> value   
            case 1:
                b = b ^ operand
            case 2:
                value = operand if operand <= 3 else [a,b,c][operand-4]
                b = value % 8
            case 3:
                if a != 0:
                    pointer = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                value = operand if operand <= 3 else [a,b,c][operand-4]
                output.append(value % 8)
            case 6:
                value = operand if operand <= 3 else [a,b,c][operand-4]
                b = a >> value
            case 7:
                value = operand if operand <= 3 else [a,b,c][operand-4]
                c = a >> value
        pointer += 2
    return output

def main():
    #example
    # registers,program = [729,0,0],[0,1,5,4,3,0]
    # print(f"Example output: {",".join(map(str,computer(registers, program)))}") #4,6,3,5,6,3,5,2,1,0
    # #part 1
    registers,program = [48744869,0,0],[2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0]
    output = computer(registers, program)
    print(f"Part 1: {",".join(map(str,output))}")

    #part 2
    candidates = [0]
    #program = [0,3,5,4,3,0] - testing
    program = [2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0]
    for l in range(len(program)):
        next_candidates = []
        for value in candidates:
            for i in range(8):
                target = (value << 3) + i
                if computer([target,0,0], program) == program[-l-1:]:
                    next_candidates.append(target)
        candidates = next_candidates
    part_2 = candidates
    print(f"Part 2: {min(part_2)}")      


if __name__ == '__main__':
    main()

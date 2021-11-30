dict = {
  "NOP": "0000",
  "HALT": "0600",
  "LDR": "0001000",
  "STR": "0001100",
  "ADD": "0010000",
  "SUB": "0010001",
  "MUL": "0010010",
  "MULU": "0010011",
  "DIV": "0010100",
  "MOD": "0010101",
  "AND": "0010110",
  "OR": "0010111",
  "EOR": "0011000",
  "NOT": "0011001",
  "LSL": "0011010",
  "LSR": "0011011",
  "ASR": "0011100",
  "ROL": "0011101",
  "ROR": "0011110",
  "MOVIm": "1",
  "MOV": "0000100",
  "MOVF": "0000101",
  "BEQ": "0110",
  "BNE": "0111",
  "B": "0100",
  "R0": "000",
  "R1": "001",
  "R2": "010",
  "R3": "011",
  "R4": "100",
  "R5": "101",
  "R6": "110",
  "R7": "111",
  "Flags": "000000"
}

def checkInt(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()

instructions = open("program.txt","r")
output = open("output.txt","w+")
LIST = open("LIST.lst","w+")

lines = instructions.readlines()

for line in lines:
  line = line.strip()
  args = line.split()

  if(args[0] == ';'):
    output.write(line+'\n')
    continue

  inst = args[0]
  try:
    a1 = args[1]
  except:
    a1 = -1
  try:
    a2 = args[2]
  except:
    a2 = -1
  try:
    a3 = args[3]
  except:
    a3 = -1
  
  if(inst == "NOP" or inst == "HALT"): #NOP or HALT
    output.write(dict[inst]+'\n')
    continue
  elif(checkInt(a1)): # Branch instructions
    instruction = dict[inst] + str(format(int(a1) & 0xfff, '012b'))
  elif(inst == "MOV" and checkInt(a2)): # MOV with immediate
    instruction = dict["MOVIm"] + dict[a1] + str(format(int(a2) & 0xfff, '012b'))
  elif(inst == "MOV" and a2 == "Flags"):# MOV flags
    instruction = dict["MOVF"] + "000" + dict[a1] + "000"
  elif(inst == "MOV"): # Basic MOV and 2 registers
    instruction = dict["MOV"] + dict[a2] + dict[a1] + "000"
  else: # ALU, LDR, and STR instructions are last
    instruction = dict[inst] + dict[a2] + dict[a1]
    if(a3!=-1):
      instruction += dict[a3]
    else: # NOT instruction
      instruction += "000"


  hexInst = hex(int(instruction, base=2))

  
  output.write(hexInst[2:].zfill(4)+'\n')

  print(args)
  print("Binary: "+instruction)
  print("Hex: "+hexInst[2:].zfill(4))
  

output.close()
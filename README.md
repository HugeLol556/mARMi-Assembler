# mARMi Compiler
Compiles a set of instructions inspired by ARM for ECS154A cpu lab. 

**!Overwrites files!**

Reads assembly code written in program.txt and writes the machine code line by line in output.txt. This output can be copy pasted into Logisim ROM for execution

Seperate arguments by spaces and comments can be made on new lines using a semicolon and a space, which will be written in output.txt.

In line comments are supported after the machine code with a space and semicolons also

*Ex:* 
MOV R0 R0 ; Meaningless instruction

Immediates must be positive or negative decimal values that fit in a signed 12 bit value.

Creates an additional file called LIST.lst that formats the code as:  

; comments 

machine code; assembly; in line comments
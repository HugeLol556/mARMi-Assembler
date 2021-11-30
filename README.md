# mARMi Compiler
Compiles a set of instructions inspired by ARM for ECS154A cpu lab. 

The machine code written in program.txt and writes the assembly line by line in output.txt.

Seperate arguments by spaces and comments can be made on new lines using a semicolon and a space, which will be written in output.txt.

In line comments are supported after the machine code with semicolons also

Immediates must be positive or negative decimal values that fit in a signed 12 bit value.

Creates an additional file called LIST.lst that formats the code as:
; comments
machine code; assembly; in line comments
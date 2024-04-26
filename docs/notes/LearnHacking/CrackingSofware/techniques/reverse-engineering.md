# Reverse Engineering

## Introduction

Apps are usually packaged in binary files. User cannot really understand what binary files is doing because user cannot see the source code.

However, it's possible to understand part of it and break the app by changing a register or memory space.

Binary files also has its meaning. It's a file of 0s and 1s. The binary data are actually commands written in assembly.

All programming languages are eventually translated into assembly in order to be executed by CPU, even interpreted languages like Python and JavaScript.

We can translate 0 and 1s to assembly if we have the instruction set of the CPU. 

With the help of disassembler apps, we can easily visualize the assembly. We can even run debugger, set breakpoints and check memory used by the app.

The apps that require activation must use a conditional statements to check whether it's activated. Let's say the variable is `activated`.

In assembly code, the variable will be loaded to a register and compared with another register that has `True` as its value. 
If the conditional statement is evaluated to be true, the software will continue running, else stop.
All we need to do is to edit the register value to set it to `True`.


This is just the basic idea, it's also possible to prevent this.






## Related Topic: Buffer Overflow.

Disassembler can be used to exploit softwares' vulnerabilities. 

Buffer overflow is a technique that take advantage of vulnerabilities to populate memory space and make a hacked software run malicious code.

For example, in C language, when `strcpy` is used instead of `strncpy`, buffer overflow can occur if the allocated memory for destination variable is not enough to hold the source data.

Hackers can input malicious input data containing offsets and binary malicious code to pollute software's memory space. When the program executes the malicious assembly code, hackers could potentially get access to the attacked computer.

ASLR (Address space layout randomization) is designed to protect user and softwares from attack like buffer overflow. When memory is allocated randomly, it's hard to predict where to inject malicious code.


## Softwares

Softwares for reverse engineering are called disassembler.

- MacOS
	- [Hopper](https://www.hopperapp.com/)
- Linux
	- [Hopper](https://www.hopperapp.com/)
- Windows

## Further Readings

- [如何破解Mac软件的付费限制](https://blog.csdn.net/pbfl98/article/details/100625547)

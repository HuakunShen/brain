If addition of 2 numbers exceeds the maximum value a number can hold, overflow happens and results in a wrong number. The max int value is determined by the number of bits used to store a number.

If attacker manage to make the amount to subtract from balance to overflow to 0, or any small number, then attacker pay low/no cost. 
## Batch Transfer
Let contract send equal amount of funds to multiple receivers. 

## Solution
Use safe math operations. The `SafeMath` library always checks for the resulting value.
e.g. For addition of two unsigned int (a and b), the result $c$ must be larger than $a+b$.

Starting from solifity 0.8, compiler will detect and raise error when integer overflow happens.

## How to update code if vulnerability is found
Deploy a new contract. Make a snapshot of the old one. The design doesn't allow anyone to change the contract. 


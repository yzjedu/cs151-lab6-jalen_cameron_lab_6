# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. name: Display choice
2. parameter: none
3. return: input choice from user
4. algorithm:
   1. output options for user to choose from, D- deposit, W- withdraw, V - view balance, E - exit
   2. return input choice stripped and upper cased

5. name: deposit
6. parameter: current balance
7. return: current balance
8. algorithm:
   1. ask user to input deposit amount
   2. if deposit amount is a digit
      1. make deposit amount an integer
      2. if deposit amount is less than 0
         1. output an error message 
      3. otherwise 
         1. add the deposit to the current balance
         2. output a success and new balance
      4. output an error message
   3. return current balance
9. name: withdraw

10. parameter: current balance
11. return: current balance
12. algorithm:
    1. ask user to input withdraw amount
       1. if withdraw amount is a digit
          1. make deposit an integer
          2. if deposit is less than 0
             1. output an error message
       2. otherwise
          1. subtract the withdraw from the current balance
          2. output success and new balance
          3. if the current balance is less than 0
             1. output a warning
    2. output error
13. name: view
14. parameter: current balance
15. return: none
16. algorithm:
    1. output current balance
    2. return
17. name: main
18. parameter: none
19. return: none
20. algorithm:
    1. while choice is not equal to the SENTINEL
       1. set choice equal display choice
       2. if choice is equal to D
          1. set current balance equal to deposit
       3. if choice is equal to W
          1. set current balance equal to withdraw
       4. if choice is equal to V
          1. call view function
       5. if choice is equal to E
          1. output thank you for using the ATM program. Goodbye!
       6. else
          1. output error
    2. output ATM program has ended

21. call main function
# Coding Challenge - 2: Sudoku Format Converter&Printer
# The purpose of this coding challenge is to write a program that prints the given lists as sudoku looking format.

# Learning Outcomes
# At the end of this coding challenge, students will be able to;

# analyze a problem, identify, and apply programming knowledge for appropriate solution.

# design, implement arithmetic operators and nested loops effectively in Python to solve the given problem.

# demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

# Problem Statement
# 💡Objective:
# To improve your control flow statement skills.
# Task: The department you work for has received a project that displays the solved sudoku puzzles in a digital environment. 

# Write a Python code to print out the given sudoku puzzle matrix in the following format.
# Given format :
# sudoku = [
#     [0, 0, 0, 0, 6, 4, 0, 0, 0],
#     [7, 0, 0, 0, 0, 0, 3, 9, 0],
#     [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 5, 0, 2, 0, 6, 0],
#     [0, 8, 0, 4, 0, 0, 0, 0, 0],
#     [3, 5, 0, 6, 0, 0, 0, 7, 0],
#     [0, 0, 2, 0, 0, 0, 1, 0, 3],
#     [0, 0, 1, 0, 5, 9, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 7, 0, 0]
# ]
# Desired output format :
# - - - - - - - - - - - - - - - 
# 0  0  0  | 0  6  4  | 0  0  0  
# 7  0  0  | 0  0  0  | 3  9  0  
# 8  0  0  | 0  0  0  | 0  0  0  
# - - - - - - - - - - - - - - - 
# 0  0  0  | 5  0  2  | 0  6  0  
# 0  8  0  | 4  0  0  | 0  0  0  
# 3  5  0  | 6  0  0  | 0  7  0  
# - - - - - - - - - - - - - - - 
# 0  0  2  | 0  0  0  | 1  0  3  
# 0  0  1  | 0  5  9  | 0  0  0  
# 0  0  0  | 0  0  0  | 7  0  0  
# - - - - - - - - - - - - - - -


sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]


count = 0
print("- - - - - - - - - - - - - - - ")
for i in sudoku :
  for j in range(9) :
    print(i[j], " ", end="")
    if(j + 1) == 9 :
      print()
      count += 1
      if count%3 == 0 and count != 0:
        print("- - - - - - - - - - - - - - - ")
    if(j+1)%3==0 and j != 0 and j != 8 :
      print("| ",end= "")
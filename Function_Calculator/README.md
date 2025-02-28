# Python Calculator

## Description
This is a simple Python calculator program that allows users to perform basic arithmetic operations including addition, subtraction, multiplication, and division. The program runs in a loop, allowing users to continuously perform calculations until they choose to exit.

## Features
- Functions for each operation (`sum(x, y)`, `diff(x, y)`, `mult(x, y)`, `div(x, y)`) to handle calculations efficiently
- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers
- Input validation to handle incorrect inputs
- Looping functionality to perform multiple calculations

## Usage
The calculator uses functions to perform each operation:
- `sum(x, y)`: Adds two numbers
- `diff(x, y)`: Subtracts two numbers
- `mult(x, y)`: Multiplies two numbers
- `div(x, y)`: Divides two numbers
1. Run the Python script.
2. Select an operation from the menu:
   - `1` for Addition
   - `2` for Subtraction
   - `3` for Multiplication
   - `4` for Division
3. Enter two numbers as inputs.
4. View the result of the operation.
5. Choose whether to continue or exit the program.

## Example Execution
```
Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice(1/2/3/4): 1
Enter the value of 1st: 10
Enter the value of 2nd: 5
10.0 + 5.0 = 15.0
Let's do next calculation? (y/n): y
```

## Error Handling
- If a user enters a non-numeric value for numbers, the program prompts them to enter a valid number.
- If an invalid operation is selected, the program displays an error message.

## Requirements
- Python 3.x

## How to Run
1. Save the script as `calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the script's directory.
4. Run the command:
   ```
   python calculator.py
   ```

## License
This project is open-source and free to use.



# Types of Calculator Project

## Overview
This project contains multiple implementations of a simple calculator in Python, each using different programming constructs and techniques. 
The calculators perform basic arithmetic operations such as addition, subtraction, multiplication, and division. 
The project is designed to showcase different approaches to solving the same problem, making it a useful resource for learning and comparing Python programming techniques.

## Features
- **Multiple Implementations**: The project includes several versions of the calculator, each using different control structures and techniques.
- **Basic Arithmetic Operations**: All calculators support addition, subtraction, multiplication, and division.
- **Input Validation**: Each calculator includes input validation to handle incorrect user inputs.
- **Looping Functionality**: The calculators run in a loop, allowing users to perform multiple calculations until they choose to exit.
- **Error Handling**: Division by zero is handled gracefully, and invalid operation selections are managed with appropriate error messages.

## Implementations
The project includes the following implementations of the calculator:

### 1. Function-Based Calculator
- **File**: `Function_Calculator/Calculator.py`
- **Description**: This version uses functions to encapsulate each arithmetic operation, making the code modular and easy to understand.
- **Features**:
  - Functions for each operation (`sum(x, y)`, `diff(x, y)`, `mult(x, y)`, `div(x, y)`).
  - Input validation for non-numeric values.
  - Looping functionality for continuous calculations.

### 2. Match-Case Calculator (Python 3.10+)
- **File**: `Match_Case_Calculator/Calculator.py`
- **Description**: This version uses the `match-case` statement introduced in Python 3.10 to handle different arithmetic operations.
- **Features**:
  - `match-case` structure for operation selection.
  - Handles division by zero.
  - Looping functionality for continuous calculations.

### 3. Nested If-Else Simple Calculator
- **File**: `Nestedifelse_Simple_Calculator/Calculator.py`
- **Description**: This version uses a nested `if-elif` structure to handle different arithmetic operations.
- **Features**:
  - Nested `if-elif` structure for operation selection.
  - Handles division by zero.
  - Looping functionality for continuous calculations.

### 4. Nested If Simple Calculator
- **File**: `Nestedif_Simple_Calculator/Calculator.py`
- **Description**: This version uses a series of `if` statements to handle different arithmetic operations.
- **Features**:
  - Series of `if` statements for operation selection.
  - Handles division by zero.
  - Looping functionality for continuous calculations.

## Usage
To use any of the calculators, follow these steps:
1. Navigate to the directory containing the desired calculator implementation.
2. Run the Python script using the command:
   ```
   python Calculator.py
   ```
3. Follow the on-screen prompts to select an operation and input the numbers.
4. View the result and choose whether to continue or exit the program.

## Example Execution
Here is an example of running the Function-Based Calculator:
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

## Requirements
- **Python Version**: The project requires Python 3.x. The Match-Case Calculator specifically requires Python 3.10 or later.

## How to Run
1. Clone the repository or download the project files.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the desired calculator implementation.
4. Run the command:
   ```
   python Calculator.py
   ```

## License
This project is open-source and free to use. Feel free to modify and distribute it as needed.

## Contributing
Contributions are welcome! If you have any improvements or additional implementations, please feel free to submit a pull request.

## Contact
For any questions or feedback, please open an issue on the project repository.

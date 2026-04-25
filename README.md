 Workflow

This program follows a simple and structured execution flow:

1. Program Start
    Python checks whether the file is being executed directly using:

     ```python
     if __name__ == "__main__":
     ```

2. Main Function Execution

The `main()` function is called, acting as the control center of the program.

3. User Input

    The program asks the user to enter three integer values:

      `x` (base value)
      `a` (coefficient)
      `b` (coefficient)

4. Function Call

    The input values are passed to the `calculate()` function:

     ```python
     result = calculate(x, a, b)
     ```

5. Computation

    Inside `calculate()`, the expression is evaluated:

     ```
     y = a * x² + b * x + 1
     ```

6. Return Value

    The computed result is returned back to the `main()` function.

7. Output Display

    The result is displayed using formatted output:

     ```python
     print(f"Result: {result}")
     ```

---

  Program Description

This program is a simple implementation of a mathematical expression using structured Python programming.

It demonstrates how to:

 Take user input from the console
 Perform mathematical computations
 Use functions to separate logic from execution
 Return and display results in a clean format

The `calculate()` function acts as a reusable computation unit, while the `main()` function manages user interaction and program flow.

The use of:

```python
if __name__ == "__main__":
```

ensures that the program runs only when executed directly, making the code modular and reusable in other programs.

---

 Key Idea

The program follows a fundamental programming pattern:

> Input → Process → Output

 Input: User provides values (`x`, `a`, `b`)
Process: Function calculates the expression
Output: Result is displayed to the user

---

 Why This Matters

This structure reflects real-world programming practices where:

 Code is divided into logical parts
 Functions are used for reusability
 Execution is controlled and predictable


 This code is done by 
 Subhradeep Sardar
 BCA student 


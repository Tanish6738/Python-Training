# Python Training Notes - Day 0

## Python Documentation
- Official Python documentation: https://docs.python.org/
- Always refer to official docs for accurate information

## Python Basics

### Memory Management
- Memory is organized like a 2D grid (similar to an Excel sheet)
- Each memory location has:
  - **Address**: Location in memory
  - **Value**: Data stored at that location
  - **Variable**: Reference/pointer to the memory location
- Variables store references to data, not the data itself (similar to linked lists)

### Architecture
- **32-bit vs 64-bit**: Refers to the processor architecture and memory addressing capability
  - 32-bit: Can address up to 4GB of RAM
  - 64-bit: Can address much larger amounts of RAM

### Code Style
- **PEP 8**: Python Enhancement Proposal 8 - Official style guide for Python
- URL: https://pep8.org/
- Provides guidelines for writing clean, readable Python code

## Core Python Concepts

### Namespace
- **Definition**: A dictionary-like mapping where all data types and objects are stored
- Ensures unique identification of variables and functions
- Prevents naming conflicts

### Operators
1. **Arithmetic**: +, -, *, /, //, %, **
2. **Logical**: and, or, not
3. **Assignment**: =, +=, -=, *=, /=
4. **Bitwise**: 
   - | (PIPE - OR)
   - & (AMPERSAND - AND)
   - ~ (TILDE - NOT)
   - ^ (CARET - XOR)

### Data Types
- **Built-in types**: int, float, str, bool
- **Collections**: list, tuple, dict, set
- **Special**: range (generator for sequences)

### Control Flow
- **Colon (:)** signifies the start of a code block scope
- Used with: if, else, elif, while, for, def, class

## Strings

### String Basics
- Default string syntax uses single quotes ('')
- Can also use double quotes ("") or triple quotes (""" or ''')

### String Operations
- **Concatenation**: Joining strings using +
- **Slicing**: string[start:end] to extract substrings

### Memory Concepts
- **Shallow Copy**: Creates a new reference to the same object
  ```python
  ans = "r"
  result = ans + s_str[1:]  # Creates new string object
  ```
- **Deep Copy**: Creates a completely new object with copied data
- Variables are references that are garbage collected after program execution

### Sets Limitation
- Cannot perform concatenation on sets due to:
  - Unordered nature
  - Hash-based storage
  - No guaranteed memory allocation pattern

### Sequential Data Types
- Have continuous memory allocation
- Can be iterated using loops
- Support indexing and direct element access
- Examples: strings, lists, tuples

### Range Function
- `range()` is a function (hence uses parentheses and commas)
- Acts as a generator and iterator for creating sequences
- Memory efficient - generates values on demand

## Functions

### Types of Functions

#### 1. Built-in Functions
- Pre-defined in Python's standard library
- Native to Python interpreter
- Documentation: https://docs.python.org/3/library/functions.html
- Examples: print(), len(), type(), dir()

```python
import builtins
print(dir(builtins))  # Lists all built-in functions
```

#### 2. User-Defined Functions
- Created by programmers for specific tasks
- Custom functionality for ease of work

**Parameter Types:**

1. **Default Parameters**:
   ```python
   def func(a=10):
       return a
   ```

2. **Keyword Arguments**:
   ```python
   func(a=20)  # Calling with keyword
   ```

3. **Variable Arguments (*args)**:
   ```python
   def func(*a):
       print(type(a))  # Prints: <class 'tuple'>
   func(1, 2, 3, 4)
   ```

4. **Keyword Variable Arguments (**kwargs)**:
   ```python
   def func(**b):
       print(type(b))  # Prints: <class 'dict'>
   func(name="John", age=25)
   ```

#### 3. Lambda Functions (Anonymous)
- Syntax: `lambda parameters: expression`
- Used for optimization and short, simple functions
- Example: `square = lambda x: x**2`

#### 4. Higher-Order Functions
- Functions that take other functions as arguments
- Or return functions as results
- Examples: map(), filter(), reduce()

## Object-Oriented Programming (OOP)

### Core Concepts
- **Class**: Blueprint for creating objects
- **Object**: Instance of a class

### Four Pillars of OOP
1. **Abstraction**: Hiding implementation details
2. **Encapsulation**: Bundling data and methods together
3. **Polymorphism**: Same interface, different implementations
4. **Inheritance**: Deriving new classes from existing ones

### Magic/Dunder Methods
- Special methods with double underscores
- **`__init__(self)`**: Constructor method
  - `self` represents the current instance of the object
  - When creating `obj = Class()`, `obj` is referenced as `self`

### Method Overloading Limitation
- Python doesn't support traditional method overloading
- Due to namespace dictionary structure
- Same function name cannot exist multiple times in the same namespace

## Advanced Concepts

### Generators
- **Definition**: Functions that use `yield` to provide output one item at a time
- **Benefits**:
  - Memory efficient
  - Lazy evaluation
  - Can pause and resume execution
- **Usage**: When you need to process large datasets without loading everything into memory

### Key Insights
- Lambda functions optimize code by reducing function definition overhead
- Generators are essential for memory-efficient programming
- Understanding namespace helps debug naming conflicts
- OOP principles provide structure and reusability to code

## Best Practices
1. Follow PEP 8 style guidelines
2. Use meaningful variable names
3. Write docstrings for functions and classes
4. Leverage built-in functions when possible
5. Use generators for large data processing
6. Apply OOP principles for complex applications


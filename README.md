# Python vs C++ Data Types: Key Differences

Coming from C++ to Python, understanding the differences in how data types work will help you adapt more quickly. Here are the major differentiating factors:

## 1. Static vs Dynamic Typing

**C++:**
- Static typing: variables must be declared with their type before use
- Type checking occurs at compile-time
- Types cannot change once declared

```cpp
int number = 10;      // Type declared explicitly
number = "hello";     // Error: cannot assign string to int
```

**Python:**
- Dynamic typing: variables don't need type declarations
- Type checking occurs at runtime
- Variables can change types

```python
number = 10           # Type inferred as int
number = "hello"      # Valid: number is now a string
```

## 2. Primitive vs Object Types

**C++:**
- Distinguishes between primitive types and objects
- Primitives (int, float, char) are value types stored on stack
- Objects are reference types stored on heap

**Python:**
- Everything is an object (even numbers and booleans)
- All variables are references to objects
- No true primitives like in C++

## 3. Memory Management

**C++:**
- Manual memory management with new/delete
- Direct pointer manipulation
- RAII, smart pointers in modern C++

**Python:**
- Automatic garbage collection
- No direct pointer manipulation
- No need to free memory manually

## 4. Specific Data Type Differences

### Numbers

**C++:**
- Fixed-size types: int, float, double, etc.
- Overflow/underflow behavior is defined
- Type conversion needs explicit casting

```cpp
int i = 5;
double d = 2.5;
double result = i + d;  // Implicit conversion allowed for operands
int narrowed = (int)d;  // Explicit cast required for narrowing
```

**Python:**
- Integers have unlimited precision (no overflow)
- Automatic type conversion in many operations
- Explicit conversion functions (int(), float())

```python
i = 5
d = 2.5
result = i + d  # 7.5 (float)
narrowed = int(d)  # 2
```

### Strings

**C++:**
- `std::string` is mutable, separate from C-strings
- Character arrays and null-termination
- String manipulation often complex

**Python:**
- Strings are immutable sequences of Unicode characters
- Simple, powerful string operations
- Rich methods and slicing capabilities

```python
# Python string operations
s = "hello"
s += " world"  # Creates new string
substring = s[1:4]  # "ell"
```

### Arrays/Lists

**C++:**
- Arrays are fixed-size, homogeneous blocks of memory
- `std::vector` for dynamic arrays
- Type and size often specified at compile time

```cpp
int arr[5] = {1, 2, 3, 4, 5};  // Fixed size
std::vector<int> vec = {1, 2, 3};  // Dynamic
vec.push_back(4);  // Add element
```

**Python:**
- Lists are dynamic, heterogeneous collections
- Can hold items of different types
- Growth and shrinking handled automatically

```python
lst = [1, 2, "three", 4.0]  # Mixed types allowed
lst.append(5)  # Add element
```

### Dictionaries vs Maps

**C++:**
- `std::map` is ordered (tree-based)
- `std::unordered_map` is unordered (hash-based)
- Explicitly typed keys and values

```cpp
std::unordered_map<std::string, int> ages;
ages["Alice"] = 30;
```

**Python:**
- Dictionaries are hash-based (like unordered_map)
- Preserve insertion order (since 3.7)
- More concise syntax

```python
ages = {"Alice": 30, "Bob": 25}
```

### Tuples

**C++:**
- `std::tuple` or `std::pair` for fixed heterogeneous collections
- Verbose syntax, less commonly used

```cpp
std::tuple<int, std::string, double> person(30, "John", 5.8);
```

**Python:**
- Tuples are immutable sequences
- Commonly used for multiple return values and small collections
- Simple, concise syntax

```python
person = (30, "John", 5.8)
```

## 5. Type Checking

**C++:**
- Strong type checking at compile time
- Templates for generic programming

**Python:**
- Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"
- Type hints available but optional (since Python 3.5)

```python
# Python type hints (optional)
def greet(name: str) -> str:
    return "Hello, " + name
```

## 6. Conversion Between Types

**C++:**
- Explicit casting often required
- Strict conversion rules

**Python:**
- Many implicit conversions
- Built-in conversion functions (int(), str(), list(), etc.)

## 7. Custom Types

**C++:**
- Classes with precise control over behavior
- Operator overloading, constructors, destructors

**Python:**
- Classes with dynamic attributes
- "Dunder" methods for operator and behavior customization
- More flexible but less control over memory layout

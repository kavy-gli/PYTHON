# Interactive Personal Data Collector

## Overview
This Python program collects personal information from the user and displays it in a structured format.

It asks for:

- Name
- Age
- Height (in meters)
- Favorite number

It also calculates the user's estimated birth year.

---

## Features

### Data Collection
The program collects user input for:

- Name
- Age
- Height
- Favorite Number

---

### Data Type Display
It shows:

- The entered value
- Data type of the value
- Memory ID of the value

Example:
```python
your name is John (type: <class 'str'>, id: 24567890)
```

---

### Birth Year Estimation
The program calculates the estimated birth year using:

```python
2026 - Age
```

Example:

If age is:

```python
18
```

Output:

```python
So your estimated birth year is: 2008
```

---

## Sample Run

```python
Welcome to the interactive personal data collector!

Please enter your name: Alex
Please enter your age: 18
Please enter your height in (METERS): 1.75
Enter your favourite no: 7

Thank..U! here is the information we collected

your name is Alex
your age is 18
your height is 1.75
your favourite no is 7

So your estimated birth year is: 2008
```

---

## Concepts Used

- print()
- input()
- type()
- id()
- int()
- String concatenation
- Type conversion

---

## Learning Purpose

This project helps practice:

- Taking user input
- Working with strings
- Type conversion
- Understanding object types
- Using Python functions

---

## Author

Python Practice Project

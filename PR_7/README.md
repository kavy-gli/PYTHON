

# 🧰 Multi-Utility Toolkit

### A clean, all-in-one Python toolkit for everyday scripting tasks

[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()
[![PRs](https://img.shields.io/badge/PRs-Welcome-orange?style=for-the-badge)]()

*Datetime helpers, math operations, random data generation, UUIDs, file I/O, and a built-in module explorer — wrapped in one friendly CLI.*

</div>

---

## ✨ Features

| Module | What it does |
|---|---|
| 🕒 **`datetime_utils`** | Get the current timestamp, diff two dates, reformat dates, run a stopwatch or countdown |
| ➗ **`math_utils`** | Factorials, compound interest, trigonometry, circle area |
| 🎲 **`random_utils`** | Random integers, random lists, secure-style passwords, OTP codes |
| 🆔 **`uuid_utils`** | Generate UUID1 (time-based) and UUID4 (random) identifiers |
| 📁 **`file_utils`** | Create, write, read, and append to files in a few lines |
| 🔍 **`explorer`** | Inspect any Python module with `dir()` right from the menu |
| 🖥️ **`main.py`** | A friendly interactive CLI tying every module together |

---

## 📦 Project Structure

```
utils/
├── __init__.py          # Package entry point — exposes all utilities
├── datetime_utils.py    # Date & time helpers
├── math_utils.py        # Mathematical operations
├── random_utils.py       # Random data generators
├── uuid_utils.py         # UUID generation
├── file_utils.py          # File read/write/append helpers
└── explorer.py            # Module introspection (dir())

main.py                   # Interactive CLI menu
```

> 💡 Place the seven utility files inside a folder named **`utils/`** alongside `main.py`, since `main.py` imports them via `from utils import *`.

---

## 🚀 Getting Started

### Prerequisites
- Python **3.7+** — no external dependencies, just the standard library 🎉

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/multi-utility-toolkit.git
cd multi-utility-toolkit

# Run it — that's it, no pip install needed!
python main.py
```

---

## 🖥️ Usage

Launch the CLI and pick an option from the menu:

```
=== Multi-Utility Toolkit ===
1. Datetime Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module (dir)
7. Exit

Enter choice:
```

### Using the functions directly in your own scripts

```python
from utils import *

# 🕒 Datetime
print(current_datetime())                       # 2026-06-19 14:32:01
print(date_difference("2026-01-01", "2026-06-19"))  # 169

# ➗ Math
print(factorial(10))                  # 3628800
print(compound_interest(1000, 5, 3))  # 1157.625
print(area_circle(4))                 # 50.265...

# 🎲 Random
print(random_password(12))   # e.g. 'aZ9!kLp2QmTx' (adjust chars set as needed)
print(random_otp())          # e.g. 482913

# 🆔 UUID
print(generate_uuid4())      # e.g. 3f29b1d2-...

# 📁 Files
create_file("notes.txt")
write_file("notes.txt", "Hello, world!")
print(read_file("notes.txt"))

# 🔍 Explore any module
import math
print(explore_module(math))
```

---

## 🧩 Module Reference

<details>
<summary><strong>🕒 datetime_utils</strong></summary>

| Function | Description |
|---|---|
| `current_datetime()` | Returns the current date & time as a string |
| `date_difference(date1, date2)` | Absolute number of days between two `YYYY-MM-DD` dates |
| `format_date(date, format_string)` | Reformats a date using a custom `strftime` pattern |
| `stopwatch(seconds)` | Counts up to `seconds`, printing each elapsed second |
| `countdown(seconds)` | Counts down from `seconds` to zero |

</details>

<details>
<summary><strong>➗ math_utils</strong></summary>

| Function | Description |
|---|---|
| `factorial(n)` | Factorial of `n` |
| `compound_interest(p, r, t)` | Compound interest for principal `p`, rate `r`%, time `t` |
| `trig_calculation(angle)` | Returns `sin`, `cos`, `tan` for an angle in degrees |
| `area_circle(radius)` | Area of a circle |

</details>

<details>
<summary><strong>🎲 random_utils</strong></summary>

| Function | Description |
|---|---|
| `random_number(start, end)` | Random integer in range |
| `random_list(size, start, end)` | List of random integers |
| `random_password(length)` | Random alphanumeric password |
| `random_otp()` | Random 6-digit OTP |

</details>

<details>
<summary><strong>🆔 uuid_utils</strong></summary>

| Function | Description |
|---|---|
| `generate_uuid1()` | Time-based UUID |
| `generate_uuid4()` | Random UUID |

</details>

<details>
<summary><strong>📁 file_utils</strong></summary>

| Function | Description |
|---|---|
| `create_file(filename)` | Creates an empty file |
| `write_file(filename, data)` | Overwrites a file with new content |
| `read_file(filename)` | Reads and returns file content |
| `append_file(filename, data)` | Appends content to a file |

</details>

<details>
<summary><strong>🔍 explorer</strong></summary>

| Function | Description |
|---|---|
| `explore_module(module)` | Returns `dir(module)` for quick introspection |

</details>

---

## 🗺️ Roadmap

- [ ] Add unit tests for every module
- [ ] Replace blind `input()` calls with validated parsing
- [ ] Add a `--cli-args` mode for non-interactive use
- [ ] Publish to PyPI as an installable package

---




</div>

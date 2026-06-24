# 📝 Task Manager System

A clean, dependency-free command-line task manager built in Python. Add tasks, track their progress, search by status, and persist everything to disk — all from a simple, friendly terminal menu.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Add Task** | Create a task with a title and description. Empty fields are rejected automatically. |
| 📋 **View Tasks** | List every task with its ID, title, description, status, and creation timestamp. |
| ✅ **Mark Complete** | Mark a task as done by its ID, with a random motivational quote on success. |
| 🎉 **Completion Celebration** | A celebratory banner pops up automatically once *every* task is marked complete. |
| 🔍 **Search by Status** | Instantly filter tasks by `Pending` or `Completed`. |
| 💾 **Save / Auto-Persist** | Tasks are saved to `data.txt` and reloaded automatically the next time you run the app. |
| 🗑️ **Reset Tasks** | Wipe all tasks clean, with a confirmation prompt to prevent accidents. |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+ (no external libraries required — uses only the standard library)

### Run it

```bash
python task_manager.py
```

That's it — no `pip install`, no setup. Just run the script and the menu takes over.

---

## 🖥️ Usage

On launch, you'll see the main menu:

```
==================================================
          TASK MANAGER SYSTEM
==================================================
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Search By Status
5. Save Tasks
6. Reset Tasks
7. Exit
==================================================
Enter your choice (1-7):
```

Pick a number and follow the prompts. A quick walkthrough of each option:

1. **Add Task** — enter a title and description. Both fields are required.
2. **View Tasks** — prints every task currently stored, including its unique 8-character ID.
3. **Mark Task Complete** — paste in a task's ID to mark it done. You'll get a random motivational quote, and if it was the *last* pending task, a celebration banner.
4. **Search By Status** — type `Pending` or `Completed` to see matching tasks (case-insensitive).
5. **Save Tasks** — writes the current task list to `data.txt` immediately.
6. **Reset Tasks** — deletes all tasks after a `yes`/`no` confirmation.
7. **Exit** — saves your tasks and closes the program.

> 💡 Tasks are also auto-saved when you exit (option 7), and auto-loaded from `data.txt` the next time you start the program.

---

## 🧩 How It Works

### `Task`
Represents a single task:
- Auto-generates a short, unique `task_id` (first 8 characters of a UUID4).
- Validates that `title` and `description` are non-empty.
- Tracks `status` (`Pending` → `Completed`) and a `created_on` timestamp.

### `TaskManager`
Owns the full task list and the menu logic:
- `add_task()`, `view_tasks()`, `mark_complete()` — core CRUD operations.
- `all_tasks_completed()` + `show_celebration()` — detects when every task is done and shows a celebration message.
- `search_by_status()` — filters tasks by status.
- `save_to_file()` / `load_from_file()` — simple pipe-delimited (`|`) persistence to `data.txt`.
- `reset_tasks()` — clears all tasks with a confirmation step.

### Data Format (`data.txt`)
Each line stores one task as:

```
task_id|title|description|status|created_on
```

Example:
```
a1b2c3d4|Buy groceries|Milk, eggs, bread|Pending|2026-06-24 10:15:32
```

---

## 📂 Project Structure

```
.
├── task_manager.py    # Main application (Task + TaskManager classes, CLI loop)
└── data.txt           # Auto-generated — stores saved tasks (created on first save/exit)

## 🛣️ Ideas for Future Improvements

- [ ] Edit existing task title/description
- [ ] Delete a single task by ID
- [ ] Switch persistence to JSON or SQLite for more robust storage
- [ ] Add due dates and priority levels
- [ ] Add sorting (by date, status, or title)


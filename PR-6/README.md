# 📓 Personal Journal Manager

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-educational-green)
![Storage](https://img.shields.io/badge/storage-plain%20text-lightgrey)

A simple command-line journaling app written in Python. Add timestamped entries, browse your full journal, search by keyword or date, and clear everything when you want a fresh start — all backed by a single, human-readable text file.

---

## 📑 Table of Contents

- [Features](#-features)
- [How It Works](#️-how-it-works)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Example Session](#-example-session)
- [Journal File Format](#-journal-file-format)
- [Error Handling](#️-error-handling)
- [Known Limitations](#️-known-limitations)
- [Roadmap](#️-roadmap--ideas-for-contributors)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 📝 **Add Entry** — write a journal entry, automatically stamped with the current date and time
- 📖 **View Entries** — print every entry stored in the journal, in order
- 🔎 **Search Entry** — find entries by keyword or by date (case-insensitive substring match)
- 🗑️ **Delete All Entries** — wipe the journal file, with a confirmation prompt
- 🛡️ Graceful handling of missing files, permission errors, and invalid menu input
- 🐍 Uses Python's `match` statement for clean menu dispatch

---

## ⚙️ How It Works

All logic lives in a single `JournalManager` class:

| Method | Responsibility |
|---|---|
| `add_entry()` | Appends a timestamped entry to `journal.txt` |
| `view_entries()` | Reads and prints the full contents of the journal file |
| `search_entry()` | Scans each line of the journal for a keyword/date match |
| `delete_entries()` | Removes the journal file entirely, after confirmation |

The journal is stored as plain text (`journal.txt` by default), so it's easy to back up, version, or read outside the app.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ (required for the `match` statement)
- No external dependencies — uses only the standard library (`datetime`, `os`)

### Installation
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### Run it
```bash
python journal_manager.py
```

---

## 📖 Usage

On launch, you'll see a menu:

```
========================================
WELCOME TO PERSONAL JOURNAL MANAGER
========================================
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

| Choice | Action |
|---|---|
| `1` | Write a new entry; it's saved with a timestamp |
| `2` | Print every entry currently in the journal |
| `3` | Search entries by keyword or date string |
| `4` | Delete the journal file (asks for `yes`/`no` confirmation) |
| `5` | Exit the program |

---

## 🧪 Example Session

```
Enter your choice: 1

Enter your journal entry: Finished the README for my project today. Feeling productive!
Entry added successfully!

========================================
WELCOME TO PERSONAL JOURNAL MANAGER
========================================
...
Enter your choice: 2

Your Journal Entries:
----------------------------------------

[2026-06-19 14:32:07]
Finished the README for my project today. Feeling productive!

========================================
WELCOME TO PERSONAL JOURNAL MANAGER
========================================
...
Enter your choice: 3
Enter a keyword or date to search: productive

Matching Entries:
----------------------------------------
Finished the README for my project today. Feeling productive!

========================================
WELCOME TO PERSONAL JOURNAL MANAGER
========================================
...
Enter your choice: 5
Thank you for using Personal Journal Manager. Goodbye!
```

---

## 🗂️ Journal File Format

Each entry is appended to `journal.txt` in this format:

```
[YYYY-MM-DD HH:MM:SS]
<entry text>
```

Because it's plain text, you can open `journal.txt` directly in any text editor, sync it with cloud storage, or commit it to a private git repo for version history.

---

## 🛡️ Error Handling

| Scenario | Behavior |
|---|---|
| Viewing/searching before any entry exists | Friendly message instead of a crash |
| No write permission on the journal file | `"Permission denied!"` message |
| Deleting when no journal file exists | `"No journal entries to delete."` |
| Entering non-numeric menu input | `"Please enter numbers only."` |
| Any other unexpected error | Caught and printed instead of crashing the program |

---

## ⚠️ Known Limitations

- Search matches on raw lines, so a multi-line entry's text and its timestamp line are matched separately rather than as one unit.
- Deleting "all entries" removes the entire file rather than letting you delete a single entry.
- No edit functionality for existing entries.
- Single flat file — no tagging, categories, or multi-journal support.

---

## 🗺️ Roadmap / Ideas for Contributors

- [ ] Allow editing or deleting a single entry instead of all-or-nothing
- [ ] Add tags/categories and filter by them
- [ ] Support exporting entries to JSON or Markdown
- [ ] Add a date-range search (e.g., entries between two dates)
- [ ] Encrypt the journal file for privacy
- [ ] Add unit tests (`pytest`) using a temporary file fixture

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project doesn't yet include a license file. Add a `LICENSE` (e.g., MIT) to your repository to clarify how others may use, modify, and distribute this code.

---

## 👤 Author

Maintained by ** kavy **. Update this section with your name, GitHub profile, and contact details.

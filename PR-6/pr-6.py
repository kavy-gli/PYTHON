from datetime import datetime
import os

class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # Add Entry
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ")

            with open(self.filename, "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"\n[{timestamp}]\n{entry}\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Permission denied!")

        except Exception as e:
            print("Error:", e)

    # View Entries
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

                if data.strip() == "":
                    print("Journal is empty.")
                else:
                    print("\nYour Journal Entries:")
                    print("-" * 40)
                    print(data)

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except Exception as e:
            print("Error:", e)

    # Search Entry
    def search_entry(self):
        try:
            keyword = input("Enter a keyword or date to search: ")

            with open(self.filename, "r") as file:
                lines = file.readlines()

            found = False

            print("\nMatching Entries:")
            print("-" * 40)

            for line in lines:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print(f"No entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("Error: Journal file not found.")

        except Exception as e:
            print("Error:", e)

    # Delete All Entries
    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("No journal entries to delete.")
                return

            choice = input(
                "Are you sure you want to delete all entries? (yes/no): "
            ).lower()

            if choice == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            else:
                print("Deletion cancelled.")

        except PermissionError:
            print("Permission denied!")

        except Exception as e:
            print("Error:", e)


# Main Program
journal = JournalManager()

while True:

    print("\n" + "=" * 40)
    print("WELCOME TO PERSONAL JOURNAL MANAGER")
    print("=" * 40)

    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        match choice:

            case 1:
                journal.add_entry()

            case 2:
                journal.view_entries()

            case 3:
                journal.search_entry()

            case 4:
                journal.delete_entries()

            case 5:
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            case _:
                print("Invalid option. Please select a valid option.")

    except ValueError:
        print("Please enter numbers only.")

    except Exception as e:
        print("Error:", e)

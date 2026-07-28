from database.notes_db import (
    create_note,
    get_notes,
    get_note,
    update_note,
    delete_note
)


def confirm_exit():
    answer = input(
        "\nExit Notes Manager and lose current input? (y/n): "
    )

    return answer.lower() == "y"


def notes_command():
    while True:
        try:
            print("""
=========================
       Notes Manager
=========================

1. Create a note
2. View notes
3. Edit a note
4. Delete a note
5. Return to AtlasOS

=========================
""")

            choice = input("Choice > ")

            if choice == "1":
                create_note_menu()

            elif choice == "2":
                view_notes_menu()

            elif choice == "3":
                update_note_menu()

            elif choice == "4":
                delete_note_menu()

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

        except KeyboardInterrupt:
            print("\n")

            if confirm_exit():
                print("Returning to AtlasOS...")
                break
            else:
                print("Continuing Notes Manager...\n")


def create_note_menu():
    try:
        print("\n=== Create Note ===")

        title = input("Title: ")
        content = input("Content: ")

        create_note(title, content)

        print("Note created successfully!\n")

    except KeyboardInterrupt:
        print("\n")

        if confirm_exit():
            print("Note creation cancelled.")
        else:
            print("Returning to note creation...")


def view_notes_menu():
    print("\n=== Your Notes ===")

    notes = get_notes()

    if not notes:
        print("No notes found.\n")
        return

    for note in notes:
        print("-" * 35)
        print("ID:", note[0])
        print("Title:", note[1])
        print("Content:", note[2])
        print("Created:", note[3])

    print("-" * 35)


def update_note_menu():
    try:
        print("\n=== Edit Note ===")

        note_id = input("Note ID: ")

        note = get_note(note_id)

        if note is None:
            print("Note not found.")
            return

        print("\nCurrent title:", note[1])
        print("Current content:", note[2])

        new_title = input("New title: ")
        new_content = input("New content: ")

        update_note(note_id, new_title, new_content)

        print("Note updated successfully!\n")

    except KeyboardInterrupt:
        print("\nModification cancelled.")


def delete_note_menu():
    try:
        print("\n=== Delete Note ===")

        note_id = input("Note ID: ")

        note = get_note(note_id)

        if note is None:
            print("Note not found.")
            return

        confirmation = input(
            f"Delete '{note[1]}' permanently? (y/n): "
        )

        if confirmation.lower() == "y":
            delete_note(note_id)
            print("Note deleted.\n")
        else:
            print("Deletion cancelled.\n")

    except KeyboardInterrupt:
        print("\nDeletion cancelled.")
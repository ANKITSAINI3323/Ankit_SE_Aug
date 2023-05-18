import os


def create_note():
    note_title = input("Enter note title: ")
    note_content = input("Enter note content: ")
    
    with open('notes.txt', 'a') as f:
        f.write(note_title + '\n' + note_content + '\n')
    print("Note added successfully!")


def view_notes():
    
    with open('notes.txt', 'r') as f:
        notes = f.readlines()
    if len(notes) == 0:
        print("No notes found.")
    else:
        
        for i in range(0, len(notes), 2):
            print("Title: " + notes[i].strip())
            print("Content: " + notes[i+1].strip())
            print()


def display_menu():
    print("                     ")
    print("\t\t welcome to E-Note Book")
    print("                     ")
    print("\t\tE-Note Book Console-based Application")
    print("\t\tPress 1 for Generate note")
    print("\t\tPress 2 for View note")
    print("\t\tPress 3 for Exit")


def main():
    
    if not os.path.exists('notes.txt'):
        with open('notes.txt', 'w') as f:
            pass
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            

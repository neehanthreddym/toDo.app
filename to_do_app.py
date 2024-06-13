import sys

todo_file = "todo_file.txt"
todos = []
arguments = sys.argv

# Read file
try:
    file = open(todo_file, 'r')
    todos = file.readlines()
    file.close()
except:
    pass

# Add ToDo
if len(arguments) >= 3 and arguments[1].lower() == 'add':
    todos.append(f"{arguments[2]}\n")


# Remove ToDo
def remove_todo(arguments):
    if len(arguments) >= 3 and arguments[1].lower() == 'remove':
        try:
            index_to_del = int(arguments[2])
            if index_to_del > 0:
                index_to_del -= 1
                del(todos[index_to_del])
            else:
                print(f"--- Out of range ---")
                sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)

remove_todo(arguments)

# Save file
file = open(todo_file, 'w')
file.writelines(todos)
file.close()

# Print ToDos list
def showToDos(todos):
    if len(todos) == 0:
        print("You have no todos :)")
    else:
        print("\nHere's your ToDo list:")
        print("--------------------------\n")
        for num, todo in enumerate(todos):
            print(f"{num+1}. {todo}", end="")

showToDos(todos)

print("\n--------------------------\n")

print(f"To view ToDos:\n{arguments[0]}")
print(f"\nTo add ToDo:\n{arguments[0]} add \"Your ToDo goes here\"")
print(f"\nTo remove ToDo:\n{arguments[0]} remove <ToDo option>")
todo = []

while True:
    task = input("Type 'add' , 'show' , 'remove' , 'exit' : ")

    if task == 'show':
        for i, t in enumerate(todo):
            print(f"{i+1}. {t}")

    elif task == 'remove':
        idx = int(input("Enter task no. to remove : ")) - 1
        if idx <= idx < len(todo):
            todo.pop(idx)
            print(f"Task removed: {todo[idx]}")

    elif task == 'add':
        new = input("Enter Task to be added : ")
        todo.append(new)
        print(f"Task added {new}")

    elif task == 'exit':
        print("Exiting the To-Do List application.")
        break

    else:
        print("Invalid Option")
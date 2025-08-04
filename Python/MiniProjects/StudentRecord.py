while True:
    action = input("Choose: add / view / delete / exit: ").strip().lower()

    if action == "add":
        name = input("Enter student name: ").strip()
        marks = input("Enter marks: ").strip()

        with open("student_record.txt", "a") as f:
            f.write(f"{name}:{marks}\n")

    elif action == "view":
        try:
            with open("student_record.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        name, marks = line.split(":", 1)
                        print(f"{name.strip()} scored {marks.strip()}")
        except FileNotFoundError:
            print("No student record file found.")

    elif action == "delete":
        deletename = input("Enter name to delete: ").strip().lower()

        try:
            with open("student_record.txt", "r") as f:
                lines = f.readlines()

            with open("student_record.txt", "w") as f:
                found = False
                for line in lines:
                    line_clean = line.strip()
                    if line_clean == "":
                        continue

                    name_in_file = line_clean.split(":", 1)[0].strip().lower()
                    if name_in_file != deletename:
                        f.write(line)
                    else:
                        found = True

                if not found:
                    print("Name not found.")
                else:
                    print(f"Deleted record for: {deletename}")
        except FileNotFoundError:
            print("No student record file found.")

    elif action == "exit":
        print("Exiting...")
        break
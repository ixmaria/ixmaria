def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def show_all_files():
    import os
    files = os.listdir('.')
    print("Files available:")
    for idx, file_name in enumerate(files, start=1):
        print(f"{idx}. {file_name}")

def view_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Content of '{file_name}':")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def main():
    while True:
        option = input("Choose an option:\n1. Write to a file\n2. Show all files\n3. View file content\n4. Exit\n")

        if option == '1':
            file_name = input("Enter file name: ")
            content = input("Enter content: ")
            write_to_file(file_name, content)
            print("File has been written successfully!\n")
        elif option == '2':
            show_all_files()
        elif option == '3':
            file_name = input("Enter the file name to view its content: ")
            view_file_content(file_name)
        elif option == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.\n")

if __name__ == "__main__":
    main()

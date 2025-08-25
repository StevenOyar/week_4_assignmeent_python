# Simple File Modifier

user_input = input("Enter the file name here (include the extension): ")
output_file = "output_file.txt"


lines = [
    "Good morning\n",
    "How have you been doing\n",
    "Are you from USA or Germany\n",
    "Do you listen to Afrobeat\n",
    "I am from Kenya\n",
    "Kisii county\n",
]


try:
    # Check if file has .txt extension only
    if not user_input.lower().endswith(".txt"):
        raise ValueError(f"Only .txt files are allowed. You entered: {user_input}")
    
    # Write to file.txt
    with open("file.txt", "w") as file:
        for line in lines:
            file.write(line)

    # Read input file
    with open(user_input, "r") as file:
        content = file.read()

    # Modify content (convert to uppercase )
    modified_content = content.upper()

    # Write to output file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"Success! Modified file saved as {output_file}")
    print()
    print(f"Original: {user_input}:")
    print(content)
    
    print(f"\n\nModified content (uppercase) in {output_file}")
    print(modified_content)

except FileNotFoundError:
    print(f" Error: {user_input} not found. File doesn't exist.")
except ValueError as e:
    print(f"File type restriction: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

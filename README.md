# File Handling

A Python program demonstrating robust file operations with error handling and text processing capabilities.

## Overview

This simple yet comprehensive Python program showcases essential file handling operations including reading, writing, and error management. The program prompts users to specify a `.txt` file, processes its contents by converting text to uppercase, and outputs the result to a new file named `output_file.txt`.

## Features

- **File Reading**: Reads content from user-specified text files
- **Text Processing**: Converts file content to uppercase
- **File Writing**: Saves processed content to `output_file.txt`
- **Console Output**: Displays both original and modified content
- **Robust Error Handling**:
  - `FileNotFoundError` → Handles missing input files
  - `ValueError` → Validates file extensions (`.txt` only)
  - `Exception` → Catches unexpected errors gracefully

## How It Works

### 1. **User Input & Validation**
```python
user_input = input("Enter the file name here (include the extension): ")
output_file = "output_file.txt"

# File extension validation
if not user_input.lower().endswith(".txt"):
    raise ValueError(f"Only .txt files are allowed. You entered: {user_input}")
```

### 2. **Predefined Content Setup**
```python
lines = [
    "Good morning\n",
    "How have you been doing\n",
    "Are you from USA or Germany\n",
    "Do you listen to Afrobeat\n",
    "I am from Kenya\n",
    "Kisii county\n",
]
```

### 3. **File Reading**
```python
with open(input_file, "r") as file:
    content = file.read()
```

### 4. **Content Processing**
```python
modified_content = content.upper()
```

### 5. **File Writing**
```python
with open(output_file, "w") as file:
    file.write(modified_content)
```

### 6. **Error Handling**
```python
except FileNotFoundError:
    print(f"Error: {user_input} not found. File doesn't exist.")
except ValueError as e:
    print(f"File type restriction: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Requirements

- Python 3.x
- Text file with `.txt` extension for input

## Usage

1. Run the Python script
2. Enter the name of your `.txt` file when prompted
3. The program will:
   - Read your file
   - Convert content to uppercase
   - Save the result to `output_file.txt`
   - Display both original and modified content

## Example

```
Enter the file name here (include the extension): file.txt

Original content:
Hello world
This is a test file

Modified content:
HELLO WORLD
THIS IS A TEST FILE

Content successfully written to output_file.txt
```

## Error Scenarios

| Error Type | Cause | Program Response |
|------------|--------|-----------------|
| **FileNotFoundError** | Input file doesn't exist | Shows file not found message |
| **ValueError** | Non-`.txt` file provided | Shows file type restriction message |
| **Exception** | Unexpected error | Shows generic error message |



# ECE_Student_Check

## Overview

This Python script provides an interface for users to input an ID either manually or through a card reader. It presents the user with a menu to choose between the two options and processes the input accordingly.

## Features

- Read ID from a card reader by swiping a card.
- Manually input an ID through keyboard entry.
- Error handling for invalid input choices.
- Easy-to-use interface.

## Requirements

- Python 3.x
- Windows operating system (for card reader functionality using `msvcrt`)
- Integrated terminal (for optimal usage in environments like Visual Studio Code)

## Usage

1. Run the script (`main.py`).
2. Follow the on-screen prompts:
   - Choose option 1 to read the ID from the card reader.
   - Choose option 2 to manually enter the ID.
   - Choose option 3 to exit the program.
3. If selecting option 1, swipe the card when prompted.
4. If selecting option 2, enter the ID manually when prompted.
5. The entered ID will be displayed on the screen.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/id-input-system.git
   ```

2. Navigate to the project directory:

   ```
   cd id-input-system
   ```

3. Run the script:

   ```
   python main.py
   ```

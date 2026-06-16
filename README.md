
# Random Password Generator

## Overview

This is a simple Python program that generates random passwords based on a user-specified length. The generated password consists of uppercase letters, lowercase letters, digits, and special characters, making it suitable for creating strong and secure passwords.

## Features

* Generates passwords of customizable length.
* Uses a combination of:

  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Numbers (`0-9`)
  * Special characters (`!@#$%^&*`, etc.)
* Randomly shuffles characters to enhance unpredictability.
* Lightweight and easy to use.

## Technologies Used

* Python 3
* `string` module
* `random` module

## How It Works

1. The program imports predefined character sets from the `string` module.
2. All character sets are combined into a single list.
3. The list is shuffled using the `random.shuffle()` function.
4. The user enters the desired password length.
5. The program displays a randomly generated password of the specified length.

## Running the Program

Execute the script using:

```bash
python password_generator.py
```

Example:

```text
Enter the password length:
10
```

Output:

```text
g#P8!aL2@x
```

## Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

## Limitations

* The program does not guarantee the inclusion of at least one uppercase letter, lowercase letter, digit, and special character in every generated password.
* Password length should not exceed the total number of available characters in the combined character set.

## Future Enhancements

* Ensure at least one character from each category is included.
* Add password strength validation.
* Create a graphical user interface (GUI).
* Allow users to select which character types to include.

## Author

Navya Agarwal

## License

This project is intended for educational and learning purposes.

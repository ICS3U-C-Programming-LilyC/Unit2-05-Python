#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/2/2023
# This program uses scope variables (local and global).

# Declaring global variable.
variable_x = 25


def local_variable():
    # This shows what happens with local variables.
    variable_x = 10
    variable_y = 30

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Local variable:  {variable_x} + {variable_y} = {variable_z}")


def global_variable():
    # This shows what happens with global variables.
    global variable_x
    variable_y = 30

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main():
    # This function shows how local and global variables work.
    local_variable()
    global_variable()


if __name__ == "__main__":
    main()

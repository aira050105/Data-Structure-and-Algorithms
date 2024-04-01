import math
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate y values based on the equation
def calculate_y_values(x_values, equation):
    if equation == "x^2+7x+2":
        return [(x**2 + 7*x + 2) for x in x_values]
    elif equation == "3x+2":
        return [(3*x + 1) for x in x_values]  # Assuming '@' as 1
    elif equation == "x^2":
        return [(x**2) for x in x_values]
    elif equation == "x^3":
        return [(x**3) for x in x_values]
    elif equation == "x^5":
        return [(x**5) for x in x_values]
    elif equation == "x^3+2x^2+x+10":
        return [(x**3 + 2*x**2 + x + 10) for x in x_values]
    elif equation == "x^4-3x^3+2x^2+100":
        return [(x**4 - 3*x**3 + 2*x**2 + 100) for x in x_values]
    elif equation == "sin(x)":
        return [np.sin(x) for x in x_values]
    elif equation == "cos(x)":
        return [np.cos(x) for x in x_values]
    elif equation == "x^5+4x^4-x^3-2x^2+100":
        return [(x**5 + 4*x**4 - x**3 - 2*x**2 + 100) for x in x_values]
    else:
        return [0 for x in x_values]  # Return zeros for unsupported equations

# Function to write data to a file
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

# Function to read data from a file and return as a list
def read_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(float(line.strip()))
    return data

# Define equations
equations = ["x^2+7x+2",
              "3x+2",
             "x^2",
             "x^3",
             "x^5",
             "x^3+2x^2+x+10", 
             "x^4-3x^3+2x^2+100",
             "sin(x)",
             "cos(x)",
             "x^5+4x^4-x^3-2x^2+100"]

# Generate x values from 1 to 50
x_values = list(range(0, 50))

# Loop through equations, calculate y values, write data to files, and plot
for equation in equations:
    y_values = calculate_y_values(x_values, equation)
    filename = equation.replace('^', '_').replace('+', '').replace('-', '').replace('(', '').replace(')', '') + '.txt'
    write_to_file(filename, y_values)
    
    # Plotting
    plt.plot(x_values, y_values, label=equation)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graphs of Various Equations')
plt.legend()
plt.grid(True)
plt.show()
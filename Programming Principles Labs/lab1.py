# Program Name: Lab1.py
# Course: IT1114/Section W03
# Student Name: Braeden Wings
# Assignment Number: Lab 1
# Due Date: 01/19/2025
# Purpose: This program will calculate the total square footage of flooring needed using the length and width given of the flooring space, the total cost of the flooring before and after tax, and calculate the tax from the cost before tax to determine the total cost of the flooring to give flooring cost after tax. It will prompt the user to input the length, width, and cost of square footage using a different function and call the function that calculates those inputs and give a result after finishing with the inputs.
# I used my knowledge on the python coding language and what i've learned from my IT1114 class, kaggle (which I've used in my spare time to further my learning), and different coding projects with a similar format to create this code to the best of my abilities. I mainly use Intellij's pycharm to do most of my python coding, but I also used pythonIDLE to ensure that make code works in both programs. I did not use the built-in AI assistant that comes with pycharm and made the code completely off knowledge of the code.

# a function to calculate the total square footage, cost of the project before tax, the tax itself, and total cost of the project from the length and with of the room and the cost of the flooring per square foot
def cost_of_flooring_total(length, width, cost_per_sqft):
    # will calculate the total square footage need for flooring project
    total_sqft = length * width
    # will calculate the cost of the project before tax by multiplying the cost per square feet by the total square footage
    cost_before_tax = cost_per_sqft * total_sqft
    # will calculate the tax by multiplying the base tax rate of 7% by the cost of the project before tax
    tax = .07 * cost_before_tax
    # will calculate the total cost of the project by adding the cost before tax plus the tax from the code above
    total_cost = cost_before_tax + tax
    # will give the amount of each variable when calling the function in the module. This will be the total square footage, cost before tax, the tax itself, and the total cost of the whole project
    return total_sqft, cost_before_tax, tax, total_cost

# a function for the user to input the variables of length, width, and cost per sqft and then run the function above and print the result to get the format from the sample in the lab assignment
def flooring_calculator():
    # run a "flooring calculator" for the user to input the variables of their room and the flooring cost per square feet
    length = float(input("Enter the length of the room (in feet): "))
    width = float(input("Enter the width of the room (in feet): "))
    cost_per_sqft = float(input("Enter the cost per square foot: "))
    # calling the function cost_of_flooring_total to have the return of said function actually becoming variables
    total_sqft, cost_before_tax, tax, total_cost = cost_of_flooring_total(length, width, cost_per_sqft)
    # print text with the result of each variable in the cost_of_flooring_total function
    print("Total square footage of your project: ", total_sqft)
    print("The cost of your project before tax: ", cost_before_tax)
    print("The tax: ", tax)
    print("The total cost of your flooring project plus tax: ", total_cost)

# a block to ensure that when running the code in a module, it will prompt the user to input the length, width, and cost per square foot
if __name__ == "__main__":
    flooring_calculator()

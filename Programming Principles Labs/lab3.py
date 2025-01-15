# Program name: Lab3.py
# Course: IT1114/Section W03
# Student Name: Braeden Wings
# Assignment Number: Lab 3
# Due Date: 02/02/2025
# Purpose: 
#

def sales (sales_goal):
    # will start numbering each of the sales people entered
    salesperson_number = 1
    # a variable to store the combined total of all salespeople entered
    total_sales_all = 0
    # list to store sales data for all salespeople
    salespeople_data = []

    # loop for enter the sales data for each salesperson added to the list
    while True:
        # will prompt the user to enter the weekly sales for the first salesperson
        print(f"Enter sales for salesperson #{salesperson_number}:")
        # list to store the sales data for each week
        weekly_sales = []
        # loop to gather sales for the 4 weeks
        for week in range (1, 5):
            while True:
                try:
                    sales_total = float(input(f"Week {week} sales: $"))
                    weekly_sales.append(sales_total)
                    # exit the loop if the sales entry is valid
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        # calculate the total sales for each sales person added and add it to the total sales of every sales person
        total_sales = sum(weekly_sales)
        total_sales_all += total_sales

        # another loop to ask if there are more sales people
        another = input("Is there another salesperson? (yes/no): ").strip().lower()

        # an if statement for when there are no more salespeople or if there are more salespeople
        if another == "no":
            # Exit the loop when all the sales peoples data is added
            break
        # will add another person to the list
        else:
            salesperson_number += 1

    # calculate the manager's bonus based on the sales goal
    manager_bonus = total_sales_all * .02
    if total_sales_all > sales_goal:
         manager_bonus = total_sales_all * .05

    return salesperson_number, sales_goal, total_sales_all, manager_bonus

# block to make the function work and print the outputs needed for the lab
if __name__ == "__main__":
    sales_goal = float(input("Enter the sales goal: "))
    # calls the function above
    salesperson_number, sales_goal, total_sales_all, manager_bonus = sales(sales_goal)

    # prints the outputs needed
    print("Department Monthly Sales and Commission")
    print("Number of Employees:", salesperson_number)
    print("Department Sales Goal:", sales_goal)
    print(f"Total Sales: ${total_sales_all:.2f}")
    print(f"Manager Bonus: ${manager_bonus:.2f}")

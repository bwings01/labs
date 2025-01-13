# Program Name: Lab2.py
# Course: IT1114/Section W03
# Student Name: Braeden Wings
# Assignment Number: Lab 2
# Due Date: 01/26/2025
# Purpose: Calculate the amount of whole pizzas needed, salads needed, the total from the cost of whole pizzas and salads, the discount for whole pizzas and salads, the delivery fee, and the total amount due. Print out the same values in an easy-to-read format.
# I used my knowledge of the python, what I've learned in my IT1114 class and from my Lab, as well as what I've learned from kaggle and other outside resources. Since I used Intellij's pycharm to do my coding, I've also gone and made sure that the code works in IDLE before I submitted.

# math import needed for pizza_salad_order function below
import math
# a function to calculate the amount of pizzas needed, the cost of each pizza, the cost of each salad, the total cost of pizzas and salads, the discount, the delivery cost, and the overall total from pizza orders and salad orders
def pizza_salad_order(pizza_orders, salad_orders):
    # calculation of pizza orders to show that a whole pizza is 12 slices but each order is 3 slices. the base price of a whole pizza is 15.99. calculation of the total slices needed for the order and the whole pizzas needed by dividing the total slices needed by the slices in a whole pizza and rounding that to a base number. calculates the total cost of the pizzas by multiplying the amount of whole pizzas needed by the cost of a whole pizza
    slices_per_whole_pizza = 12
    slices_per_order = 3
    pizza_cost = 15.99
    total_slices_needed = pizza_orders * slices_per_order
    whole_pizzas_needed = math.ceil(total_slices_needed / slices_per_whole_pizza)
    total_pizza_cost = whole_pizzas_needed * pizza_cost
    # calculation of the total cost of salads by multiplying the salad orders by 7.99
    salad_cost = 7.99 * salad_orders
    # calculation of the total cost of both pizzas and salads combined
    total_cost = total_pizza_cost + salad_cost
    # to give a base discount of both pizza and salads 0 so that a discount isn't given every time
    discount_pizza = discount_salad = 0
    # an if statement that will give a discount if the amount of pizzas is over 10 by multiplying the total cost of pizzas by 15%
    if whole_pizzas_needed > 10:
        discount_pizza = total_pizza_cost * .15
    # an if statement will give a discount if the amount of salads is over 10 by multiplying the total cost of salads by 15%
    if salad_orders > 10:
        discount_salad = salad_cost * .15
    # calculation for the total discounts on the order
    discount = discount_pizza + discount_salad
    # calculation for the delivery cost
    delivery_cost = total_cost * .07
    # an if statement to keep the base delivery cost at $20 if the above calculation comes out to less than $20
    if delivery_cost < 20:
        delivery_cost = 20
    # the total amount due at the end of the transaction
    total_cost_due = (total_cost - discount) + delivery_cost
    # will give the return values of the defined variables below
    return whole_pizzas_needed, total_pizza_cost, salad_cost, total_cost, discount, delivery_cost, total_cost_due

# a function for the user to interactively put how many pizza and salad orders they have and display each of the return values above while turning them into variables
def order_up():
    # the interface for the user to input how many pizza and salad orders that have
    pizza_orders = float(input("How many pizzas would you like to order? "))
    salad_orders = float(input("How many salads would you like to order? "))
    # makes the return values above into variables that will come from the function pizza_salad_order
    whole_pizzas_needed, total_pizza_cost, salad_cost, total_cost, discount, delivery_cost, total_cost_due = pizza_salad_order(pizza_orders, salad_orders)
    # prints out each of the now defined variables with clear labels beside them to show the transaction total with all the different parts of the total amount due
    print("Pizzas ordered", whole_pizzas_needed)
    print("Pizza cost $", total_pizza_cost)
    print("Salad cost $", salad_cost)
    print("Total $", total_cost)
    print("Discount $", discount)
    print("Delivery fee $", delivery_cost)
    print("Total amount due $", total_cost_due)
# a block to make the order_up function actually function when run through a module
if __name__ == "__main__":
    order_up()

# Project Statement: Bean and Brew Cafe Billing and Order System

## 1. Problem Statement
In cafes and coffee shops, taking orders on paper slips can be confusing. When waiters write down drink customisations like extra espresso shot or oat milk by hand, sometimes the person making the coffee misreads it and prepares the wrong drink. Also, calculating service charge and gst on a calculator takes extra time and cashiers can make silly math errors when there is a rush. So I wanted to create a simple python command line program where the cashier can enter table orders, add customisations easily, and print the total bill automatically without calculation mistakes.

## 2. Scope of the Project
This project handles the basic ordering and billing work for a dine-in cafe:
- Showing the menu with hot coffees, cold brew, and bakery items.
- Taking customer orders for tables (table 1 to 20).
- Allowing customers to order multiple items in one go using a loop.
- Adding extra charges for large cup size and add-ons like caramel or extra shots.
- Calculating the subtotal, 5% service charge, and 5% gst for the final bill.
- Printing a neat receipt in the terminal.

## 3. Target Users
- Cafe counter staff or cashiers taking orders from customers sitting at tables.
- Customers who want a clean receipt showing what they ordered and the exact tax.

## 4. High-Level Features
- Menu Viewer: Shows item codes, names, categories, base prices, and extra charges.
- Order Loop: Lets you keep adding items with size and add-on choices until you type 'n'.
- Price Customizer: Uses if-elif statements to add extra cost for large size and selected add-ons.
- Automatic Bill Calculation: Automatically calculates 5% service charge and 5% gst on the subtotal.
- Terminal Receipt: Prints a neat formatted guest check with item details and grand total.

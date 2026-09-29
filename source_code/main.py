from menu import do_show_menu
from order import do_order
from billing import do_view_last_bill

def main():
    while True:
        print("\n==========================================")
        print("         Bean & Brew Cafe System          ")
        print("==========================================")
        print("1. View Menu")
        print("2. Place Order and Generate Bill")
        print("3. View Last Receipt")
        print("4. Exit")
        print("------------------------------------------")

        ch = input("Enter choice (1-4): ").strip()

        if ch == "1":
            do_show_menu()
        elif ch == "2":
            do_order()
        elif ch == "3":
            do_view_last_bill()
        elif ch == "4":
            print("\nExiting cafe system.")
            break
        else:
            print("\nInvalid choice. Please choose from 1 to 4.")

if __name__ == "__main__":
    main()

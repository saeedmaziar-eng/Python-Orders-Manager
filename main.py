orders = ["Laptop", "Mouse", "Keyboard", "Monitor"]
print(orders)
while True:
    print("1-> show orders")
    print("2-> add order")
    print("3-> search order")
    print("4-> edit order")
    print("5-> delete order")
    print("6-> total orders")
    print("7-> check Laptop")
    print("8-> sort orders")
    print("9-> finish and show final orders")
    choice = input("Enter your choice: ")
    if choice == "1":
        for i in orders:
            print(i)
    elif choice == "2":
        new_order = input("Enter your new order: ")
        orders.append(new_order)
        print("Success!")
    elif choice == "3":
        products_name = input("Enter your products: ")
        if products_name in orders:
            print("Found")
        else:
            print("Not Found")
    elif choice == "4":
        old_order = input("Enter your old order: ")
        if old_order in orders:
            index = orders.index(old_order)
            new_order = input("Enter your new order: ")
            orders[index] = new_order
            print("Success!")
            print(orders)
        else:
            print("Not Found")
    elif choice == "5":
        delete_order = input("Enter your order to delete: ")
        if delete_order in orders:
            index = orders.index(delete_order)
            orders.remove(delete_order)
            print("Success!")
        else:
            print("Not Found")
    elif choice == "6":
        print(len(orders))
    elif choice == "7":
        if "Laptop" in orders:
            print("Laptop exists in orders")
        else:
            print("Laptop does not exist in orders")
    elif choice == "8":
        orders.sort()
        print("Success!")
        print(orders)
    elif choice == "9":
        print(orders)
        break
    else:
        print("Wrong Input")



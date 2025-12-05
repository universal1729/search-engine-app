import webbrowser

print("Which E-commerce platform would you like to use today?")

choice = input("Enter 1 for Amazon or 2 for Ebay or 3 for Alibaba or 4 for Temu: ")

if choice == '1':

    webbrowser.open_new_tab("https://www.amazon.com")


elif choice == '2':

    webbrowser.open_new_window("https://www.ebay.com")

elif choice == '3':
    webbrowser.open_new_tab("https://www.alibaba.com")

elif choice == '4':
    webbrowser.open_new_tab("https://www.temu.com")



else:
    print("Invalid choice")
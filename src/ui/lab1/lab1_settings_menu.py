def settings_option(HISTORY_FILE):
    """Display settings options and perform the selected action."""
    while True:
        print("\nOptions:")
        print("1. Display calculation history")
        print("2. Clear history")
        print("3. Set memory functions")
        print("4. Set decimal places")
        print("5. Back")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            display_history(HISTORY_FILE)
        elif choice == '2':
            clear_history(HISTORY_FILE)
        elif choice == '3':
            set_memory_functions()
        elif choice == '4':
            set_decimal_places()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")
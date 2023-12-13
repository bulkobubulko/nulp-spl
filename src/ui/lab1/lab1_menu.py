HISTORY_FILE = 'data/lab1/history.txt'

def main():    
    while True:
        print("\nOptions:")
        print("1. Perform calculation")
        print("2. Settings")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            result = calculate_option()
            save_result(result, HISTORY_FILE, number_of_calculations)
        elif choice == '2':
            settings_option(HISTORY_FILE)
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()
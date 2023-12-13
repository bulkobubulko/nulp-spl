import importlib

class Runner:
    """
    This class provides an interface for users to select and execute labs 
    within the specified range (Lab 1 to Lab 8). It utilizes a modular 
    approach, importing the 'main' function from the respective lab modules.
    """
    MAX_LAB_NUMBER = 8

    @staticmethod   
    def run_lab(lab_number):
        """Run the selected lab."""
        module_name = f"..src.lab{lab_number}.main"

        try:
            # Import the 'main' function from the lab module
            main_module = importlib.import_module(module_name)
            main_function = getattr(main_module, "main")

            # Check if 'main' is callable
            if callable(main_function):
                main_function()
                print(f"Lab {lab_number} executed successfully.")
            else:
                print(f"Error: 'main' function not found in module {module_name}")

        except ImportError as e:
            print(f"Error importing module {module_name}: {e}")

    def get_user_input(self):
        """Get user input for lab selection."""
        while True:
            try:
                print(f"\nSelect a lab to run (1-{self.MAX_LAB_NUMBER}) or press 'q' to quit:")
                user_input = input("Lab: ")
                
                if user_input.lower() == 'q':
                    print("Exiting...")
                    return None
                
                lab_number = int(user_input)
                if 1 <= lab_number <= self.MAX_LAB_NUMBER:
                    return lab_number
                else:
                    print(f"Please enter a number between 1 and {self.MAX_LAB_NUMBER}.")

            except ValueError:
                print("Please enter a valid integer.")

    def main(self):
        while True:
            lab_number = self.get_user_input()
            if lab_number is None:
                break
            self.run_lab(lab_number)

if __name__ == "__main__":
    Runner().main()
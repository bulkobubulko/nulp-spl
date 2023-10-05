HISTORY_FILE = 'source/lab1/history.txt'

# History functions

def save_history(HISTORY_FILE, history):
    """
    Saves history to file.
    
    Args:
        HISTORY_FILE (str): Path to history file.
        history (list): List of dictionaries containing the operation and the result.
    """
    with open(HISTORY_FILE, "w") as file:
        for entry in history:
            file.write(f"{entry['operation']} = {entry['result']}\n")

def load_history(HISTORY_FILE):
    """
    Loads history from file.
    
    Args:
        HISTORY_FILE (str): Path to history file.
    
    Returns: 
        history (list): List of dictionaries containing the operation and the result.
    
    Raises:
        FileNotFoundError: If file does not exist.
    """
    history = []
    try:
        with open(HISTORY_FILE, "r") as file:
            for line in file:
                operation, result = line.strip().split(" = ")
                result_dict = {'operation': operation, 'result': float(result)}
                history.append(result_dict)
    except FileNotFoundError:
        pass 
    return history

def display_history(HISTORY_FILE):
    """
    Display history from file.
    
    Args:
        HISTORY_FILE (str): Path to history file.   
    """
    history = load_history(HISTORY_FILE)
    if len(history) == 0:
        print("History is empty")
    else:
        with open(HISTORY_FILE, "r") as file:
            for line in file:
                print(line.strip())
                
def clear_history(HISTORY_FILE):
    """
    Clear history from file.
    
    Args:
        HISTORY_FILE (str): Path to history file.
    """
    with open(HISTORY_FILE, "w") as file:
        file.write("")
    print("History cleared")
import os
import json
import csv
import datetime

def save_data(data, folder_path, file_name, file_format, field_names=None):
    supported_formats = ['json', 'csv', 'txt']
    
    if file_format.lower() not in supported_formats:
        print(f"Unsupported file format: {file_format}")
        return
    
    file_path = os.path.join(folder_path, f"{file_name}.{file_format}")
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            if file_format.lower() == 'json':
                json.dump(data, file, indent=2)
            elif file_format.lower() == 'csv':
                writer = csv.DictWriter(file, field_names=field_names)
                writer.writeheader()
                writer.writerows(data)
            elif file_format.lower() == 'txt':
                for item in data:
                    file.write(str(item) + '\n')
            else:
                print(f"Unsupported file format: {file_format}")
    except Exception as e:
        print(f"Error saving data: {e}")

def log_user_history(action, user_input, result, log_file):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(f"{current_time} - Action: {action} - Input: {user_input} - Output: {result}\n")
    except Exception as e:
        print(f"Error logging user history: {e}")       
        
def view_user_history(log_file):
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            history = file.readlines()
            for entry in history:
                print("\t" + entry)
    except FileNotFoundError:
        print("No user history found.")
    except Exception as e:
        print(f"Error viewing user history: {e}")

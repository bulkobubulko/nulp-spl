import os

from service.lab8.data_preprocessing import DataExploration, DataCleaning, DataVisualization
from config.path_config import FOLDER_PATH_PLOT_LAB8, FOLDER_PATH_DATASETS_LAB8

# Checking if directories exist and creating them if not
for directory in [FOLDER_PATH_PLOT_LAB8, FOLDER_PATH_DATASETS_LAB8]:
    if not os.path.exists(directory):
        os.makedirs(directory)
    
def main():
    print("Provide file path or press enter to use the default file path.")
    user_input = input("File path: ")
    
    if user_input:
        csv_path = user_input
    else:
        csv_path = f'{FOLDER_PATH_DATASETS_LAB8}USA_Housing.csv'
        print(f"Using default file path: {csv_path}")

    try:
        explorer = DataExploration(csv_path, FOLDER_PATH_PLOT_LAB8, FOLDER_PATH_DATASETS_LAB8)
        cleaner = DataCleaning(csv_path, FOLDER_PATH_PLOT_LAB8, FOLDER_PATH_DATASETS_LAB8)
        visualizer = DataVisualization(csv_path, FOLDER_PATH_PLOT_LAB8, FOLDER_PATH_DATASETS_LAB8)

        explorer.data_exploration()
        cleaner.data_cleaning()
        visualizer.data_visualization()

        print("Data processing completed successfully!")

    except FileNotFoundError:
        print(f"Error: The specified CSV file '{csv_path}' does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
import os

FOLDER_PATH_PLOTS = 'data/lab8/plots/'
FOLDER_PATH_DATASETS = 'data/lab8/datasets/'

# Checking if directories exist and creating them if not
for directory in [FOLDER_PATH_PLOTS, FOLDER_PATH_DATASETS]:
    if not os.path.exists(directory):
        os.makedirs(directory)
    
def main():
    print("Provide file path or press enter to use the default file path.")
    user_input = input("File path: ")
    
    if user_input:
        csv_path = user_input
    else:
        csv_path = 'sources/datasets/USA_Housing.csv'
        print(f"Using default file path: {csv_path}")

    try:
        explorer = DataExploration(csv_path, FOLDER_PATH_PLOTS, FOLDER_PATH_DATASETS)
        cleaner = DataCleaning(csv_path, FOLDER_PATH_PLOTS, FOLDER_PATH_DATASETS)
        visualizer = DataVisualization(csv_path, FOLDER_PATH_PLOTS, FOLDER_PATH_DATASETS)

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
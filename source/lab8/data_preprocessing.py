import os
import pandas as pd
import numpy as np
import seaborn as sns   
import matplotlib.pyplot as plt
import warnings

# Filter out UserWarnings related to figure layout changes
warnings.filterwarnings("ignore", category=UserWarning)

class DataExploration():
    """Class for data exploration operations"""
    def __init__(self, csv_file, folder_path_plots, folder_path_datasets) -> None:
        if not os.path.isfile(csv_file):
            raise FileNotFoundError(f"The specified CSV file '{csv_file}' does not exist.")
        
        self.csv_file = pd.read_csv(csv_file)
        self.csv_file_name = os.path.splitext(os.path.basename(csv_file))[0]
        self.folder_path_plots = folder_path_plots
        self.folder_path_datasets = folder_path_datasets
        
    def data_exploration(self):
        """Perform data exploration"""
        print("\nData exploration:")
        
        print("\nFirst 5 rows of data:")
        print(self.explore_data_first())
        print("\nLast 5 rows of data:")
        print(self.explore_data_last())
        print("\nColumns of data:")
        print(self.explore_data_columns())
        print("\nShape of data:")
        print(self.explore_data_shape())
        print("\nExtreme values of data:")
        self.get_extreme_values()
        
    def explore_data_first(self):
        """Get first 5 rows of data"""
        return self.csv_file.head()
    
    def explore_data_last(self):
        """Get last 5 rows of data"""
        return self.csv_file.tail()
    
    def explore_data_columns(self):
        """Get columns of data"""
        return self.csv_file.columns
    
    def explore_data_shape(self):
        """Get shape of data"""
        return self.csv_file.shape
    
    def get_extreme_values(self):
        """Get extreme values of data"""
        for column in self.csv_file.columns:
            if self.csv_file[column].dtype == 'object':
                continue
            min_value = self.csv_file[column].min()
            max_value = self.csv_file[column].max()
            median = self.csv_file[column].median()
            print(f"Column: {column}, min: {min_value}, max: {max_value}, median: {median}")
            
class DataCleaning(DataExploration):
    """Class for data cleaning operations"""
    def __init__(self, csv_file, folder_path_plots, folder_path_datasets) -> None:
        super().__init__(csv_file, folder_path_plots, folder_path_datasets)
        
    def data_cleaning(self):
        """Perform data cleaning"""
        print("\nData cleaning:")
                
        if self.csv_file.isnull().values.any():
            print("Missing values found")
            cleaned_file_path = self.drop_missing_values()
            print(f"Missing values dropped and saved to {cleaned_file_path}")
        else:
            print("No further cleaning required.") 
            
        print("Data cleaning completed")
            
    def drop_missing_values(self):
        """Drop missing values and return cleaned file path"""
        if self.csv_file.isnull().values.any():
            self.csv_file.dropna(inplace=True)
            
            cleaned_file_path = os.path.join(
                self.folder_path_datasets,
                f"{self.csv_file_name}_cleaned.csv",
            )
            
            self.csv_file.to_csv(cleaned_file_path, index=False)
            return cleaned_file_path

        
class DataVisualization(DataExploration):
    """Class for data visualization operations"""
    def __init__(self, csv_file, folder_path_plots, folder_path_datasets) -> None:
        super().__init__(csv_file, folder_path_plots, folder_path_datasets)
        
    def data_visualization(self):
        """Perform data visualization"""
        print("\nData visualization:")
        pairplot_path = self.plot_pairplot()
        print(f"Pairplot plotted and saved to {pairplot_path}")
        heatmap_path = self.plot_heatmap()
        if heatmap_path:
            print(f"Heatmap plotted and saved to {heatmap_path}")
        else:
            print("No numeric columns found for heatmap.")
        
    def plot_pairplot(self):
        """Plot pairplot"""
        sns.pairplot(self.csv_file)
        pairplot_path = f'{self.csv_file_name}_pairplot'
        pairplot_path = self.export_plot_to_png(plt, pairplot_path)
        return pairplot_path

    def plot_heatmap(self):
        """Plot heatmap for numeric columns"""
        numeric_df = self.csv_file.select_dtypes(include=[np.number])
        
        if not numeric_df.empty:
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
            plt.title("Correlation Heatmap")
            
            heatmap_path = f'{self.csv_file_name}_heatmap'
            heatmap_path = self.export_plot_to_png(plt, heatmap_path)
            
            return heatmap_path
        else:
            return None

    def export_plot_to_png(self, plt, file_name):
        """Export plot to PNG file with exception handling"""
        file_path = f"{self.folder_path_plots}{file_name}.png"
        try:
            plt.savefig(file_path, bbox_inches='tight')
        except Exception as e:
            print(f"Error exporting plot: {e}")
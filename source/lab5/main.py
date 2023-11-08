# Include the parent directory in the system's import path
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from lab5.three_d_shape import ThreeDShape

SETTINGS_FILE_PATH = 'source/lab5/settings.json'

def main():
    shape_obj = ThreeDShape()
    shape_obj.set_settings_file_path(SETTINGS_FILE_PATH)
    shape_obj.load_settings()
    # shape_obj.render_3d_shape()
    
    while True:
        print('\n')
        print('Options:')
        print('1. Render 3D shape rotating')
        print('2. Render 3D shape static')
        print('3. Settings')
        print('4. Exit')
        user_input = input('Enter option number: ')
        
        if user_input == '1':
            shape_obj.render_3d_shape_static()
        elif user_input == '2':
            shape_obj.render_3d_shape_rotating()
        elif user_input == '3':
            shape_obj.settings()
        elif user_input == '4':
            break

if __name__ == "__main__":
    main()
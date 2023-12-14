from service.lab5.three_d_shape import ThreeDShape
from config.path_config import SETTINGS_FILE_PATH_LAB5

def main():
    shape_obj = ThreeDShape()
    shape_obj.set_settings_file_path(SETTINGS_FILE_PATH_LAB5)
    shape_obj.load_settings()
    menu(shape_obj)
        
def menu(shape_obj):
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
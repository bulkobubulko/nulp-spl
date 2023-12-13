from shared.ascii_utils import set_font, set_size, set_symbols, set_color, set_alignment, set_3d_option

def settings(settings_obj):
    while True:
        print('Options:')
        print('0. Show current settings')
        print('1. Change size')
        print('2. Change symbol')
        print('3. Change color')
        print('4. Change alignment')
        print('5. Change 3D option')
        print('6. Reset settings')
        print('7. Back')
        
        user_input = input('Enter option number: ')
        if user_input == '0':
            settings_obj.show_settings()
        elif user_input == '1':
            settings_obj.set_size(*set_size())
        elif user_input == '2':
            settings_obj.set_symbols(*set_symbols())
        elif user_input == '3':
            settings_obj.set_color(set_color())
        elif user_input == '4':
            settings_obj.set_alignment(set_alignment())
        elif user_input == '5':
            settings_obj.set_3d_option(set_3d_option())
        elif user_input == '6':
            settings_obj.default_settings()
        elif user_input == '7':
            break
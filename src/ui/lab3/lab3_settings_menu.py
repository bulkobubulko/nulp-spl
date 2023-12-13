from shared.ascii_utils import set_font, set_size, set_symbols, set_color

def settings_menu(settings_obj):    
    while True:
        print('Options (1/2/3/4/5/6):')
        print('0. Show current settings')
        print('1. Change font')
        print('2. Change size')
        print('3. Change symbol')
        print('4. Change color')
        print('5. Reset settings')
        print('6. Back')
        
        user_input = input('Enter option number: ')
        if user_input == '0':
            settings_obj.show_settings()
        if user_input == '1':
            settings_obj.set_font(set_font())
        elif user_input == '2':
            settings_obj.set_size(*set_size())
        elif user_input == '3':
            settings_obj.set_symbols(*set_symbols())
        elif user_input == '4':
            settings_obj.set_color(set_color())
        elif user_input == '5':
            settings_obj.default_settings()
        elif user_input == '6':
            break
import os.path
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import detector
from infi.systray import SysTrayIcon
import configparser

DEFAULT_PATH = 'templateimages\\req_queue.png'
template_path = 'templateimages\\winter_queue.png'
threshold = 0.6

def main():
    """ Main function which calls other helper functions """
    load_config()
    while True:
        win_loc = detector.window_location()
        if win_loc is not None:
            league_img = detector.grab_screen(win_loc)
            global template_path
            if os.path.isfile(template_path):
                queue_result = detector.detect_queue(league_img, template_path, threshold)
                if queue_result:
                    print("Queue Detected")
            elif os.path.isfile(DEFAULT_PATH):
                template_path = DEFAULT_PATH
                queue_result = detector.detect_queue(league_img, template_path, threshold)
                if queue_result:
                    print("Queue Detected")
            else:
                get_custom_file()

def load_config():
    global template_path
    global threshold
    config = configparser.RawConfigParser()
    config.read('config.ini')
    template_path = config['SETTINGS']['TemplateImagePath']
    threshold = config['SETTINGS']['Threshold']

def get_custom_file():
    global template_path
    Tk().withdraw()
    filepath = askopenfilename(title="Select file of custom queue template image")
    if (filepath != ""):
        template_path = filepath
        config = configparser.RawConfigParser()
        config.read('config.ini')
        config['SETTINGS']['TemplateImagePath'] = filepath
        config['SETTINGS']['TemplateImageType'] = 'cust'

        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        pass

def start_systray():
    # icon = glob.glob("icons/sync.ico")
    icon = "icons/sync.ico"
    checkmark_icon = "icons/checkmark.ico"
    hover_text = "League Queue Notify"

    def quit_app(sysTrayIcon):
        print("Bye")

    def change_queue_reg(sysTrayIcon):
        menu_options = reg_menu
        sysTrayIcon.update(menu_options=menu_options)
        save_menu_choice("templateimages\\reg_queue.png", "reg")

    def change_queue_win(sysTrayIcon):
        menu_options = win_menu
        sysTrayIcon.update(menu_options=menu_options)
        save_menu_choice("templateimages\\winter_queue.png", "win")

    def change_queue_cust(sysTrayIcon):
        menu_options = cust_menu
        sysTrayIcon.update(menu_options=menu_options)
        get_custom_file()
    
    reg_menu = (('Change queue image', None, (('Regular queue', checkmark_icon, change_queue_reg),
                                              ('Winter queue', None, change_queue_win),
                                              ('Custom queue...', None, change_queue_cust))),)
    win_menu = (('Change queue image', None, (('Regular queue', None, change_queue_reg),
                                              ('Winter queue', checkmark_icon, change_queue_win),
                                              ('Custom queue...', None, change_queue_cust))),)
    cust_menu = (('Change queue image', None, (('Regular queue', None, change_queue_reg),
                                               ('Winter queue', None, change_queue_win),
                                               ('Custom queue...', checkmark_icon, change_queue_cust))),)

    menu_options = load_menu_choice(reg_menu, win_menu, cust_menu)

    systray = SysTrayIcon(icon, hover_text, menu_options, on_quit=quit_app, default_menu_index=1)
    systray.start()

def load_menu_choice(reg, win, cust):
    config = configparser.RawConfigParser()
    config.read('config.ini')
    template_choice = config['SETTINGS']['TemplateImageType']
    if (template_choice == 'reg'):
        return reg
    elif (template_choice == 'win'):
        return win
    elif (template_choice == 'cust'):
        return cust
    else:
        return reg

def save_menu_choice(filepath, queue_type):
    global template_path
    template_path = filepath
    config = configparser.RawConfigParser()
    config.read('config.ini')
    config['SETTINGS']['TemplateImagePath'] = filepath
    config['SETTINGS']['TemplateImageType'] = queue_type

    with open('config.ini', 'w') as configfile:
            config.write(configfile)

if __name__ == '__main__':
    start_systray()

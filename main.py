import detector
import SysTrayIcon
import configparser

template_path = 'templateimages\\winter_queue.png'
threshold = 0.6

def main():
    """ Main function which calls other helper functions """
    load_config()
    while True:
        win_loc = detector.window_location()
        if win_loc is not None:
            league_img = detector.grab_screen(win_loc)
            queue_result = detector.detect_queue(league_img, template_path, threshold)
            if queue_result:
                print("Queue Detected")

def load_config():
    global template_path
    global threshold
    config = configparser.RawConfigParser()
    config.read('config.ini')
    template_path = config['SETTINGS']['TemplateImagePath']
    threshold = config['SETTINGS']['Threshold']

def start_systray():
    # icon = glob.glob("icons/sync.ico")
    icon = "icons/sync.ico"
    hover_text = "League Queue Notify"
    def placeholder_menu(sysTrayIcon):
        print("Placeholder")
    def quit_app(sysTrayIcon):  
        print("Bye")
    menu_options = (('Placeholder', icon, placeholder_menu),)

    SysTrayIcon.SysTrayIcon(icon, hover_text, menu_options, on_quit=quit_app, default_menu_index=1)

if __name__ == '__main__':
    start_systray()

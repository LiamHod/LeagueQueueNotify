import detector

def main():
    """ Main function which calls other helper functions """
    while True:
        win_loc = detector.window_location()
        if win_loc is not None:
            league_img = detector.grab_screen(win_loc)
            queue_result = detector.detect_queue(league_img)
            if queue_result:
                print("Queue Detected")

main()
import cv2

def main():
    """ Main function that loads and plays video """
    cap = cv2.VideoCapture('queuevideo.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('League of Legends', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()

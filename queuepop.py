import cv2
import detector

def get_video(video_name):
    """ Main function that loads and plays video """
    cap = cv2.VideoCapture(video_name)

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('League of Legends', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    get_video("tools\\queuevideo.mp4")

import cv2

# def main():
#     """ Main function that loads and plays video """
#     cap = cv2.VideoCapture('queuevideo.mp4')
#     ret, frame = cap.read()
#     while 1:
#         ret, frame = cap.read()
#         cv2.imshow('League of Legends', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
#             cap.release()
#             cv2.destroyAllWindows()
#             break
#         cv2.imshow('frame', frame)

def alternative():
    cap = cv2.VideoCapture('queuevideo.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('League of Legends', frame)
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

alternative()

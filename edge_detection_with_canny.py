import cv2

def main(threshold1=100, threshold2=120):
    camera_stream = cv2.VideoCapture(0)

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_edge = cv2.Canny(img_gray, threshold1, threshold2)
        cv2.imshow('edge detected image', img_edge)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    threshold1 = 30
    threshold2 = 120
    main(threshold1=threshold1, threshold2=threshold2)

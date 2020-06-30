import cv2

def main(kernel=(5, 5)):
    camera_stream = cv2.VideoCapture(0)

    while True:
        is_return, img = camera_stream.read()
        if not is_return:
            break
        img_gaussian = cv2.GaussianBlur(img, kernel, 0)
        cv2.imshow('gaussian image', img_gaussian)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    kernel = (41, 41)
    main(kernel=kernel)

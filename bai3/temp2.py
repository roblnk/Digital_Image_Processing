import cv2
import numpy as np

bg_path = 'bai3\\blue_screen.jpg'
fg_path = 'bai3\\cat.jpg'
def blue_screen_matting(foreground_img_path, background_img_path, blue_threshold=0):
    # Load foreground and background images
    foreground = cv2.imread(foreground_img_path)
    background = cv2.imread(background_img_path)
    
    # Resize the foreground to match the size of the background
    background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
     
    # Extract blue screen mask from foreground
    blue_mask = cv2.inRange(foreground, (0,0, blue_threshold), (0,0,100))
    blue_mask = cv2.cvtColor(blue_mask, cv2.COLOR_GRAY2BGR)

    # Calculate difference between foreground and background
    diff = cv2.absdiff(foreground, background)
    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

    # Perform matting using Smith and Blinn algorithm
    alpha = cv2.cvtColor(alpha, cv2.COLOR_GRAY2BGR)
    foreground = foreground.astype(float)
    background = background.astype(float)
    alpha = alpha.astype(float)/255
    new_background = np.zeros(foreground.shape, dtype=float)
    rows,cols,_ = foreground.shape
    for i in range(rows):
        for j in range(cols):
            if all(blue_mask[i,j] == [255, 255, 255]):
                new_background[i,j] = [0,0,0]
            else:
                new_background[i,j] = background[i,j] * alpha[i,j]
    alpha = alpha.astype(int)
    print(alpha[0][0][0])
    result = cv2.addWeighted(foreground, 0 + alpha[0][0][0], new_background, 1 - alpha[0][0][0], 0)
    cv2.imshow('kam', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
blue_screen_matting(fg_path, bg_path)
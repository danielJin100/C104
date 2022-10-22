import cv2

img = cv2.imread("solar-system.jpg")
cv2.waitKey(0)
cv2.puttext("Sun", (200, 30), cv2.FONT_HERSEY_COMPLEX, 0.5 (255, 0, 0))
cv2.imwrite("solar system", img)
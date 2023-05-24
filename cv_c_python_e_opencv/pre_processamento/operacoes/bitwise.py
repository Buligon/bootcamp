import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img1, (100, 100), (250, 250), 255, -1)

img2 = np.zeros((300, 300), dtype="uint8")
cv2.circle(img2, (150, 150), 90, 255, -1)

fig, axes = plt.subplots(3, 2, figsize=(20, 10))

axes[0, 0].imshow(img1, cmap='gray')
axes[0, 1].imshow(img2, cmap='gray')

rect_and_circle = cv2.bitwise_and(img1, img2)
rect_or_circle = cv2.bitwise_or(img1, img2)
rect_xor_circle = cv2.bitwise_xor(img1, img2)
rect_not = cv2.bitwise_not(img1)

axes[1, 0].imshow(rect_and_circle, cmap='gray')
axes[1, 0].set_title('AND')
axes[1, 1].imshow(rect_or_circle, cmap='gray')
axes[1, 1].set_title('OR')
axes[2, 0].imshow(rect_xor_circle, cmap='gray')
axes[2, 0].set_title('XOR')
axes[2, 1].imshow(rect_not, cmap='gray')
axes[2, 1].set_title('NOT')


plt.tight_layout()
plt.show()

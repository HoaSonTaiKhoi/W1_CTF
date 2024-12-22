import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('C:/Code C/Python_Hash/nosa_art/artworks/0000c5e8-00d2-4806-89a2-f4204d1cd117.png')

# Chuyển đổi ảnh sang không gian màu HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Tạo một mảng chứa 5 ảnh
color_images = np.zeros((10, image.shape[0], image.shape[1], 3), dtype=np.uint8)

# Phân tách ảnh thành 5 màu khác nhau
for i in range(10):
#     # Tạo mặt nạ cho màu cụ thể
    lower_hue = int(360 / 5 * i) %255
    upper_hue = int(360 / 5 * (i + 1)) %255
    mask = cv2.inRange(hsv_image, (lower_hue, 50, 50), (upper_hue, 255, 255))
#     # Áp dụng mặt nạ để tách màu
    color_images[i] = cv2.bitwise_and(image, image, mask=mask)


# Hiển thị 5 ảnh đã tách
for i, color_image in enumerate(color_images):
    cv2.imshow(f"Color {i+1}", color_image)

# Đợi phím bấm để thoát
cv2.waitKey(0)
cv2.destroyAllWindows()
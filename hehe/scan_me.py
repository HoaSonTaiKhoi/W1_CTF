import cv2
from pyzbar.pyzbar import decode
def extract_frames_from_image(image_path, frame_width, frame_height):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    frames = []
    for y in range(0, height, frame_height):
        for x in range(0, width, frame_width):
            frame = image[y:y+frame_height, x:x+frame_width]
            frames.append(frame)

    return frames

# Đường dẫn tới hình ảnh chứa nhiều khung hình
image_path = "C:/Code C/Python_Hash/scan_me.png"

# Chiều rộng và chiều cao của khung hình
frame_width = 50
frame_height = 50

# Gọi hàm để tách các ảnh từ hình ảnh
frames = extract_frames_from_image(image_path, frame_width, frame_height)
list_qr=[]

# Lưu các ảnh tách được vào các tệp PNG
for i, frame in enumerate(frames):
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qr_codes = decode(gray_image)
    for qr in qr_codes:
        data=qr.data.decode()
        list_qr.append(data)

print (len(list_qr))

for i in list_qr:
    if i.startswith('W1'):
        print(i)
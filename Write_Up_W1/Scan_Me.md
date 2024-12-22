# ![](https://cnsc.uit.edu.vn/files/a5f4b16e6021acf91fc92de2f292a7a1/Challend.png)

# Scan Me

## Solution:
##### - Tải ảnh về, chúng ta phóng to lên nhận ra là các QRcode.
##### - Dùng opencv theo cách thông thường nó chỉ đọc được tầm vài chục cái QRcode.
![](https://scontent.fsgn5-10.fna.fbcdn.net/v/t1.15752-9/387594601_24075477272100438_6181227459586769753_n.png?_nc_cat=107&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=z-O8WCHSf5AAX-7Ae7B&_nc_ht=scontent.fsgn5-10.fna&oh=03_AdR96PK-VstBHuWjfKfWphtOSPnA3CYVkuRuw68K-Uev9Q&oe=6552D2D7)

##### - Dùng công cụ chỉnh sửa ảnh trong windows, ta thấy mỗi QRcode có kích cỡ 50x50.
##### - Nên chúng ta tạo một hàm đọc ảnh theo điểm ảnh:
![](https://scontent.fsgn5-9.fna.fbcdn.net/v/t1.15752-9/387584263_662220206012150_3136851494906321408_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=QRPdJ3gX9nsAX94gVra&_nc_ht=scontent.fsgn5-9.fna&oh=03_AdQyb7lhNk_JdlOAJo0yyI9bNRfSY5Q6PwwIDgzpeam_eg&oe=6552F1B9)
##### - frame = image[y:y+frame_height, x:x+frame_width], mỗi frame là một ảnh QR có kích thước 50x50.
#
![](https://scontent.fsgn5-15.fna.fbcdn.net/v/t1.15752-9/370199658_307549178649181_5357522953486533948_n.png?_nc_cat=111&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=TKBIiYwRMecAX-JrvVO&_nc_ht=scontent.fsgn5-15.fna&oh=03_AdTfsMy77UR_JCnO-XOsNcBda6IU_pmvNc6CWrJaZmvXtQ&oe=6552EFC3)
##### - Chuyển tất cả các ảnh thành đen trắng (grayscale) - cho chắc.
##### - Đồng thời giải mã tất cả QR có trong 1 frame bằng decode đến từ thư viện pyzbar.pyzbar.
##### - Trong list_qr là nội dung sau khi giải mã các QR, Lọc các dòng bắt đầu bằng `W1`:
# ![](https://scontent.fsgn5-10.fna.fbcdn.net/v/t1.15752-9/387525365_343031598097379_8911137711823578661_n.png?_nc_cat=107&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=QYQQ3o4BUKcAX_TAmOi&_nc_ht=scontent.fsgn5-10.fna&oh=03_AdTDld727BzdFbMEcwgYYqBfbFQoVGNNKCoqablXLSjhuQ&oe=6552CEA0)

# Flag: W1{do_anh_bat_duoc_em}
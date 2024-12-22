# ![](https://cnsc.uit.edu.vn/files/a5f4b16e6021acf91fc92de2f292a7a1/Challend.png)

# Scan Me 2

## Solution:
##### - Vì 2 file .csv nặng vãi. Nên em xem file 1.1G trước.
![](https://scontent.fsgn5-3.fna.fbcdn.net/v/t1.15752-9/387482076_348215084331855_1212931915781592492_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=6dQdiKTXYYoAX8-Z6-T&_nc_ht=scontent.fsgn5-3.fna&oh=03_AdSuGacmy4MwIZrYZHHv1yCj2dCkpl-hemyPfRHBnp2g5g&oe=6552F9DB)
##### - Tìm một hồi, ta thấy được cột Flag chỉ toàn giá trị 255 và 0.
##### - Trùng hợp mỗi cột trong file đều có độ dài là 291600=540x540. Trong file `solution.ipynb` có đề cập đến cái này:
![](https://scontent.fsgn5-9.fna.fbcdn.net/v/t1.15752-9/387526898_863127881753994_3282834397242582247_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=n0V0QZuRhhsAX9Y8MsI&_nc_ht=scontent.fsgn5-9.fna&oh=03_AdTr1WRpUA5bVC4-j7bBoMUKK8_fP1qzSchVTwUUBTQsGw&oe=6552FA5F)

#
##### - Lại phải dùng scatter:
![](https://scontent.fsgn5-2.fna.fbcdn.net/v/t1.15752-9/387583242_697408535314351_1167926187513873042_n.png?_nc_cat=105&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=QXnnda0glGEAX8lBs51&_nc_oc=AQkd6S4ZfHY2m7VtkE6kCP13ymzQ7oBIzFVwFZueZtMrNu8WajJZI6vH6137M-GRGrQ&_nc_ht=scontent.fsgn5-2.fna&oh=03_AdR-NKT-axYAebkcRl-7CN_QKQ7mSTZGbZmRcLOFMQ2Xow&oe=6552D7B5)
##### - Đọc cột thứ 115-"Flag" và chuyển nó thành mảng một chiều.
##### - Vì chỉ có giá trị 255 hoặc 0 nên t nghĩ ngay đến ảnh đen trắng.
##### - Dùng reshape của numpy để chuyển mảng 1 chiều thành mảng 2 chiều 540x540:
`matrix = np.reshape(temp_x, (int(np.sqrt(len(temp_x))), int(np.sqrt(len(temp_x)))))`
##### - Cuối cùng dùng maplotlib.pyplot để biến ma trận tìm được thành ảnh - mỗi giá trị trong ma trận là 1 điểm ảnh:
`plt.imshow(matrix, cmap='gray')` - cmap='gray' trong trường hợp này để giá trị 255 sẽ là trắng và 0 là đen.
##### - Đồng thời tắt trục trong biểu đồ và hiển thị ảnh lên:
`plt.axis('off')`

`plt.show()`
# ![](https://scontent.fsgn5-9.fna.fbcdn.net/v/t1.15752-9/370132032_287609754222087_9037142104476504715_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=KR3f8U0TqlEAX-7GzKw&_nc_ht=scontent.fsgn5-9.fna&oh=03_AdTxyr7Dleevy37HunVa7FGVL1S-oiciYHnV7OdL7wiYYg&oe=6552D942)
##### - Quét QR bằng điện thoại:
# ![](https://scontent.fsgn5-14.fna.fbcdn.net/v/t1.15752-9/385496029_539075801751222_8413617972369345747_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=XMA6btDGfnAAX9ao7iP&_nc_ht=scontent.fsgn5-14.fna&oh=03_AdRkTjxuDKXxN9g6aZUbwQfsPTkC_W9fohgInxHSRyG_xg&oe=6552FC7E)

# Flag: W1{N4NGD4UNGH3O}
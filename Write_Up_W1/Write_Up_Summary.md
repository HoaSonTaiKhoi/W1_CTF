# ![](https://cnsc.uit.edu.vn/files/a5f4b16e6021acf91fc92de2f292a7a1/Challend.png)

# I. Scan Me
- Tải ảnh về, chúng ta phóng to lên nhận ra là các QRcode.
- Dùng opencv theo cách thông thường nó chỉ đọc được tầm vài chục cái QRcode.
![](https://scontent.fsgn5-10.fna.fbcdn.net/v/t1.15752-9/387594601_24075477272100438_6181227459586769753_n.png?_nc_cat=107&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=z-O8WCHSf5AAX-7Ae7B&_nc_ht=scontent.fsgn5-10.fna&oh=03_AdR96PK-VstBHuWjfKfWphtOSPnA3CYVkuRuw68K-Uev9Q&oe=6552D2D7)

- Dùng công cụ chỉnh sửa ảnh trong windows, ta thấy mỗi QRcode có kích cỡ 50x50.
- Nên chúng ta tạo một hàm đọc ảnh theo điểm ảnh:
![](https://scontent.fsgn5-9.fna.fbcdn.net/v/t1.15752-9/387584263_662220206012150_3136851494906321408_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=QRPdJ3gX9nsAX94gVra&_nc_ht=scontent.fsgn5-9.fna&oh=03_AdQyb7lhNk_JdlOAJo0yyI9bNRfSY5Q6PwwIDgzpeam_eg&oe=6552F1B9)
- frame = image[y:y+frame_height, x:x+frame_width], mỗi frame là một ảnh QR có kích thước 50x50.
#
![](https://scontent.fsgn5-15.fna.fbcdn.net/v/t1.15752-9/370199658_307549178649181_5357522953486533948_n.png?_nc_cat=111&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=TKBIiYwRMecAX-JrvVO&_nc_ht=scontent.fsgn5-15.fna&oh=03_AdTfsMy77UR_JCnO-XOsNcBda6IU_pmvNc6CWrJaZmvXtQ&oe=6552EFC3)
- Chuyển tất cả các ảnh thành đen trắng (grayscale)- cho chắc.
- Đồng thời giải mã tất cả QR có trong 1 frame bằng decode đến từ thư viện pyzbar.pyzbar.
- Trong list_qr là nội dung sau khi giải mã các QR, Lọc các dòng bắt đầu bằng `W1`:
![](https://scontent.fsgn5-10.fna.fbcdn.net/v/t1.15752-9/387525365_343031598097379_8911137711823578661_n.png?_nc_cat=107&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=QYQQ3o4BUKcAX_TAmOi&_nc_ht=scontent.fsgn5-10.fna&oh=03_AdTDld727BzdFbMEcwgYYqBfbFQoVGNNKCoqablXLSjhuQ&oe=6552CEA0)

> Flag: W1{do_anh_bat_duoc_em}

#
# II. A Letter I Send Love To You
- Sau khi tải file .zip về và giải nén ra, ta thấy 100 file excel .csv mà mỗi file có đúng 2 cột.
- Nghĩ ngay đến scatter và matplotlib.pyplot:

# ![](https://scontent.fsgn5-3.fna.fbcdn.net/v/t1.15752-9/370351803_279252471739671_6168032560937470069_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=5dKhVDsxoYkAX8hBkiU&_nc_ht=scontent.fsgn5-3.fna&oh=03_AdRbWOFCN-iCA2EnX7JDHGA6TkeSwdTUmVwOI2dNOhA4Eg&oe=6552DCBB)

- Cho i chạy từ 1 đến 100, trong mỗi file .csv, lấy dữ liệu cột 0 và 1 chuyển thành mảng.
- Đồng thời vẽ biểu đồ tọa độ cho từng file.
- Kết quả:
# ![](https://scontent.fsgn5-11.fna.fbcdn.net/v/t1.15752-9/368584269_734518845184994_6295880807797623862_n.png?_nc_cat=110&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=rJjbZwpdoR4AX_gyilZ&_nc_ht=scontent.fsgn5-11.fna&oh=03_AdR7HyKgxbL_eezT6g3OiVH6afcwgyKqNn0iI9Hn4oPsAA&oe=6552EB96)

- Giảm height lại:
![](https://scontent.fsgn5-2.fna.fbcdn.net/v/t1.15752-9/387419558_1024682962112009_3182335570065611275_n.png?_nc_cat=105&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=sZJtTIWjfoUAX__WLvE&_nc_ht=scontent.fsgn5-2.fna&oh=03_AdRXD26k8QwLsVzb-dxpe9u8AecSBfMz7lUzkfwT2T7FMg&oe=6552C518)

> Flag: W1{TE4M_CUT3}

#
# III. Scan Me 2
- Vì 2 file .csv nặng vãi. Nên em xem file 1.1G trước.
![](https://scontent.fsgn5-3.fna.fbcdn.net/v/t1.15752-9/387482076_348215084331855_1212931915781592492_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=6dQdiKTXYYoAX8-Z6-T&_nc_ht=scontent.fsgn5-3.fna&oh=03_AdSuGacmy4MwIZrYZHHv1yCj2dCkpl-hemyPfRHBnp2g5g&oe=6552F9DB)
- Tìm một hồi, ta thấy được cột Flag chỉ toàn giá trị 255 và 0.
- Trùng hợp mỗi cột trong file đều có độ dài là 291600=540x540. Trong file `solution.ipynb` có đề cập đến cái này:
![](https://scontent.fsgn5-9.fna.fbcdn.net/v/t1.15752-9/387526898_863127881753994_3282834397242582247_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=n0V0QZuRhhsAX9Y8MsI&_nc_ht=scontent.fsgn5-9.fna&oh=03_AdTr1WRpUA5bVC4-j7bBoMUKK8_fP1qzSchVTwUUBTQsGw&oe=6552FA5F)

#
- Lại phải dùng scatter:
![](https://scontent.fsgn5-2.fna.fbcdn.net/v/t1.15752-9/387583242_697408535314351_1167926187513873042_n.png?_nc_cat=105&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=QXnnda0glGEAX8lBs51&_nc_oc=AQkd6S4ZfHY2m7VtkE6kCP13ymzQ7oBIzFVwFZueZtMrNu8WajJZI6vH6137M-GRGrQ&_nc_ht=scontent.fsgn5-2.fna&oh=03_AdR-NKT-axYAebkcRl-7CN_QKQ7mSTZGbZmRcLOFMQ2Xow&oe=6552D7B5)
- Đọc cột thứ 115-"Flag" và chuyển nó thành mảng một chiều.
- Vì chỉ có giá trị 255 hoặc 0 nên t nghĩ ngay đến ảnh đen trắng.
- Dùng reshape của numpy để chuyển mảng 1 chiều thành mảng 2 chiều 540x540:

`matrix = np.reshape(temp_x, (int(np.sqrt(len(temp_x))), int(np.sqrt(len(temp_x)))))`
- Cuối cùng dùng maplotlib.pyplot để biến ma trận tìm được thành ảnh- mỗi giá trị trong ma trận là 1 điểm ảnh:

`plt.imshow(matrix, cmap='gray')` - cmap='gray' trong trường hợp này để giá trị 255 sẽ là trắng và 0 là đen.
- Đồng thời tắt trục trong biểu đồ và hiển thị ảnh lên:

`plt.axis('off')`

`plt.show()`
# ![](https://scontent.fsgn5-9.fna.fbcdn.net/v/t1.15752-9/370132032_287609754222087_9037142104476504715_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=KR3f8U0TqlEAX-7GzKw&_nc_ht=scontent.fsgn5-9.fna&oh=03_AdTxyr7Dleevy37HunVa7FGVL1S-oiciYHnV7OdL7wiYYg&oe=6552D942)
- Quét QR bằng điện thoại:
# ![](https://scontent.fsgn5-14.fna.fbcdn.net/v/t1.15752-9/385496029_539075801751222_8413617972369345747_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=XMA6btDGfnAAX9ao7iP&_nc_ht=scontent.fsgn5-14.fna&oh=03_AdRkTjxuDKXxN9g6aZUbwQfsPTkC_W9fohgInxHSRyG_xg&oe=6552FC7E)

> Flag: W1{N4NGD4UNGH3O}

#
# IV. Send Me
- Ta tải về được một file có định dạng .file
- Sau một hồi kiểm tra thì thấy file này thực ra là file hdf5.
- Load model lên google colab và dùng summary() để hiện data của nó.
![](https://scontent.fsgn5-14.fna.fbcdn.net/v/t1.15752-9/387513664_3557103487902579_9093168272848134635_n.png?_nc_cat=101&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=iWjV7aWqVGMAX_NKQxE&_nc_ht=scontent.fsgn5-14.fna&oh=03_AdQ9Y_nqhgwBM0XPv_nQhfmUJ8QIO3_Xd6Eny6THnQqWGg&oe=6552E052)
#

- Ta thấy InputLayer(input_2) có Output Shape là [(None,120,254,1)]
- Suy ra, InputLayer là ảnh có một kênh duy nhất có kích thước 120x254(120 dòng và 254 cột)
- Ta cần tạo một ảnh đen trắng ngẫu nhiên cũng có kích thước 120X254:
![](https://scontent.fsgn5-8.fna.fbcdn.net/v/t1.15752-9/385517466_231840562950706_6832153391337550198_n.png?_nc_cat=109&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=O7qISLWnCsMAX8EmcKi&_nc_ht=scontent.fsgn5-8.fna&oh=03_AdSS92FVs5dBi0662EyjWlsXScxjf3qV3jU_IskJ24xvCg&oe=655378C8)
- Dùng thư viện numpy và maplotlib để tạo một ảnh grayscale ngẫu nhiên:

`np.random.choice()`- tạo một mảng mới với mảng đã cho.

`[0,255]`- mảng gồm giá trị 0 và 255, để 0 là đen và 255 là trắng.

`size=(120,254)`- mảng có kích thước 120x254.

`replace=True`- các giá trị trong mảng [0,255] có thể lặp lại trong mảng image.

`cmap='gray'`- để 0 hiển thị màu đen và 255 hiển thị màu trắng.
#

- Tạo một mảng chứa một phần tử duy nhất là ảnh grayscale đã tạo.
- Predict với input đã tạo và hiện kết quả đầu tiên được trả về từ model:
![](https://scontent.fsgn5-12.fna.fbcdn.net/v/t1.15752-9/387513618_656292686583952_1246355669930456769_n.png?_nc_cat=103&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=M_jKebgeoIcAX8Xvvrg&_nc_ht=scontent.fsgn5-12.fna&oh=03_AdQo6hKs3-iBNOWDLZn6pfgvYBPAHKYgSIz_n_JO0TamEg&oe=65538559)

> Flag: W1{n0w_u_kn0w_h0w_t0_pl4y}

#
# V. Echo In The Cosmos
- BigramLanguageModel trong solution là một mô hình dự đoán xác suất xảy ra của 2 từ liên tiếp.
- Copy class trong solution mà ban tổ chức cho sang google colab, thêm thư viện torch:
# ![](https://scontent.fsgn5-3.fna.fbcdn.net/v/t1.15752-9/387547792_2237515829776937_3551684022297025281_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=C83tJstUKvIAX9pSYFs&_nc_ht=scontent.fsgn5-3.fna&oh=03_AdTCgTqGfk-027AqeMVqt2wkmHjj9VSQTAkeeTplIyVsaw&oe=65530C2C)

- Tạo một thể hiện của class BigramLanguageModel với vocab_size=len(vocab)
![](https://scontent.fsgn5-3.fna.fbcdn.net/v/t1.15752-9/387417616_356680450126597_8928285468470905376_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=R-AeWS3DTywAX9zWtx5&_nc_ht=scontent.fsgn5-3.fna&oh=03_AdS7lypxkV47CXWcJ7Niitl2GqFZibHzhknesQ-S_ik9jQ&oe=65531542)
- Load thêm file .pth mà ban tổ chức cho,để khôi phục lại trạng thái của mô hình đã được huấn luyện và sử dụng nó để predict.
- model.eval() để mô hình hoạt động ở chế độ đánh giá.
#
- Vì mô hình này dự đoán xác suất xuất hiện của các từ tiếp theo trong vocab với input chúng ta nhập nên:
![](https://scontent.fsgn5-12.fna.fbcdn.net/v/t1.15752-9/393067250_853804742733398_3172555220561077817_n.png?_nc_cat=103&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=btnfX5n4edQAX_8i1nm&_nc_ht=scontent.fsgn5-12.fna&oh=03_AdSrruW-Tc8QPazeAJiwdrj5jXOLvog5YgsKnFC4W5j97A&oe=65531E2C)
-  đầu ra là `1` với input là tensor([58]) tức là `W`.
#
![](https://scontent.fsgn5-14.fna.fbcdn.net/v/t1.15752-9/393098638_351272624139530_1628815477415014808_n.png?_nc_cat=101&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=dlgbReXwjcAAX-zrwzq&_nc_ht=scontent.fsgn5-14.fna&oh=03_AdQtt3hqHMHBwjvVpwjMOU7qi3LlYm3r3tKg1yKYnS7kRw&oe=6553279B)
- đầu ra là `{` với input là tensor([1]) hay là `1`.
- Sau 2 lần cho dự đoán thì đầu ra đã có dạng: `W1{` giống với template.
#
- Ta code để `vocab[value]` ra đến `}` thì dừng- flag kết thúc bằng `}`:
# ![](https://scontent.fsgn5-12.fna.fbcdn.net/v/t1.15752-9/393084852_995036198488145_6487425733745609350_n.png?_nc_cat=103&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=hxPN5H7p3zYAX9Av5Lo&_nc_ht=scontent.fsgn5-12.fna&oh=03_AdSO2CSe4--0dvtiEN0wTvqwBxJJiu9HdfZ3UPdpjl0x6g&oe=655309CD)

> Flag: W1{unlock}
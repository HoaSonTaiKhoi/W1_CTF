# ![](https://cnsc.uit.edu.vn/files/a5f4b16e6021acf91fc92de2f292a7a1/Challend.png)

# Send me

### Solution:
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

`np.random.choice()` - tạo một mảng mới với mảng đã cho.

`[0,255]` - mảng gồm giá trị 0 và 255, để 0 là đen và 255 là trắng.

`size=(120,254)` - mảng có kích thước 120x254.

`replace=True` - các giá trị trong mảng [0,255] có thể lặp lại trong mảng image.

`cmap='gray'` - để 0 hiển thị màu đen và 255 hiển thị màu trắng.
#

- Tạo một mảng chứa một phần tử duy nhất là ảnh grayscale đã tạo.
- Predict với input đã tạo và hiện kết quả đầu tiên được trả về từ model:
![](https://scontent.fsgn5-12.fna.fbcdn.net/v/t1.15752-9/387513618_656292686583952_1246355669930456769_n.png?_nc_cat=103&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=M_jKebgeoIcAX8Xvvrg&_nc_ht=scontent.fsgn5-12.fna&oh=03_AdQo6hKs3-iBNOWDLZn6pfgvYBPAHKYgSIz_n_JO0TamEg&oe=65538559)

# Flag: W1{n0w_u_kn0w_h0w_t0_pl4y}
# ![](https://cnsc.uit.edu.vn/files/a5f4b16e6021acf91fc92de2f292a7a1/Challend.png)

# Echo In The Cosmos

## Solution:

##### - BigramLanguageModel trong solution là một mô hình dự đoán xác suất xảy ra của 2 từ liên tiếp.
##### - Copy class trong solution mà ban tổ chức cho sang google colab, thêm thư viện torch:
# ![](https://scontent.fsgn5-3.fna.fbcdn.net/v/t1.15752-9/387547792_2237515829776937_3551684022297025281_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=C83tJstUKvIAX9pSYFs&_nc_ht=scontent.fsgn5-3.fna&oh=03_AdTCgTqGfk-027AqeMVqt2wkmHjj9VSQTAkeeTplIyVsaw&oe=65530C2C)

##### - Tạo một thể hiện của class BigramLanguageModel với vocab_size=len(vocab)
![](https://scontent.fsgn5-3.fna.fbcdn.net/v/t1.15752-9/387417616_356680450126597_8928285468470905376_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=R-AeWS3DTywAX9zWtx5&_nc_ht=scontent.fsgn5-3.fna&oh=03_AdS7lypxkV47CXWcJ7Niitl2GqFZibHzhknesQ-S_ik9jQ&oe=65531542)
##### - Load thêm file .pth mà ban tổ chức cho,để khôi phục lại trạng thái của mô hình đã được huấn luyện và sử dụng nó để predict
##### - model.eval() để mô hình hoạt động ở chế độ đánh giá.
#
##### - Vì mô hình này dự đoán xác suất xuất hiện của các từ tiếp theo trong vocab với input chúng ta nhập nên:
![](https://scontent.fsgn5-12.fna.fbcdn.net/v/t1.15752-9/393067250_853804742733398_3172555220561077817_n.png?_nc_cat=103&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=btnfX5n4edQAX_8i1nm&_nc_ht=scontent.fsgn5-12.fna&oh=03_AdSrruW-Tc8QPazeAJiwdrj5jXOLvog5YgsKnFC4W5j97A&oe=65531E2C)
##### -  đầu ra là `1` với input là tensor([58]) tức là `W`
#
![](https://scontent.fsgn5-14.fna.fbcdn.net/v/t1.15752-9/393098638_351272624139530_1628815477415014808_n.png?_nc_cat=101&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=dlgbReXwjcAAX-zrwzq&_nc_ht=scontent.fsgn5-14.fna&oh=03_AdQtt3hqHMHBwjvVpwjMOU7qi3LlYm3r3tKg1yKYnS7kRw&oe=6553279B)
##### - đầu ra là `{` với input là tensor([1]) hay là `1`.
##### - Sau 2 lần cho dự đoán thì đầu ra đã có dạng: `W1{` giống với template.
#
##### - Ta code để `vocab[value]` ra đến `}` thì dừng - flag kết thúc bằng `}`:
# ![](https://scontent.fsgn5-12.fna.fbcdn.net/v/t1.15752-9/393084852_995036198488145_6487425733745609350_n.png?_nc_cat=103&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=hxPN5H7p3zYAX9Av5Lo&_nc_ht=scontent.fsgn5-12.fna&oh=03_AdSO2CSe4--0dvtiEN0wTvqwBxJJiu9HdfZ3UPdpjl0x6g&oe=655309CD)

# Flag: W1{unlock}
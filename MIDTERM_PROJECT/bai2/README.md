3.2 Demosaicing

- Cách chạy: cd vào thư mục bai2 và gõ lần lượt các câu lệnh sau vào terminal:

python bai2_demosaicing.py


- Giải thích: 
Variable Number of Gradients (VNG) là một thuật toán phổ biến để khử màu cho các hình ảnh mẫu của Bayer. Nó hoạt động bằng cách ước tính thông tin màu còn thiếu dựa trên thông tin độ dốc có trong ảnh. Ý tưởng cơ bản đằng sau thuật toán VNG là sử dụng thực tế là các pixel lân cận trong cùng một kênh màu có độ dốc cường độ tương tự nhau. Do đó, thuật toán ước tính các giá trị màu bị thiếu bằng cách xem độ dốc cường độ của các pixel lân cận và sử dụng thông tin này để nội suy các giá trị bị thiếu, điều này làm cho thuật toán thích ứng hơn với các nội dung hình ảnh và mức độ nhiễu khác nhau, dựa trên sự khác biệt về cường độ giữa các pixel lân cận. Các độ dốc này sau đó được sử dụng để ước tính các giá trị màu còn thiếu cho mỗi pixel trong hình ảnh mẫu của Bayer.

Thuật toán VNG đã được chứng minh là tạo ra kết quả chất lượng cao, đặc biệt đối với hình ảnh có độ nhiễu thấp và độ sắc nét cao. Tuy nhiên, nó có thể tương đối chậm so với các thuật toán giải mã khác do độ phức tạp tính toán của nó.

- Câu hỏi:
1. Máy ảnh của bạn có thực hiện ánh xạ tuyến tính đơn giản giữa các giá trị RAW và các giá trị cân bằng màu trong JPEG không? Một số máy ảnh cao cấp có chế độ RAW+JPEG, giúp việc so sánh này dễ dàng hơn nhiều?
+ Trả lời: Hầu hết các máy ảnh đều thực hiện ánh xạ tuyến tính đơn giản giữa các giá trị RAW và các giá trị cân bằng màu trong JPEG. Tuy nhiên, một số máy ảnh cao cấp cung cấp chế độ RAW+JPEG để ghi cả dữ liệu RAW và ảnh JPEG đã xử lý. Chế độ này cho phép chúng tôi so sánh hình ảnh RAW được khử màu với đầu ra JPEG của máy ảnh và đánh giá chất lượng của thuật toán khử màu.


- input: input_bayer.jpg
- output: giao diện Tkinter và ảnh input đã lọc màu


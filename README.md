# Bai-Tap-Lon-python
Bài 3. Trivia Challenge có GUI & file I/O
Đầu bài:
Chuyển chương trình Trivia Challenge (đọc câu hỏi từ file, Chapter 7) thành ứng dụng GUI.
Đầu vào – đầu ra:
Đầu vào: File định dạng câu hỏi (text) giống mẫu trong sách.
Đầu ra: Câu hỏi hiển thị, ô nhập đáp án, hiện điểm.
Tính năng yêu cầu:
Đọc file, bắt lỗi file không tồn tại hoặc format sai.
GUI: Label câu hỏi, Entry đáp án, nút “Nộp”, Label điểm.
Tính điểm, chuyển câu hỏi kế tiếp.
Nút “Kết thúc” hiển thị tổng điểm.
Kiểm tra & kết quả mẫu:
Câu “What is 2+2?” → Nhập “4” → +1 điểm, sang câu kế.
Nhập sai → không cộng điểm.
Các bước triển khai:
Viết module đọc file theo cấu trúc open_file(), next_block().
Class GUI với tkinter; Frame cho câu hỏi, Entry và Button.
Kết nối logic và giao diện, cập nhật câu hỏi & điểm.
# Bài làm 
#
# https://youtu.be/r2hic4hXPJE?si=IUT-zee6j9K01n8a

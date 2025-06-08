import tkinter as tk
from tkinter import messagebox

# Đọc file và xử lý định dạng
def open_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return content.strip().split("\n\n")
    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Không tìm thấy file {filename}")
        exit()

# Tách câu hỏi và đáp án
def parse_block(block):
    lines = block.strip().split("\n")
    question = lines[0]
    answers = lines[1:-1]
    correct_index = int(lines[-1].split(":")[1]) - 1
    return {"question": question, "answers": answers, "correct": correct_index}

# GUI Class
class TriviaApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Trivia Challenge")
        self.questions = questions
        self.current = 0
        self.score = 0
        self.selected = tk.IntVar()

        self.root.geometry("500x400")
        self.root.configure(bg="white")

        self.question_label = tk.Label(root, text="", font=("Arial", 16, "bold"), wraplength=480, bg="white", justify="center")
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected, value=i,
                                font=("Arial", 12), bg="white", anchor="w", width=50, justify="left",
                                indicatoron=False, padx=10, pady=8, relief="ridge", bd=2, selectcolor="#d0e8ff")
            rb.pack(pady=5)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(root, text="Nộp", command=self.submit, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(root, text="Điểm: 0", font=("Arial", 12), bg="white")
        self.score_label.pack()

        self.quit_button = tk.Button(root, text="Kết thúc", command=self.end_game, font=("Arial", 12), bg="#f44336", fg="white")
        self.quit_button.pack(pady=5)

        self.load_question()

    def load_question(self):
        if self.current >= len(self.questions):
            self.end_game()
            return

        q = self.questions[self.current]
        self.question_label.config(text=f"Câu {self.current + 1}: {q['question']}")
        self.selected.set(-1)

        for i in range(4):
            if i < len(q['answers']):
                self.radio_buttons[i].config(text=q['answers'][i], state=tk.NORMAL)
            else:
                self.radio_buttons[i].config(text="", state=tk.DISABLED)

    def submit(self):
        choice = self.selected.get()
        if choice == -1:
            messagebox.showwarning("Chưa chọn", "Bạn chưa chọn đáp án.")
            return

        correct = self.questions[self.current]["correct"]
        if choice == correct:
            self.score += 1

        self.score_label.config(text=f"Điểm: {self.score}")
        self.current += 1
        self.load_question()

    def end_game(self):
        messagebox.showinfo("Hoàn tất", f"Tổng điểm của bạn: {self.score}/{len(self.questions)}")
        self.root.quit()

# Chạy chương trình
def main():
    print("Đang chạy chương trình...")  # Thêm dòng này
    raw = open_file("questions.txt")
    print("Đã đọc xong file.")  # Thêm dòng này
    questions = [parse_block(q) for q in raw]
    print("Đã phân tích xong câu hỏi.")  # Thêm dòng này
    root = tk.Tk()
    app = TriviaApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()

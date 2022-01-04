import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog


class Code_injector:
    def __init__(self):
        self.text1 = "Get main file."
        self.text2 = "Get file to hide."

        self.root = tk.Tk()  # defining a window
        self.root.geometry("600x500")  # window size
        self.root.title("Code_injector")  # title

        self.file1 = ""  # file1 directory
        self.file2 = ""  # file2 directory
        ###########################################
        self.header = tk.Label(self.root, text="Hide your file in any file!!!", font=('Comic Sans MS', 16))
        self.header.pack()  # header label

        self.button_back1 = tk.Button(self.root, text="Back", font=('Arial', 13), command=self.back1)  # button go back to main menu from write state
        self.button_back2 = tk.Button(self.root, text="Back", font=('Arial', 13), command=self.back2)  # button go back to main menu from read state
        ###########################################
        #  options variable
        self.option_write_state = tk.IntVar()
        self.option_read_state = tk.IntVar()
        # options
        self.option_frame = tk.Frame(self.root)
        self.option_write = tk.Checkbutton(self.option_frame, text="Write", font=('Arial', 13),
                                           variable=self.option_write_state)
        self.option_read = tk.Checkbutton(self.option_frame, text="Read", font=('Arial', 13),
                                          variable=self.option_read_state)
        self.option_write.grid(row=0, column=0)
        self.option_read.grid(row=0, column=1)
        self.option_frame.pack(pady=10)
        ###########################################
        # buttons
        self.button_start = tk.Button(self.root, text="Start", font=('Arial', 13), command=self.check)  # button Start
        self.button_start.pack(pady=10)

        self.button_start_hide = tk.Button(self.root, text="Start", font=('Arial', 13), command=self.start_hide)  # button to hide file
        self.button_start_extract = tk.Button(self.root, text="Start", font=('Arial', 13), command=self.start_extract)  # button to extract file
        ###########################################
        # hide file
        self.label_file1 = tk.Label(self.root, text=self.text1, font=("Arial", 14))
        self.button_get_file1 = tk.Button(self.root, text="Get file", font=('Arial', 12), command=self.get_file1)

        self.label_file2 = tk.Label(self.root, text=self.text2, font=("Arial", 14))
        self.button_get_file2 = tk.Button(self.root, text="Get file", font=('Arial', 12), command=self.get_file2)
        ###########################################
        self.done_label = tk.Label(self.root, text="Done!", font=('Arial', 13))  # label show done
        ###########################################
        self.root.mainloop()  # main loop

    def check(self):
        if self.option_write_state.get() == 1 and self.option_read_state.get() == 0:
            self.hide()

        if self.option_write_state.get() == 0 and self.option_read_state.get() == 1:
            self.export()

        if self.option_write_state.get() == 1 and self.option_read_state.get() == 1:
            messagebox.showerror(title="Error.", message="You chose too many options!!!")

        if self.option_write_state.get() == 0 and self.option_read_state.get() == 0:
            messagebox.showerror(title="Error.", message="You chose nothing!!!")

    def start_hide(self):
        if self.file1 == "" or self.file2 == "":
            messagebox.showerror(title="Error.", message="You chose nothing!!!")
        else:
            with open(self.file2, 'rb') as f, open(self.file1, 'ab') as w:
                w.write(b"#!@" + bytes(self.file2[self.file2.index("."):], encoding='utf8') + b"#!@" + f.read())

    def start_extract(self):
        if self.file1 == "":
            messagebox.showerror(title="Error.", message="You chose nothing!!!")
        else:
            with open(self.file1, 'rb') as f:
                self.content = f.read()

            try:
                self.index = [self.content.index(b"#!@")]
                self.index.append(self.content.index(b"#!@", self.index[0]+3))
                self.extenction = self.content[self.index[0]+3:self.index[1]]
                self.extenction = str(self.extenction)
                self.__a = True
                while self.__a == True:
                    self.file_name = simpledialog.askstring("New file", "Enter a file name", )
                    if self.file_name == None or self.file_name == '':
                        messagebox.showerror("Error", "You don't enter a file name")
                    else:
                        self.__a = False

                with open(self.file_name + self.extenction[2:-1], "wb") as w:
                    w.write(self.content[self.index[1] + 3:])
            except ValueError:
                messagebox.showerror("Error", "There is nothing here. :(")
            self.done_label.pack()


    def hide(self):
        self.button_start.pack_forget()
        self.header.pack_forget()
        self.option_frame.pack_forget()

        self.button_back1.pack()
        self.label_file1.pack(pady=10)
        self.button_get_file1.pack()

        self.label_file2.pack(pady=10)
        self.button_get_file2.pack()
        self.button_start_hide.pack(pady=10)

    def export(self):
        self.button_start.pack_forget()
        self.header.pack_forget()
        self.option_frame.pack_forget()

        self.button_back2.pack()
        self.label_file1.pack()
        self.button_get_file1.pack()
        self.button_start_extract.pack()

    def get_file1(self):
        self.file1 = filedialog.askopenfilename(title="Choose a file")  # poprawić
        if self.file1 != "":
            self.label_file1.configure(text=self.file1)
        else:
            self.label_file1.configure(text=self.text1)

    def get_file2(self):
        self.file2 = filedialog.askopenfilename(title="Choose a file")
        if self.file2 != "":
            self.label_file2.configure(text=self.file2)
        else:
            self.label_file2.configure(text=self.text2)

    def back1(self):
        self.button_back1.pack_forget()
        self.label_file1.pack_forget()
        self.button_get_file1.pack_forget()
        self.file1 = ""
        self.label_file2.configure(text=self.text2)
        self.label_file1.configure(text=self.text1)

        self.label_file2.pack_forget()
        self.button_get_file2.pack_forget()
        self.button_start_hide.pack_forget()
        self.file2 = ""

        self.header.pack()
        self.option_write_state.set(0)
        self.option_frame.pack()
        self.button_start.pack()

    def back2(self):
        self.header.pack()
        self.option_read_state.set(0)
        self.option_frame.pack()
        self.button_start.pack()
        self.file1 = ""
        self.label_file1.configure(text=self.text1)

        self.button_back2.pack_forget()
        self.label_file1.pack_forget()
        self.button_get_file1.pack_forget()
        self.button_start_extract.pack_forget()


x = Code_injector()

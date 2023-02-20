import tkinter as tk
from pdf import *
from tkinter import filedialog as fd
from tkinter import simpledialog as sd

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('462x336')
        self.title('Pdf Manipulator')
        self.funcs = functions()

    def window(self):
        """
        
        """
        self.frame1 = tk.Frame(self)
        labelf = tk.Label(self.frame1, text='Options: ')
        option = tk.StringVar()
        option.set("Choose one option")
        options = []

        def select_answers():
            if option.get() == "Choose one option":
                return
            self.options(option.get())
            return

        for function in dir(functions):
            if not function.startswith('__') and not function=='select_file':
                options.append(function)

        option_menu = tk.OptionMenu(self.frame1, option, *options)
            
        submit = tk.Button(self.frame1, text="Submit", command=select_answers)

        labelf.grid(column=1, row=1)
        option_menu.grid(column=2, row=1)
        submit.grid(column=1, row=2)
        self.frame1.pack()

    def options(self, selected_option):
        """
        
        """
        self.frame1.pack_forget()
        match selected_option:
            case 'split_pdf':
                title = tk.Label(self, text='Split Pdf', font='monospace 20')
                title.pack()
                frame = tk.Frame(self)
                
                input_path = tk.StringVar()
                input_path.set('')
                output_path = tk.StringVar()
                output_path.set('')
                start_page = tk.StringVar()
                start_page.set('')
                end_page = tk.StringVar()
                end_page.set('')

                def split_pdfs(input_path, output_path, start_page, end_page):                    
                    result = self.funcs.split_pdf(str(input_path), str(output_path), int(start_page), int(end_page))
                    frame.pack_forget()
                    frame2 = tk.Frame(self)
                    label12 = tk.Label(frame2, text=result)
                    label12.pack()
                    back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (title.pack_forget(), frame2.pack_forget(), self.window()))
                    back_to_home.pack()
                    frame2.pack()

                submit_button = tk.Button(frame, text='Submit', command=lambda: split_pdfs(input_path=input_path.get(), output_path=output_path.get(), start_page=start_page.get(), end_page=end_page.get()))

                input_path_box = tk.Entry(frame, textvariable=input_path)
                output_path_box = tk.Entry(frame, textvariable=output_path)
                start_page_box = tk.Entry(frame, textvariable=start_page)
                end_page_box = tk.Entry(frame, textvariable=end_page)

                input_path_label = tk.Label(frame, text='Input Path: ')
                output_path_label = tk.Label(frame, text='Output Path: ')
                start_page_label = tk.Label(frame, text='Start Page: ')
                end_page_label = tk.Label(frame, text='End Page: ')

                input_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (input_path.set(self.funcs.select_file()), input_path_box.update()))
                output_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (output_path.set(self.funcs.select_file()), output_path_box.update()))

                back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

                input_path_label.grid(column=1, row=1)
                output_path_label.grid(column=1, row=2)
                start_page_label.grid(column=1, row=3)
                end_page_label.grid(column=1, row=4)
                
                input_path_icon_file.grid(column=3, row=1, padx=3, pady=2)
                output_path_icon_file.grid(column=3, row=2, padx=3, pady=2)

                input_path_box.grid(column=2, row=1)
                output_path_box.grid(column=2, row=2)
                start_page_box.grid(column=2, row=3, pady=2)
                end_page_box.grid(column=2, row=4, pady=3)

                submit_button.grid(column=1, row=5)

                back_to_homepage.grid(column=3, row=5, pady=10)

                frame.pack()
            
            case 'reduce_pdf_size':
                title = tk.Label(self, text="Reduce file size of a pdf", font='Sans-Serif 20')
                title.pack()
                frame = tk.Frame(self)

                input_path = tk.StringVar()
                input_path.set('')
                output_path = tk.StringVar()
                output_path.set('')

                def reduce_file_size(file, out_file):
                    result = self.funcs.reduce_pdf_size(file, out_file)
                    frame.pack_forget()
                    frame2 = tk.Frame(self)
                    label12 = tk.Label(frame2, text=result, font='sans-serif 15')
                    label12.pack()
                    back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (title.pack_forget(), frame2.pack_forget(), self.window()))
                    back_to_home.pack()
                    frame2.pack()

                input_path_box = tk.Entry(frame, textvariable=input_path)
                output_path_box = tk.Entry(frame, textvariable=output_path)

                input_path_label = tk.Label(frame, text='Input Path: ')
                output_path_label = tk.Label(frame, text='Output Path: ')

                input_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (input_path.set(self.funcs.select_file()), input_path_box.update()))
                output_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (output_path.set(self.funcs.select_file()), output_path_box.update()))

                submit_button = tk.Button(frame, text='Submit', command=lambda: reduce_file_size(input_path.get(), output_path.get()))
                back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

                input_path_label.grid(column=1, row=1)
                output_path_label.grid(column=1, row=2)

                input_path_icon_file.grid(column=3, row=1, padx=3, pady=2)
                output_path_icon_file.grid(column=3, row=2, padx=3, pady=2)

                input_path_box.grid(column=2, row=1)
                output_path_box.grid(column=2, row=2)

                submit_button.grid(column=1, row=5)

                back_to_homepage.grid(column=3, row=5, pady=10)

                frame.pack()
            
            case 'merge_pdfs':
                title = tk.Label(self, text="Merge Pdfs", font='Sans-Serif 20')
                title.pack()
                frame = tk.Frame(self)

                file1 = tk.StringVar()
                file1.set('')
                file2 = tk.StringVar()
                file2.set('')
                output_path = tk.StringVar()
                output_path.set('')

                def merge_pdfs(list_of_files, output_file):
                    result = self.funcs.merge_pdfs(list_of_files, output_file)
                    frame.pack_forget()
                    frame2 = tk.Frame(self)
                    label12 = tk.Label(frame2, text=result, font='sans-serif 15')
                    label12.pack()
                    back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (title.pack_forget(), frame2.pack_forget(), self.window()))
                    back_to_home.pack()
                    frame2.pack()

                file1_box = tk.Entry(frame, textvariable=file1)
                file2_box = tk.Entry(frame, textvariable=file2)
                output_path_box = tk.Entry(frame, textvariable=output_path)

                file1_label = tk.Label(frame, text='File 1: ')
                file2_label = tk.Label(frame, text='File 2: ')
                output_path_label = tk.Label(frame, text='Output Path: ')

                submit_button = tk.Button(frame, text='Submit', command=lambda: (frame.pack_forget(), merge_pdfs([file1.get(), file2.get()], output_path.get())))
                back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

                file1_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (file1.set(self.funcs.select_file()), file1_box.update()))
                file2_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (file2.set(self.funcs.select_file()), file2_box.update()))
                output_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (output_path.set(self.funcs.select_file()), output_path_box.update()))

                file1_label.grid(column=1, row=1)
                file2_label.grid(column=1, row=2)
                output_path_label.grid(column=1, row=3)

                file1_box.grid(column=2, row=1)
                file2_box.grid(column=2, row=2)
                output_path_box.grid(column=2, row=3)

                file1_path_icon_file.grid(column=3, row=1, padx=3, pady=2)
                file2_path_icon_file.grid(column=3, row=2, padx=3, pady=2)
                output_path_icon_file.grid(column=3, row=3, padx=3, pady=2)

                submit_button.grid(column=1, row=4)
                back_to_homepage.grid(column=3, row=5, pady=10)

                frame.pack()



if __name__=='__main__':
    gui = window()
    gui.window()
    gui.mainloop()
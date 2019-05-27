import tkinter


def main():
     window = tkinter.Tk()
     window.title("A test run")
     canvas = tkinter.Canvas(window, height=130, width=130)
     canvas.pack(fill=tkinter.BOTH, expand=1)

     for i in range(13):
         canvas.create_line(0, i*10, 120, i*10, fill="red")
         canvas.create_line(i*10, 0, i*10, 120, fill="red")

     window.mainloop()


if __name__ == "__main__":
     main() 
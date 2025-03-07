from tkinter import Button, Label, TclVersion, Tk


def _test():
    root = Tk()
    text = (
        f"This is Tcl/Tk version {TclVersion}\n"
        "This should be a cedilla: \xe7"
    )
    label = Label(root, text=text)
    label.pack()
    test = Button(
        root,
        text="Click me!",
        command=lambda root=root: root.test.configure(
            text="[%s]" % root.test["text"]
        ),
    )
    test.pack()
    root.test = test
    quit = Button(root, text="QUIT", command=root.destroy)
    quit.pack()
    # The following three commands are needed so the window pops
    # up on top on Windows...
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()


if __name__ == "__main__":
    _test()

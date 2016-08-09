try:  # Python 2
    from Tkinter import *  # noqa
except ImportError:  # Python 3
    from tkinter import *  # noqa


class ScrolledListbox(Listbox):
    def __init__(
            self, master,
            vert_scroll=True,
            horiz_scroll=True,
            **kwargs
            ):
        self.hbar = None
        self.vbar = None
        self.frame = Frame(
            master,
            borderwidth=1,
            highlightthickness=0,
            relief=SUNKEN,
        )
        if vert_scroll:
            self.vbar = Scrollbar(
                self.frame,
                orient=VERTICAL,
                command=self.yview,
            )
            kwargs.setdefault('yscrollcommand', self.vbar.set)
        if horiz_scroll:
            self.hbar = Scrollbar(
                self.frame,
                orient=HORIZONTAL,
                command=self.xview,
            )
            kwargs.setdefault('xscrollcommand', self.hbar.set)
        Listbox.__init__(self, self.frame, **kwargs)
        Listbox.grid(self, row=0, column=0, sticky=N+S+E+W)
        if vert_scroll:
            self.vbar.grid(row=0, column=1, sticky=N+S)
        if horiz_scroll:
            self.hbar.grid(row=1, column=0, sticky=E+W)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

    def grid(self, *args, **kwargs):
        return self.frame.grid(*args, **kwargs)

    def pack(self, *args, **kwargs):
        return self.frame.pack(*args, **kwargs)

    def place(self, *args, **kwargs):
        return self.frame.place(*args, **kwargs)


if __name__ == "__main__":
    def main():
        tk = Tk()
        lbox = ScrolledListbox(
            tk,
            horiz_scroll=False,
            vert_scroll=True,
            width=30,
            height=15,
        )
        lbox.pack(side=TOP, fill=BOTH, expand=1)
        for i in range(1,51):
            lbox.insert(END, "Item %d" % i)
        tk.mainloop()

    main()


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap

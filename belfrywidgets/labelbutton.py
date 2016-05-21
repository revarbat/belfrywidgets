try:
    from Tkinter import *  # noqa
except:
    from tkinter import *  # noqa


class LabelButton(Label):
    def __init__(self, master, command=None, **kwargs):
        kwargs.setdefault('highlightthickness', 0)
        kwargs.setdefault('borderwidth', 1)
        kwargs.setdefault('takefocus', 1)
        kwargs.setdefault('relief', FLAT)
        Label.__init__(self, master, **kwargs)
        self.bind('<Enter>', self._evt_enter)
        self.bind('<FocusIn>', self._evt_enter)
        self.bind('<Leave>', self._evt_leave)
        self.bind('<FocusOut>', self._evt_leave)
        self.bind('<ButtonPress-1>', self._evt_button_press)
        self.bind('<ButtonRelease-1>', self._evt_button_release)
        self.bind('<Key-space>', self._evt_activate)
        self.master = master
        self.command = command
        self.downin = False
        self.inside = False

    def _shade(self, color, mult=0.75):
        r, g, b = self.master.winfo_rgb(color)
        r = int(r // (256 / mult))
        g = int(g // (256 / mult))
        b = int(b // (256 / mult))
        return "#%02x%02x%02x" % (r, g, b)

    def _evt_enter(self, event):
        bg = self._shade(self.master.cget('background'), 0.75)
        self.config(background=bg)
        if self.downin:
            self.config(relief=SUNKEN)
        self.inside = True

    def _evt_leave(self, event):
        bg = self.master.cget('background')
        self.config(background=bg)
        if self.downin:
            self.config(relief=FLAT)
        self.inside = False

    def _evt_button_press(self, event):
        self.config(relief=SUNKEN)
        self.downin = True

    def _evt_button_release(self, event):
        self.config(relief=FLAT)
        if self.downin and self.inside and self.command:
            self.command()
        self.downin = False

    def _evt_activate(self, event):
        if self.command:
            self.command()


if __name__ == "__main__":
    tk = Tk()
    b1 = LabelButton(tk, text="Button 1", command=lambda: print("B1!"))
    b2 = LabelButton(tk, text="Button 2", command=lambda: print("B2!"))
    b1.pack(side=TOP, padx=20, pady=20)
    b2.pack(side=TOP, padx=20, pady=20)
    tk.mainloop()

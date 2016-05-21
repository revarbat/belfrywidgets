import platform
try:
    from Tkinter import *  # noqa
except:
    from tkinter import *  # noqa

from belfrywidgets.labelbutton import LabelButton


class TabbedNoteBook(Frame):
    def __init__(
        self,
        master,
        width=640,
        height=480,
        **kwargs
    ):
        self.master = master
        self.selected_pane = StringVar()
        self.pane_names = []
        self.panes = {}
        self.tabs = {}
        self.font = kwargs.get('font', ('Helvetica', '10'))
        Frame.__init__(
            self,
            master,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
            width=width,
            height=height,
            relief=FLAT,
        )
        self.tabsfr = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
        )
        self.holder = Frame(
            self,
            borderwidth=0,
            relief=FLAT,
        )
        self.tabsfr.pack(side=TOP, fill=X, expand=0)
        self.holder.pack(side=TOP, fill=BOTH, expand=1)
        tl = self.winfo_toplevel()
        if platform.system() == "Darwin":
            tl.bind('<Command-Shift-braceright>', self._nextpane)
            tl.bind('<Command-Shift-braceleft>', self._prevpane)
            tl.bind('<Command-Shift-Right>', self._nextpane)
            tl.bind('<Command-Shift-Left>', self._prevpane)
        else:
            tl.bind('<Control-Tab>', self._nextpane)
            tl.bind('<Shift-Control-Tab>', self._prevpane)
        self.config(**kwargs)

    def config(self, **kwargs):
        for k, v in kwargs.items():
            if k in ['font']:
                if k == 'font':
                    self.font = v
                for name, tab in self.tabs.items():
                    for sub in tab.winfo_children():
                        try:
                            sub.config(**{k: v})
                        except:
                            pass

    def add_pane(self, name, label, closecommand=None):
        tab = Frame(
            self.tabsfr,
            borderwidth=1,
            relief=SOLID,
        )
        tab.name = name
        tab.closebtn = None
        tab.closecommand = closecommand
        if closecommand:
            tab.closebtn = LabelButton(
                tab,
                text=" ",
                width=1,
                font=('Helvetica', '10'),
                command=lambda w=tab: self._close_tab(w),
            )
            tab.closebtn.tab = tab
            tab.closebtn.pack(side=LEFT, fill=Y)
            tab.closebtn.bind('<FocusIn>', self._closebtn_focusin, add='+')
            tab.closebtn.bind('<FocusOut>', self._closebtn_focusout, add='+')
        tab.label = Label(tab, text=label, font=self.font)
        tab.label.pack(side=TOP, fill=BOTH, expand=0)
        tab.label.bind('<1>', lambda event, n=name: self._setpane(n))
        tab.pack(side=LEFT, fill=BOTH, expand=1)
        tab.bind('<1>', lambda event, n=name: self._setpane(n))
        tab.bind('<Enter>', self._tab_enter)
        tab.bind('<Leave>', self._tab_leave)
        newpane = Frame(
            self.holder,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
        )
        tab.pane = newpane
        if not self.panes:
            self.selected_pane.set(name)
        self.pane_names.append(name)
        self.panes[name] = newpane
        self.tabs[name] = tab
        self._update_tabs()
        return newpane

    def _close_tab(self, w):
        if w.closecommand:
            if w.closecommand():
                del self.tabs[w.name]
                del self.panes[w.name]
                self.pane_names.remove(w.name)
                w.pane.destroy()
                w.destroy()

    def _tab_enter(self, event):
        if event.widget.closebtn:
            event.widget.closebtn.config(text=u'X')

    def _tab_leave(self, event):
        if event.widget.closebtn:
            event.widget.closebtn.config(text=' ')

    def _closebtn_focusin(self, event):
        event.widget = event.widget.tab
        self._tab_enter(event)

    def _closebtn_focusout(self, event):
        event.widget = event.widget.tab
        self._tab_leave(event)

    def _setpane(self, name):
        self.selected_pane.set(name)
        self._update_tabs()

    def _update_tabs(self):
        for child in self.holder.winfo_children():
            child.forget()
        selpane = self.selected_pane.get()
        for name, tab in self.tabs.items():
            color = '#ddd' if name == selpane else '#aaa'
            for sub in tab.winfo_children():
                sub.config(background=color)
            tab.config(background=color)
        newpane = self.panes[selpane]
        newpane.pack(side=TOP, fill=BOTH, expand=1)

    def _prevpane(self, event=None):
        selpane = self.selected_pane.get()
        pos = self.pane_names.index(selpane)
        pos -= 1
        self.selected_pane.set(self.pane_names[pos])
        self._update_tabs()

    def _nextpane(self, event=None):
        selpane = self.selected_pane.get()
        pos = self.pane_names.index(selpane)
        pos += 1
        pos %= len(self.pane_names)
        self.selected_pane.set(self.pane_names[pos])
        self._update_tabs()


if __name__ == "__main__":
    def _closeit(name):
        print("Close tab %s" % name)
        # Return true to allow tab to be closed.
        return True

    def main():
        tk = Tk()
        tnb = TabbedNoteBook(tk, width=640, height=480)
        tnb.pack_propagate(False)  # Keep noteboox from shrinking
        tnb.pack(side=TOP, fill=BOTH, expand=1)

        pane1 = tnb.add_pane(
            'one', 'First Pane',
            closecommand=lambda: _closeit('one')
        )
        lbl1 = Label(pane1, text="This is a label.")
        lbl1.pack(side=TOP, fill=BOTH, expand=1)

        pane2 = tnb.add_pane(
            'two', 'Second Pane',
            closecommand=lambda: _closeit('two')
        )
        lbl2 = Label(pane2, text="This is a second label.")
        lbl2.pack(side=TOP, fill=BOTH, expand=1)

        pane3 = tnb.add_pane(
            'three', 'Third Pane',
            closecommand=lambda: _closeit('three')
        )
        lbl3 = Label(pane3, text="This is a third label.")
        lbl3.pack(side=TOP, fill=BOTH, expand=1)

        tk.mainloop()

    main()


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap

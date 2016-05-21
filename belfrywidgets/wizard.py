try:
    from Tkinter import *  # noqa
except:
    from tkinter import *  # noqa


class Wizard(Toplevel):
    def __init__(
        self,
        width=640,
        height=480,
        cancelcommand=None,
        finishcommand=None,
        **kwargs
    ):
        self.selected_pane = None
        self.pane_names = []
        self.panes = {}
        self.font = kwargs.get('font', ('Helvetica', '10'))
        self.cancel_command = cancelcommand
        self.finish_command = finishcommand
        Toplevel.__init__(
            self,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
            relief=FLAT,
        )
        self.holder = Frame(
            self,
            borderwidth=0,
            relief=FLAT,
        )
        self.btnsfr = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
        )
        self.prevbtn = Button(
            self.btnsfr,
            text="< Prev",
            width=6,
            command=self._prevpane,
        )
        self.nextbtn = Button(
            self.btnsfr,
            text="Next >",
            width=6,
            command=self._nextpane,
        )
        self.fnshbtn = Button(
            self.btnsfr,
            text="Finish",
            width=6,
            command=self._finish,
        )
        self.cnclbtn = Button(
            self.btnsfr,
            text="Cancel",
            width=6,
            command=self._cancel,
        )
        self.cnclbtn.pack(side=RIGHT, fill=Y, expand=0, padx=10, pady=10)
        self.fnshbtn.pack(side=RIGHT, fill=Y, expand=0, padx=20, pady=10)
        self.nextbtn.pack(side=RIGHT, fill=Y, expand=0, padx=10, pady=10)
        self.prevbtn.pack(side=RIGHT, fill=Y, expand=0, padx=0, pady=10)

        self.holder.pack(side=TOP, fill=BOTH, expand=1)
        self.btnsfr.pack(side=TOP, fill=X, expand=0)

        self.wm_geometry("%dx%d" % (width, height))
        self.protocol('WM_DELETE_WINDOW', self._cancel)

    def add_pane(self, name, label):
        newpane = Frame(
            self.holder,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
        )
        if not self.panes:
            self.selected_pane = name
        self.pane_names.append(name)
        self.panes[name] = newpane
        self._update()
        return newpane

    def _update(self):
        selpane = self.selected_pane
        if not self.pane_names or selpane == self.pane_names[0]:
            self.prevbtn.config(state='disabled')
        else:
            self.prevbtn.config(state='normal')

        if not self.pane_names or selpane == self.pane_names[-1]:
            self.nextbtn.config(state='disabled')
        else:
            self.nextbtn.config(state='normal')

        if self.finish_command:
            self.fnshbtn.config(state='normal')
        else:
            self.fnshbtn.config(state='disabled')

        if self.cancel_command:
            self.cnclbtn.config(state='normal')
        else:
            self.cnclbtn.config(state='disabled')

        for child in self.holder.winfo_children():
            child.forget()
        newpane = self.panes[selpane]
        newpane.pack(side=TOP, fill=BOTH, expand=1)
        self.update_idletasks()
        self.update_idletasks()

    def _prevpane(self, event=None):
        selpane = self.selected_pane
        pos = self.pane_names.index(selpane)
        if pos > 0:
            pos -= 1
        self.selected_pane = self.pane_names[pos]
        self._update()

    def _nextpane(self, event=None):
        selpane = self.selected_pane
        pos = self.pane_names.index(selpane)
        if pos < len(self.pane_names) - 1:
            pos += 1
        self.selected_pane = self.pane_names[pos]
        self._update()

    def _finish(self, event=None):
        self.destroy()
        if self.finish_command:
            self.finish_command()

    def _cancel(self, event=None):
        self.destroy()
        if self.cancel_command:
            self.cancel_command()


if __name__ == "__main__":
    def _finish():
        print("Finish")

    def _cancel():
        print("Cancel")

    def main():
        root = Tk()
        wiz = Wizard(
            width=640,
            height=480,
            cancelcommand=_cancel,
            finishcommand=_finish,
        )

        pane1 = wiz.add_pane('one', 'First')
        lbl1 = Label(pane1, text="This is the first pane.")
        lbl1.pack(side=TOP, fill=BOTH, expand=1)

        pane2 = wiz.add_pane('two', 'Second')
        lbl2 = Label(pane2, text="This is the second pane.")
        lbl2.pack(side=TOP, fill=BOTH, expand=1)

        pane3 = wiz.add_pane('three', 'Third')
        lbl3 = Label(pane3, text="This is the third pane.")
        lbl3.pack(side=TOP, fill=BOTH, expand=1)

        root.wm_withdraw()
        root.wait_window(wiz)

    main()


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap

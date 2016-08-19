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
            default_button="finish",
            **kwargs
            ):
        self.selected_pane = None
        self.pane_entry_cmds = {}
        self.pane_prev_cmds = {}
        self.pane_next_cmds = {}
        self.pane_names = []
        self.panes = {}
        self.font = kwargs.get('font', ('Helvetica', '10'))
        self.cancel_command = cancelcommand
        self.finish_command = finishcommand
        self.prev_enabled = True
        self.next_enabled = True
        self.finish_enabled = True
        self.cancel_enabled = True
        self.default_button = default_button
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

    def add_pane(
            self, name, label,
            entrycommand=None,
            prevcommand=None,
            nextcommand=None,
            ):
        newpane = Frame(
            self.holder,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
        )
        if not self.panes:
            self.selected_pane = name
            if entrycommand:
                self.after(0, entrycommand)
        self.pane_names.append(name)
        self.panes[name] = newpane
        self.pane_entry_cmds[name] = entrycommand
        self.pane_prev_cmds[name] = prevcommand
        self.pane_next_cmds[name] = nextcommand
        self._update()
        return newpane

    def del_pane(self, name):
        if name == self.selected_pane:
            idx = self.pane_names.index(name)
            panecnt = len(self.pane_names)
            if panecnt == 1:
                self.selected_pane = None
            elif idx == panecnt - 1:
                self._prevpane()
            else:
                self._nextpane()
        del (self.pane_entry_cmds[pane])
        del (self.pane_prev_cmds[pane])
        del (self.pane_next_cmds[pane])
        del (self.panes[pane])
        self.pane_names.remove(pane)

    def show_pane(self, newpane):
        if newpane not in self.pane_names:
            raise ValueError("No pane with the name '%s' exists." % newpane)
        self.selected_pane = newpane
        entrycmd = self.pane_entry_cmds[newpane]
        if entrycmd:
            entrycmd()
        self._update()

    def set_prev_enabled(self, enable=True):
        self.prev_enabled = enable
        self._update()

    def set_next_enabled(self, enable=True):
        self.next_enabled = enable
        self._update()

    def set_finish_enabled(self, enable=True):
        self.finish_enabled = enable
        self._update()

    def set_cancel_enabled(self, enable=True):
        self.cancel_enabled = enable
        self._update()

    def set_prev_text(self, text="< Prev"):
        self.prevbtn.config(text=text)
        self._update()

    def set_next_text(self, text="Next >"):
        self.nextbtn.config(text=text)
        self._update()

    def set_finish_text(self, text="Finish"):
        self.fnshbtn.config(text=text)
        self._update()

    def set_cancel_text(self, text="Cancel"):
        self.cnclbtn.config(text=text)
        self._update()

    def set_default_button(self, btn="finish"):
        self.default_button = btn
        self._update()

    def _update(self):
        selpane = self.selected_pane
        prev_state = 'normal'
        next_state = 'normal'
        finish_state = 'normal'
        cancel_state = 'normal'
        if not self.pane_names or selpane == self.pane_names[0]:
            prev_state = 'disabled'
        if not self.prev_enabled:
            prev_state = 'disabled'
        if not self.pane_names or selpane == self.pane_names[-1]:
            next_state = 'disabled'
        if not self.next_enabled:
            next_state = 'disabled'
        if not self.finish_command or not self.finish_enabled:
            finish_state = 'disabled'
        if not self.cancel_command or not self.cancel_enabled:
            cancel_state = 'disabled'
        self.prevbtn.config(state=prev_state)
        self.nextbtn.config(state=next_state)
        self.fnshbtn.config(state=finish_state)
        self.cnclbtn.config(state=cancel_state)
        for child in self.holder.winfo_children():
            child.forget()
        if self.pane_names:
            newpane = self.panes[selpane]
            newpane.pack(side=TOP, fill=BOTH, expand=1)
        prev_def = "active" if self.default_button == "prev" else "normal"
        next_def = "active" if self.default_button == "next" else "normal"
        finish_def = "active" if self.default_button == "finish" else "normal"
        cancel_def = "active" if self.default_button == "cancel" else "normal"
        self.prevbtn.config(default=prev_def)
        self.nextbtn.config(default=next_def)
        self.fnshbtn.config(default=finish_def)
        self.cnclbtn.config(default=cancel_def)
        self.bind('<Return>', self._invoke_default)
        self.update_idletasks()
        self.update_idletasks()

    def _invoke_default(self, event=None):
        if self.default_button == "prev":
            self.prevbtn.invoke()
        elif self.default_button == "next":
            self.nextbtn.invoke()
        elif self.default_button == "finish":
            self.fnshbtn.invoke()
        elif self.default_button == "cancel":
            self.cnclbtn.invoke()
        return "break"

    def _prevpane(self, event=None):
        oldpane = self.selected_pane
        prevcmd = self.pane_prev_cmds[oldpane]
        if prevcmd:
            prevcmd()
        if oldpane != self.selected_pane:
            return
        pos = self.pane_names.index(oldpane)
        if pos > 0:
            pos -= 1
        self.show_pane(self.pane_names[pos])

    def _nextpane(self, event=None):
        oldpane = self.selected_pane
        nextcmd = self.pane_next_cmds[oldpane]
        if nextcmd:
            nextcmd()
        if oldpane != self.selected_pane:
            return
        pos = self.pane_names.index(oldpane)
        if pos < len(self.pane_names) - 1:
            pos += 1
        self.show_pane(self.pane_names[pos])

    def _finish(self, event=None):
        self.destroy()
        if self.finish_command:
            self.finish_command()

    def _cancel(self, event=None):
        self.destroy()
        if self.cancel_command:
            self.cancel_command()


if __name__ == "__main__":
    def main():
        root = Tk()
        wiz = Wizard(
            width=640,
            height=480,
            cancelcommand=lambda: print("Cancel"),
            finishcommand=lambda: print("Finish"),
        )

        def disable_finish():
            wiz.set_finish_enabled(False)

        def enable_finish():
            wiz.set_finish_enabled(True)

        wiz.set_default_button('next')
        pane1 = wiz.add_pane('one', 'First', entrycommand=disable_finish)
        lbl1 = Label(pane1, text="This is the first pane.")
        lbl1.pack(side=TOP, fill=BOTH, expand=1)

        pane2 = wiz.add_pane( 'two', 'Second')
        lbl2 = Label(pane2, text="This is the second pane.")
        lbl2.pack(side=TOP, fill=BOTH, expand=1)

        pane3 = wiz.add_pane(
            'three', 'Third',
            entrycommand=enable_finish,
            prevcommand=disable_finish
        )
        lbl3 = Label(pane3, text="This is the third pane.")
        lbl3.pack(side=TOP, fill=BOTH, expand=1)

        # wiz.show_pane('two')
        # wiz.del_pane('two')
        # wiz.set_prev_enabled(True)
        # wiz.set_next_enabled(True)

        root.wm_withdraw()
        root.wait_window(wiz)

    main()


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap

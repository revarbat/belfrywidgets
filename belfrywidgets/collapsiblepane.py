try:
    from Tkinter import *  # noqa
except:
    from tkinter import *  # noqa


class CollapsiblePane(LabelFrame):
    def __init__(self, master, **kwargs):
        self.master = master
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.text = kwargs.get('text', '')
        self.visible = kwargs.get('visible', True)
        self.collapsible = kwargs.get('collapsible', False)
        self.collapsed = kwargs.get('collapsed', False)
        LabelFrame.__init__(
            self,
            self.master,
            text=self.text,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
            relief=FLAT,
        )
        self.holder = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
            relief=FLAT,
        )
        self.bind('<1>', self._toggle)
        self.config(**kwargs)

    def config(self, **kwargs):
        if 'visible' in kwargs:
            self.visible = kwargs['visible']
            if self.visible:
                kwargs['borderwidth'] = 2
                kwargs['relief'] = GROOVE
            else:
                kwargs['borderwidth'] = 0
                kwargs['relief'] = FLAT
        if 'collapsed' in kwargs:
            self.collapsed = kwargs['collapsed']
        if 'collapsible' in kwargs:
            self.collapsible = kwargs['collapsible']
        if 'text' in kwargs:
            self.text = kwargs['text']
        for k, v in kwargs.items():
            if k in [
                'font', 'text', 'width', 'height', 'relief', 'borderwidth'
            ]:
                Frame.config(self, **{k: v})

        if not self.collapsible or not self.collapsed:
            self.holder.config(height=None)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.holder.grid(row=0, column=0, sticky=N+S+E+W)
        else:
            self.holder.config(height=20)
            self.holder.grid_remove()

    def _toggle(self, event=None):
        if self.collapsible:
            self.config(collapsed=not self.collapsed)
        else:
            self.config(collapsed=False)


if __name__ == "__main__":
    tk = Tk()
    cp = CollapsiblePane(
        tk,
        text="Collapsible",
        visible=True,
        collapsible=True,
    )
    cp.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)

    lbl1 = Label(cp.holder, text="This is a text message.")
    lbl1.pack(side=TOP)

    tk.mainloop()

# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap

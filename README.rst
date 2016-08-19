BelfryWidets
============

A collection of useful Tkinter widgets and mega-widgets.

This package contains:

CollapsiblePane:
  A LabelFrame derivitive that can be collapsed by clicking on the label.

LabelButton:
  A Label derivitive that is clickable like a button, with rollovers and focus.

TabbedNoteBook:
  A notebook that provides Safari-style tabs, with optional close-buttons
  per tab.

Wizard:
  A wizard dialog with Prev/Next/Finish/Cancel buttons, which progresses
  through multiple panes of widgets.

ScrolledListbox:
  A Listbox widget with scrollbars, similar to the ScrolledText widget.

ProgressBar:
  A rounded progress bar, similar in function to tkinter.ttk.Progressbar,
  except that the colors are more controllable on all platforms.

ToolTip:
  Attaches a tooltip to a widget, so that hovering over that widget will
  show a small tooltip message.


CollapsiblePane
---------------
Example code::

    from belfrywidgets import CollapsiblePane

    tk = Tk()
    cp = CollapsiblePane(
        tk,
        text="Click Here to Collapse",
        visible=True,
        collapsible=True,
    )
    cp.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
    lbl1 = Label(cp.holder, text="This is a label.")
    lbl2 = Label(cp.holder, text="This is another label.")
    lbl1.pack(side=TOP)
    lbl2.pack(side=TOP)
    tk.mainloop()


LabelButton
-----------
Example code::

    from belfrywidgets import LabelButton
    tk = Tk()
    b1 = LabelButton(tk, text="Button 1", command=lambda: print("B1!"))
    b2 = LabelButton(tk, text="Button 2", command=lambda: print("B2!"))
    b1.pack(side=TOP, padx=20, pady=20)
    b2.pack(side=TOP, padx=20, pady=20)
    tk.mainloop()


TabbedNoteBook
--------------
Example code::

    from belfrywidgets import TabbedNoteBook

    def _closeit(name):
        print("Close tab %s" % name)
        return True  # Return True to allow closing tab.

    tk = Tk()
    tnb = TabbedNoteBook(tk, width=640, height=480)
    tnb.pack_propagate(False)  # Keep noteboox from shrinking to fit contents.
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

    lbl = tnb.pane_label('two')
    lbl.config(text="Tab 2")

    tk.mainloop()


Wizard
------
Example code::

    from belfrywidgets import Wizard

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


ScrolledListbox
---------------
Example code::

    from belfrywidgets import Wizard

    root = Tk()
    lbox = ScrolledListbox(
        root,
        horiz_scroll=False,
        vert_scroll=True,
        width=30,
        height=15,
    )
    lbox.pack(side=TOP, fill=BOTH, expand=1)
    for i in range(1,51):
        lbox.insert(END, "Item %d" % i)
    tk.mainloop()

ProgressBar
-----------
Indeterminate mode example code::

    from belfrywidgets import ProgressBar, INDETERMINATE

    tk = Tk()
    tk.config(background="#446")
    pb = ProgressBar(
        tk, mode=INDETERMINATE,
        bordercolor="#446",
        foreground="red",
        background="cyan"
    )
    pb.pack(fill=BOTH, expand=1, padx=10, pady=10)
    pb.start()
    tk.after(20000, pb.stop)
    tk.mainloop()

Determinate mode example code::

    from belfrywidgets import ProgressBar, DETERMINATE

    tk = Tk()
    tk.config(background="#446")
    v = DoubleVar()
    v.set(0.0)
    pb = ProgressBar(
        tk, mode=DETERMINATE,
        maximum=200,
        variable=v,
        bordercolor="#446",
        foreground="red",
        background="cyan"
    )
    pb.pack(fill=BOTH, expand=1, padx=10, pady=10)

    def inc():
        v.set(v.get()+1)
        if v.get() < 200:
            tk.after(100, inc)

    inc()
    tk.mainloop()


ToolTip
-------
Example code::

    from belfrywidgets import ToolTip

    tk = Tk()
    ent = Entry(tk)
    txt = Text(tk, borderwidth=2, relief="sunken")
    ent.pack(side=TOP, padx=5, pady=5)
    txt.pack(side=TOP, padx=5, pady=5)
    txt.insert(END, "Tagged Text\n", "footag")
    txt.insert(END, "Untagged Text\n")
    ToolTip(ent, "This is an entry widget.")
    ToolTip(txt, "This is a text widget.", tag="footag")
    tk.mainloop()



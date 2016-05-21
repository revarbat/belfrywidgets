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


CollapsiblePane
---------------
Example code::

    from belfrywidgets.collapsiblepane import CollapsiblePane

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

    from belfrywidgets.labelbutton import LabelButton
    tk = Tk()
    b1 = LabelButton(tk, text="Button 1", command=lambda: print("B1!"))
    b2 = LabelButton(tk, text="Button 2", command=lambda: print("B2!"))
    b1.pack(side=TOP, padx=20, pady=20)
    b2.pack(side=TOP, padx=20, pady=20)
    tk.mainloop()


TabbedNoteBook
--------------
Example code::

    from belfrywidgets.tabbednotebook import TabbedNoteBook

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

    tk.mainloop()


Wizard
------
Example code::

    from belfrywidgets.wizard import Wizard

    def _finish():
        print("Finish")

    def _cancel():
        print("Cancel")

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



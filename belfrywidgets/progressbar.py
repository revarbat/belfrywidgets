try:
    from Tkinter import *  # noqa
except:
    from tkinter import *  # noqa

import math


DETERMINATE = "determinate"
INDETERMINATE = "indeterminate"


class ProgressBar(Canvas):
    def __init__(
        self, master,
        value=0.0,
        maximum=100.0,
        length=100,
        thickness=8,
        variable=None,
        orient=HORIZONTAL,
        mode=DETERMINATE,
        foreground='blue',
        bordercolor=None,
        **kwargs
    ):
        if bordercolor is None:
            bordercolor = master.cget('background')
        self.value = value
        self.maximum = maximum
        self.variable = variable
        self.orient = orient
        self.mode = mode
        self.foreground = foreground
        self.bordercolor = bordercolor
        self.phase = -1
        self.timer = None
        self.timer_ms = 10
        if orient == HORIZONTAL:
            kwargs['width'] = length
            kwargs['height'] = thickness
        else:
            kwargs['height'] = length
            kwargs['width'] = thickness
        kwargs.setdefault('borderwidth', 0)
        kwargs.setdefault('highlightthickness', 0)
        kwargs.setdefault('background', '#ccc')
        Canvas.__init__(self, master, **kwargs)
        self.master = master
        self.bar = self.create_rectangle(
            0, 0, kwargs['width'], kwargs['height'],
            fill=foreground,
            outline=foreground
        )
        self.mask = self.create_polygon(
            self._calc_mask_coords(),
            smooth='raw',
            splinesteps=24,
            fill=bordercolor,
            outline=bordercolor
        )
        self.bind('<MouseWheel>', 'break')
        self.bind('<Configure>', self._update)
        if variable is not None:
            if isinstance(variable, IntVar) or isinstance(variable, DoubleVar):
                self.value = self.variable.get()
                variable.trace("w", self._var_update)
        self.after(1000, self._update)

    def config(  # noqa
        self,
        value=None,
        maximum=None,
        length=None,
        thickness=None,
        variable=None,
        orient=None,
        mode=None,
        bordercolor=None,
        foreground=None,
        *args,
        **kwargs
    ):
        if length is not None:
            self.length = length
            key = 'width' if self.orient == HORIZONTAL else 'height'
            kwargs[key] = length
        if thickness is not None:
            self.thickness = thickness
            key = 'height' if self.orient == HORIZONTAL else 'width'
            kwargs[key] = thickness
        if orient is not None:
            self.orient = orient
        if maximum is not None:
            self.maximum = maximum
        if value is not None:
            self.value = value
        if mode is not None:
            self.mode = mode
        if foreground is not None:
            self.foreground = foreground
            self.itemconfig(self.bar, fill=foreground)
            self.itemconfig(self.bar, outline=foreground)
        if bordercolor is not None:
            self.bordercolor = bordercolor
            self.itemconfig(self.mask, fill=bordercolor)
            self.itemconfig(self.mask, outline=bordercolor)
        if variable is not None:
            self.variable = variable
            if isinstance(variable, IntVar) or isinstance(variable, DoubleVar):
                self.value = self.variable.get()
                variable.trace("w", self._var_update)
        if args or kwargs:
            attrs = [
                'value', 'maximum', 'length', 'thickness', 'variable',
                'orient', 'mode', 'bordercolor', 'foreground',
            ]
            if args and args[0] in attrs:
                return getattr(self, args[0])
            return super(ProgressBar, self).config(*args, **kwargs)
        self._update()

    def start(self, ms=20):
        self.timer_ms = ms
        self.phase = 0
        self._timer_update()

    def stop(self):
        self.after_cancel(self.timer)
        self.phase = -1
        self._update()

    def _timer_update(self):
        self.phase = (self.phase + 1) % 100
        self._update()
        self.timer = self.after(self.timer_ms, self._timer_update)

    def _var_update(self, *args):
        if self.variable:
            self.value = self.variable.get()
        self._update()

    def _update(self, e=None):
        width = self.winfo_width()
        height = self.winfo_height()
        self.coords(self.mask, self._calc_mask_coords())
        pcnt = float(self.value) / self.maximum
        if self.mode == DETERMINATE:
            if self.orient == HORIZONTAL:
                self.coords(self.bar, [-1, 0, (pcnt * width) - 1, height])
            else:
                self.coords(self.bar, [0, -1, width, (pcnt * height) - 1])
        else:
            w = width / 5
            pos = width * 0.5 * (
                1 - math.cos(2.0 * math.pi * self.phase/100.0)
            ) - w/2
            if self.phase < 0:
                self.coords(self.bar, [-10, -10, -11, -11])
            elif self.orient == HORIZONTAL:
                self.coords(self.bar, [pos, 0, pos + w, height])
            else:
                self.coords(self.bar, [0, pos, width, pos + w])

    def _calc_mask_coords(self):
        width = self.winfo_width()
        height = self.winfo_height()
        fillet = height/2 if self.orient == HORIZONTAL else width/2
        kappa = 0.552228474
        bezext = fillet * kappa
        coords = [
            fillet-1, -1,
            fillet-1, -1,

            width-fillet, -1,
            width-fillet, -1,
            width-fillet+bezext, -1,

            width, fillet-bezext-1,
            width, fillet-1,
            width, fillet-1,

            width, height-fillet,
            width, height-fillet,
            width, height-fillet+bezext,

            width-fillet+bezext, height,
            width-fillet, height,
            width-fillet, height,

            fillet-1, height,
            fillet-1, height,
            fillet-bezext-1, height,

            -1, height-fillet+bezext,
            -1, height-fillet,
            -1, height-fillet,

            -1, fillet-1,
            -1, fillet-1,
            -1, fillet-bezext-1,

            fillet-bezext-1, -1,
            fillet-1, -1,
            fillet-1, -1,

            fillet, -fillet,
            fillet, -fillet,
            fillet, -fillet,

            -fillet, -fillet,
            -fillet, -fillet,
            -fillet, -fillet,

            -fillet, height+fillet,
            -fillet, height+fillet,
            -fillet, height+fillet,

            width+fillet, height+fillet,
            width+fillet, height+fillet,
            width+fillet, height+fillet,

            width+fillet, -fillet,
            width+fillet, -fillet,
            width+fillet, -fillet,

            fillet-1, -fillet,
            fillet-1, -fillet,
            fillet-1, -fillet,

            fillet-1, -1,
            fillet-1, -1,
        ]
        return coords


if __name__ == "__main__":
    tk = Tk()
    v = DoubleVar()
    v.set(0.0)
    pb = ProgressBar(
        tk, mode=DETERMINATE,
        maximum=200,
        variable=v,
        foreground="red",
        background="cyan"
    )
    pb.pack(fill=BOTH, expand=1, padx=10, pady=10)

    def inc():
        v.set(v.get()+1)
        if v.get() < 200:
            tk.after(50, inc)

    inc()
    tk.mainloop()


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap

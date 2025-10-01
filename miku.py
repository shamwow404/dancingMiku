#!/usr/bin/env python3
import gi, os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

PIDFILE = "/tmp/miku.pid"

class MikuWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Miku")
        self.set_decorated(False)    
        self.set_app_paintable(True) 
        self.set_resizable(False)
        self.set_keep_above(True)     
        self.connect("destroy", self.on_destroy)

        # Enable RGBA transparency
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)

        # Make window draggable
        self.drag = False
        self.connect("button-press-event", self.on_press)
        self.connect("button-release-event", self.on_release)
        self.connect("motion-notify-event", self.on_motion)

        # Load the GIF
        image = Gtk.Image.new_from_file("IMAGE_URL_GO_HERE")
        self.add(image)

        # Save PID can kill later
        with open(PIDFILE, "w") as f:
            f.write(str(os.getpid()))

        self.show_all()

    def do_draw(self, cr):
        cr.set_source_rgba(0, 0, 0, 0)
        cr.set_operator(3)  
        cr.paint()
        cr.set_operator(2) 
        Gtk.Window.do_draw(self, cr)

    def on_press(self, widget, event):
        if event.button == 1:
            self.drag = True
            self.drag_start_x = event.x_root
            self.drag_start_y = event.y_root
            self.start_x, self.start_y = self.get_position()

    def on_release(self, widget, event):
        if event.button == 1:
            self.drag = False

    def on_motion(self, widget, event):
        if self.drag:
            dx = event.x_root - self.drag_start_x
            dy = event.y_root - self.drag_start_y
            self.move(self.start_x + dx, self.start_y + dy)

    def on_destroy(self, *args):
        if os.path.exists(PIDFILE):
            os.remove(PIDFILE)
        Gtk.main_quit()

win = MikuWindow()
Gtk.main()

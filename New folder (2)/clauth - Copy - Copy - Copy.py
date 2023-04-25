import gtk
def image_grab_gtk(window):
    left, top, right, bot = get_rect(window)
    w = right - left
    h = bot - top
    s=gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, w, h)
    s.get_from_drawable(gtk.gdk.get_default_root_window(),gtk.gdk.colormap_get_system(),left, top, 0, 0, w, h )
    return Image.frombuffer("RGB",(w, h),s.get_pixels(),"raw","RGB",s.get_rowstride(), 1)

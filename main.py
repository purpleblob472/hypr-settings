import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from gi.repository import Gdk

import inputFunctions

class input_settings_window(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Input")
   
#import CSS
        styleContext = Gtk.StyleContext
        cssProvider = Gtk.CssProvider.new()
        Gtk.CssProvider.load_from_path (cssProvider, "style.css")
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), cssProvider, 400)
        

        scrolled_window = Gtk.ScrolledWindow.new()
        main_box = Gtk.Box.new(Gtk.Orientation(1), 25)

#"gb", "us", "euro", "fr", "dvorak", "dvorak-uk", "colemak"
#Keyboard Layout
        layout_label = Gtk.Label.new("Keyboard Layout")
        layout_dropdown = Gtk.DropDown.new_from_strings(["uk", "us", "europe", "french", "dvorak", "uk dvorak", "colmak"])
        layout_dropdown.connect('notify::selected-item', inputFunctions.keyboard_layout_changed)
        layout_dropdown.props.name = "layout_dropdown"
        layout_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        layout_box.append(layout_label)
        layout_box.append(layout_dropdown)
        main_box.append(layout_box)

#Repeat Rate
        repeat_rate_label = Gtk.Label.new("Repeat Rate")
        repeat_rate_scale = Gtk.Scale.new_with_range(Gtk.Orientation(0), 0, 100, 5)
        repeat_rate_scale.props.width_request = 500
        repeat_rate_scale.set_value(25)
        repeat_rate_scale.add_mark(25, Gtk.PositionType(3), "25")
        repeat_rate_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        repeat_rate_box.append(repeat_rate_label)
        repeat_rate_box.append(repeat_rate_scale)
        main_box.append(repeat_rate_box)

#Follow Mouse
        follow_mouse_label = Gtk.Label.new("Mouse Follows Cursor")
        follow_mouse_switch = Gtk.Switch.new()
        follow_mouse_switch.set_state(inputFunctions.get_follow_mouse())
        follow_mouse_switch.set_active(inputFunctions.get_follow_mouse())
        follow_mouse_switch.connect('notify::state', inputFunctions.follow_mouse_toggle)
        follow_mouse_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        follow_mouse_box.append(follow_mouse_label)
        follow_mouse_box.append(follow_mouse_switch)
        main_box.append(follow_mouse_box)

#Repeat Delay
        repeat_delay_label = Gtk.Label.new("Repeat Delay")
        repeat_delay_scale = Gtk.Scale.new_with_range(Gtk.Orientation(0), 0, 10000, 100)
        repeat_delay_scale.props.width_request = 500
        repeat_delay_scale.set_value(600)
        repeat_delay_scale.add_mark(600, Gtk.PositionType(3), "600")
        repeat_delay_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        repeat_delay_box.append(repeat_delay_label)
        repeat_delay_box.append(repeat_delay_scale)
        main_box.append(repeat_delay_box)

#Senitivity
        sensitivity_label = Gtk.Label.new("Mouse Sensitivity")
        sensitivity_scale = Gtk.Scale.new_with_range(Gtk.Orientation(0), -1, 1, 0.1)
        sensitivity_scale.props.width_request = 500
        sensitivity_scale.set_value(0)
        sensitivity_scale.add_mark(0, Gtk.PositionType(3), "0")
        sensitivity_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        sensitivity_box.append(sensitivity_label)
        sensitivity_box.append(sensitivity_scale)
        main_box.append(sensitivity_box)

#Mouse Acceleration
        accel_profile_label = Gtk.Label.new("Mouse Acceleration")
        accel_profile_switch = Gtk.Switch.new()
        accel_profile_switch.set_state(inputFunctions.get_mouse_accel())
        accel_profile_switch.set_active(inputFunctions.get_mouse_accel())
        accel_profile_switch.connect('notify::state', inputFunctions.mouse_accel_toggle)
        accel_profile_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        accel_profile_box.append(accel_profile_label)
        accel_profile_box.append(accel_profile_switch)
        main_box.append(accel_profile_box)

#Left Handed Mode
        left_handed_label = Gtk.Label.new("Left Hand Mode")
        left_handed_switch = Gtk.Switch.new()
        left_handed_switch.set_state(inputFunctions.get_left_hand())
        left_handed_switch.set_active(inputFunctions.get_left_hand())
        left_handed_switch.connect('notify::state', inputFunctions.left_hand_toggle)
        left_handed_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        left_handed_box.append(left_handed_label)
        left_handed_box.append(left_handed_switch)
        main_box.append(left_handed_box)

#Cursor Icon
        cursor_icon_label = Gtk.Label.new("Cursor Icon")
        cursor_icon_dropdown = Gtk.DropDown.new_from_strings(["Adwita", "Breeze"])
        cursor_icon_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        cursor_icon_box.append(cursor_icon_label)
        cursor_icon_box.append(cursor_icon_dropdown)
        main_box.append(cursor_icon_box)

#Cursor Size
        cursor_size_label = Gtk.Label.new("Cursor Size")
        cursor_size_scale = Gtk.Scale.new_with_range(Gtk.Orientation(0), 2, 100, 2)
        cursor_size_scale.props.width_request = 500
        cursor_size_scale.set_value(32)
        cursor_size_scale.add_mark(24, Gtk.PositionType(3), "24")
        cursor_size_scale.add_mark(32, Gtk.PositionType(3), "32")
        cursor_size_scale.add_mark(48, Gtk.PositionType(3), "48")
        cursor_size_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        cursor_size_box.append(cursor_size_label)
        cursor_size_box.append(cursor_size_scale)
        main_box.append(cursor_size_box)

#Scroll Factor
        scroll_factor_label = Gtk.Label.new("Scroll Factor")
        scroll_factor_scale = Gtk.Scale.new_with_range(Gtk.Orientation(0), 0, 10, 0.1)
        scroll_factor_scale.props.width_request = 500
        scroll_factor_scale.set_value(1.0)
        scroll_factor_scale.add_mark(0, Gtk.PositionType(3), "0")
        scroll_factor_scale.add_mark(1, Gtk.PositionType(3), "1")
        scroll_factor_scale.add_mark(10, Gtk.PositionType(3), "10")
        scroll_factor_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        scroll_factor_box.append(scroll_factor_label)
        scroll_factor_box.append(scroll_factor_scale)
        main_box.append(scroll_factor_box)

#Natural Scroll
        natural_scroll_label = Gtk.Label.new("Natural Scoll")
        natural_scroll_switch = Gtk.Switch.new()
        natural_scroll_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        natural_scroll_box.append(natural_scroll_label)
        natural_scroll_box.append(natural_scroll_switch)
        main_box.append(natural_scroll_box)

#Focus on Close
        focus_on_close_label = Gtk.Label.new("Focus on Close")
        focus_on_close_switch = Gtk.Switch.new()
        focus_on_close_box = Gtk.Box.new(Gtk.Orientation(0), 300)
        focus_on_close_box.append(focus_on_close_label)
        focus_on_close_box.append(focus_on_close_switch)
        main_box.append(focus_on_close_box)


        scrolled_window.set_child(main_box)
        self.set_child(scrolled_window)


class TestApp(Gtk.Application):
    def __init__(self):
        super().__init__()
        self.window = None
    
    def do_activate(self):
        if self.window is None:
            self.window = input_settings_window(self)
        self.window.present()

app = TestApp()
app.run([])

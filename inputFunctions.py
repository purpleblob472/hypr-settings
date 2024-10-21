import sys
import subprocess

def keyboard_layout_changed(x, y):
    layouts = ["gb", "us", "euro", "fr", "dvorak", "dvorak-uk", "colemak"]
    print(layouts[x.props.selected])
    print(x.props.name)

def repeat_rate_change(x, y):
    print(x.props.value_pos)

def get_follow_mouse():
    print("getting state")
    follow_mouse_state = subprocess.getoutput('grep "follow_mouse" $HOME/.config/hypr/hyprland.conf | tail -c 2')
    print("follow mouse is", follow_mouse_state)
    if (int(follow_mouse_state) == 1): return True
    return False



def follow_mouse_toggle(x, y):
    print("changing to state {}".format(x.props.state))
    if (x.props.state):
        subprocess.run(["sed -i 's/follow_mouse = 0/follow_mouse = 1/' $HOME/.config/hypr/hyprland.conf"], shell=True)
        print("turned on")
    else:
        subprocess.run(["sed -i 's/follow_mouse = 1/follow_mouse = 0/' $HOME/.config/hypr/hyprland.conf"], shell=True)
        print("turned off")
    print("done")

def get_mouse_accel():
    print("getting accel")
    accel_state = subprocess.getoutput('grep "accel_profile" $HOME/.config/hypr/hyprland.conf | tail -c 5')
    if(accel_state == "flat"): return False
    return True

def mouse_accel_toggle(x,y):
    print("toggling mouse accel")
    if(x.props.state):
        subprocess.run(["sed -i 's/accel_profile = flat/accel_profile = adaptive/' $HOME/.config/hypr/hyprland.conf"], shell=True)
        print("turned on")
    else:
        subprocess.run(["sed -i 's/accel_profile = adaptive/accel_profile = flat/' $HOME/.config/hypr/hyprland.conf"], shell=True)
        print("turned off")
    print("done")

def get_left_hand():
    print("getting left_hand")
    left_hand_state = subprocess.getoutput('grep "left_handed" $HOME/.config/hypr/hyprland.conf | tail -c 5')
    if(left_hand_state == "true"): return True
    return False

def left_hand_toggle(x,y):
    print("toggling")
    if(x.props.state):
        subprocess.run(["sed -i 's/left_handed = false/left_handed = true/' $HOME/.config/hypr/hyprland.conf"], shell=True)
        print("turned on")
    else:
        subprocess.run(["sed -i 's/left_handed = true/left_handed = false/' $HOME/.config/hypr/hyprland.conf"], shell=True)
        print("turned off")

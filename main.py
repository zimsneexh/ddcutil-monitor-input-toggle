import os

def main():

    reader = open(os.path.expanduser('~') + "/.config/ddcutil-monitor-switcher/state.txt")
    writer = open(os.path.expanduser('~') + "/.config/ddcutil-monitor-switcher/state.txt")
    state = file.read()
   
    
    if(state == "dp"):
        os.command("sudo ddcutil setvcp 0x60 0x0f")
        writer.write("hdmi")
    else if(state == "hdmi"):
        os.command("sudo ddcutil setvcp 0x60 0x0f")
        writer.write("dp")
    else:
        print("Unknown state. Check file!")

if __name__ == "__main__":
    main()

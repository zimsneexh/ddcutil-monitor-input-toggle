import os

def main():

    reader = open(os.path.expanduser('~') + "/.config/ddcutil-monitor-switcher/state.txt", "r")
    state = reader.read()
  
    print(state)
    
    if("dp" in state):
        writer = open(os.path.expanduser('~') + "/.config/ddcutil-monitor-switcher/state.txt", "w")
        os.system("sudo ddcutil setvcp 0x60 0x05")
        writer.write("hdmi")
    elif("hdmi" in state):
        writer = open(os.path.expanduser('~') + "/.config/ddcutil-monitor-switcher/state.txt", "w")
        os.system("sudo ddcutil setvcp 0x60 0x0f")
        writer.write("dp")
    else:
        print("Unknown state. Check file!")

if __name__ == "__main__":
    main()

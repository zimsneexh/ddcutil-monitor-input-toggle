import subprocess
import os

def main():

    command = "sudo ddcutil getvcp 0x60"
    cmdres = subprocess.getoutput(command)

    if("0x0f" in cmdres):
        os.system("sudo ddcutil setvcp 0x60 0x05")
    elif("0x05" in cmdres):
        os.system("sudo ddcutil setvcp 0x60 0x0f")

if __name__ == "__main__":
    main()

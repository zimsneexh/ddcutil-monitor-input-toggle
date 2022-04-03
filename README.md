# ddcutil-monitor-input-toggle
Toggle your monitors input source with ddcutil from Linux

# Usage:
Kernel module i2c-dev needs to be loaded in order to interface with the monitor.  
To get all available ddc commands, use:  
    ddcutil listvcp
    
Note the feature codes, there should be plenty to choose from.

# Set feature code to a specific value:
To set the state of a feature code:     
    ddcutil setvcp 0x** (Replace stars with feature code)

# Get a feature codes current value:
To get the current state of a feature code:  
    ddcutil getvcp 0x** (Replace stars with feature code)
   
# Find valid values:
I'm not exactly sure if finding all valid values is possible via ddcutil,   
but changing the required feature via the Monitors UI and checking for changes with getvcp   
worked quite well.

# Switching monitor Input:
I wrote a simple python script to switch between monitor inputs   
with ddcutil for use with i3wm. Simply replace feature codes and valid values.

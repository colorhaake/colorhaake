import subprocess
import os
import time

# Environment settings
SDK_PATH = "/Users/minibarque/android/sdk:/Users/minibarque/android/sdk/tools:/Users/minibarque/android/sdk/platform-tools:"
APPIUM_PATH = "/usr/local/bin:"
my_env = os.environ
my_env["PATH"] =  SDK_PATH + APPIUM_PATH + my_env.get("PATH", '')


# Open Terminal
cmd = """osascript -e 'tell application "Terminal"
    activate
    do script "appium"
end tell'"""
print "command: " + cmd

output = subprocess.Popen(cmd, shell=True, env=my_env, stdout=subprocess.PIPE)
output, err = output.communicate()

print "output : " + output

# get window id
# e.g.: tab 1 of window id 4564
key = "window id"
key_loc = output.find(key)
window_id = output[key_loc+len(key)+1:].strip()

print "window id : " + window_id 

time.sleep(5)

# Close Terminal
cmd = """osascript -e 'tell application "Terminal"
    close (every window whose id is """ + window_id + """)
    tell application "System Events" to tell process "Terminal" to keystroke return
    end tell'"""
print "command: " + cmd

output = subprocess.Popen(cmd, shell=True, env=my_env, stdout=subprocess.PIPE)
output, err = output.communicate()

print "output : " + output



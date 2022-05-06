import os, time, pyautogui

start_rec = input(" Welcome to VERSA Anti Cheat\n Are you ready to start recording? (y/n): ")
if "y" in start_rec:
    if not os.path.exists(time.strftime("%Y.%m.%d")):
        os.mkdir(time.strftime("%Y.%m.%d"))

    while True:
        time.sleep(5)
        pyautogui.screenshot().save((time.strftime("%Y.%m.%d")) + "/" + time.strftime("%Y.%m.%d.%H.%M.%S.png"))
        open((time.strftime("%Y.%m.%d")) + "/" + time.strftime("%Y.%m.%d.%H.%M.%S")+".txt", "w")\
            .write(os.popen('wmic process get description').read())
        print(f"\n Screenshot Saved: {time.strftime('%Y.%m.%d.%H.%M.%S')}")
        time.sleep(10)

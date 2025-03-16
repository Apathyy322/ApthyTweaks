import subprocess
import os
import shutil
import winreg
import ctypes
import sys
import time
import requests
from pystyle import Colorate, Colors,Write
ctypes.windll.kernel32.SetConsoleTitleW("ApthyTweaks")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
def logo():
    header = """
            ++-----------------------------------------------------------------------------------------------++
            ||  █████╗ ██████╗ ████████╗██╗  ██╗██╗   ██╗████████╗██╗    ██╗███████╗ █████╗ ██╗  ██╗███████╗ || 
            || ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║╚██╗ ██╔╝╚══██╔══╝██║    ██║██╔════╝██╔══██╗██║ ██╔╝██╔════╝ ||
            || ███████║██████╔╝   ██║   ███████║ ╚████╔╝    ██║   ██║ █╗ ██║█████╗  ███████║█████╔╝ ███████╗ ||
            || ██╔══██║██╔═══╝    ██║   ██╔══██║  ╚██╔╝     ██║   ██║███╗██║██╔══╝  ██╔══██║██╔═██╗ ╚════██║ ||
            || ██║  ██║██║        ██║   ██║  ██║   ██║      ██║   ╚███╔███╔╝███████╗██║  ██║██║  ██╗███████║ ||
            || ╚═╝  ╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝   ╚═╝      ╚═╝    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ||
            ++----------------------------------------Made By Apathy-----------------------------------------++
            ++-----------------------------------------------------------------------------------------------++
            """
    print(Colorate.Horizontal(Colors.blue_to_purple,f'{header}'))
def set_wallpaper_from_url(url: str):
    path = "C:\\Users\\apthy\\Downloads\\apthytweaks.png"
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
        else:
            print(f"Failed to download image. HTTP status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to set wallpaper: {e}")

wallpaper_url = "https://i.ibb.co/fVhd84tq/apthytweaks.png"  
set_wallpaper_from_url(wallpaper_url)
def enable_game_mode():
    subprocess.run('reg add "HKCU\\SOFTWARE\\Microsoft\\GameBar" /v "AutoGameModeEnabled" /t REG_DWORD /d 1 /f', shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def disable_game_mode():
    subprocess.run('reg add "HKCU\\SOFTWARE\\Microsoft\\GameBar" /v "AutoGameModeEnabled" /t REG_DWORD /d 0 /f', shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def clear_temp_files():
    subprocess.run("del /q /f /s %temp%\\*", shell=True)
    subprocess.run("rd /s /q %temp%", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def clear_prefetch():
    subprocess.run("del /q /f /s C:\\Windows\\Prefetch\\*", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def clear_software_distribution():
    subprocess.run("del /q /f /s C:\\Windows\\SoftwareDistribution\\Download\\*", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def stop_and_restart_wuauserv():
    subprocess.run("net stop wuauserv", shell=True)
    subprocess.run("net start wuauserv", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def clear_recycle_bin():
    subprocess.run("rd /s /q %systemdrive%\\$RECYCLE.BIN", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def clear_event_logs():
    subprocess.run("wevtutil cl Application", shell=True)
    subprocess.run("wevtutil cl System", shell=True)
    subprocess.run("wevtutil cl Security", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def disable_hibernation():
    subprocess.run("powercfg -h off", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def disable_notifications():
    subprocess.run('reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_TOASTS_ENABLED" /t REG_DWORD /d 0 /f', shell=True)
    subprocess.run('reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_sGLOBAL_SETTING_TOASTS_DISABLED" /t REG_DWORD /d 1 /f', shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def disable_aero_peek():
    subprocess.run("reg add HKCU\\Software\\Microsoft\\Windows\\DWM /v EnableAeroPeek /t REG_DWORD /d 0 /f", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def optimize_visual_effects():
    visual_effects_flags = 0x1 | 0x40 | 0x100 | 0x200 | 0x800
    subprocess.run(f"reg add \"HKCU\\Control Panel\\Desktop\" /v UserPreferenceMask /t REG_DWORD /d {visual_effects_flags} /f", shell=True)
    subprocess.run("reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects /v VisualFXSetting /t REG_DWORD /d 2 /f", shell=True)
    time.sleep(2)
    logo()
    multi_tool()
def remove_startup_programs():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run") as key:
        i = 0
        startup_programs = []
        while True:
            try:
                program_name, program_path, _ = winreg.EnumValue(key, i)
                startup_programs.append((i+1, program_name, program_path))
                i += 1
            except OSError:
                break

        if startup_programs:
            print("Startup Programs:")
            for i, name, path in startup_programs:
                print(f"{i} - {name}: {path}")
            
            try:
                choice = int(input("Enter the number of the program to remove (0 to cancel): "))
                if choice > 0 and choice <= len(startup_programs):
                    program_to_remove = startup_programs[choice - 1]
                    subprocess.run(f'reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "{program_to_remove[1]}" /f', shell=True)
                    print(f"Removed {program_to_remove[1]} from startup.")
                    time.sleep(1)
                    logo()
                    multi_tool()
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
        else:
            print("No startup programs found.")

def all_optimizations():
    enable_game_mode()
    clear_temp_files()
    clear_prefetch()
    clear_software_distribution()
    stop_and_restart_wuauserv()
    clear_recycle_bin()
    clear_event_logs()
    disable_hibernation()
    disable_notifications()
    disable_aero_peek()
    optimize_visual_effects()
    print("All optimizations completed.")
    time.sleep(2)
    logo()
    multi_tool()

def multi_tool():
    Write.Print("\n     Choose an option:", Colors.purple_to_blue, interval = 0)
    Write.Print("\n     1. Enable Game Mode", Colors.purple_to_blue,interval = 0)
    Write.Print("\n     2. Disable Game Mode", Colors.purple_to_blue,interval = 0)
    Write.Print("\n     3. Clear Temp Files", Colors.purple_to_blue,interval = 0)
    Write.Print("\n     4. Clear Prefetch", Colors.purple_to_blue,interval = 0)
    Write.Print("\n     5. Clear Software Distribution Cache", Colors.purple_to_blue,interval = 0)
    Write.Print("\n     6. Stop and Restart Windows Update Service", Colors.purple_to_blue,interval = 0)
    Write.Print("\n     7. Clear Recycle Bin", Colors.blue_to_purple,interval = 0)
    Write.Print("\n     8. Clear Event Logs", Colors.blue_to_purple,interval = 0)
    Write.Print("\n     9. Disable Hibernation", Colors.blue_to_purple,interval = 0)
    Write.Print("\n     10. Disable Notifications", Colors.blue_to_purple,interval = 0)
    Write.Print("\n     11. Disable Aero Peek", Colors.blue_to_purple,interval = 0)
    Write.Print("\n     12. Optimize Visual Effects", Colors.blue_to_purple,interval = 0)
    Write.Print("\n     13. Remove Startup Programs", Colors.blue_to_purple,interval = 0)
    Write.Print("\n     14. Do All Optimizations", Colors.blue_to_purple,interval = 0)
    print("\n     0.Exit")
    try:
        choice = int(Write.Input("\n     > ", Colors.red, interval=0))
        if choice == 1:
            enable_game_mode()
        elif choice == 2:
            disable_game_mode()
        elif choice == 3:
            clear_temp_files()
        elif choice == 4:
            clear_prefetch()
        elif choice == 5:
            clear_software_distribution()
        elif choice == 6:
            stop_and_restart_wuauserv()
        elif choice == 7:
            clear_recycle_bin()
        elif choice == 8:
            clear_event_logs()
        elif choice == 9:
            disable_hibernation()
        elif choice == 10:
            disable_notifications()
        elif choice == 11:
            disable_aero_peek()
        elif choice == 12:
            optimize_visual_effects()
        elif choice == 13:
            remove_startup_programs()
        elif choice == 14:
            all_optimizations()
        elif choice == 0:
            print("Exiting...")
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Invalid input, please enter a number between 0 and 14.")
logo()
multi_tool()

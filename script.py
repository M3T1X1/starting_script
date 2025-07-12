import shutil
import subprocess

def flatpak_based_apps(app_id, app_name=None):
    app_name = app_name or app_id
    result = subprocess.run(["flatpak", "info", app_id], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if result.returncode != 0:
        print(f"{app_name} not found. Installing...")
        subprocess.run(["flatpak", "install", "-y", app_id])
    else:
        print(f"{app_name} installed.")

def dnf_based_apps(app_run, app_dnf_install):
    app_name = app_run or app_dnf_install
    if shutil.which(f"{app_run}") is None:
       print(f"Installing {app_name}...")
       subprocess.run(["sudo", "dnf", "install", app_dnf_install])
    else:
        print(f"{app_name} is already installed.")

if __name__ == "__main__":
    dnf_apps =[
        ("steam", "steam"),
        ("brave-browser", "brave-browser"),
    ]

    flatpak_apps = [
        ("com.spotify.Client", "Spotify"),
        ("com.discordapp.Discord", "Discord"),
        ("com.visualstudio.code", "VS Code")
    ]

    for app_run, app_dnf_install in dnf_apps:
        print(f"Checking: {app_run}")
        dnf_based_apps(app_run, app_dnf_install)

    for app_id, app_name in flatpak_apps:
        print(f"Checking: {app_id}")
        flatpak_based_apps(app_id, app_name)
import requests
import json
from datetime import datetime

REPO_OWNER = "mamaclapper"
REPO_NAME = "StremioX"
IPA_PATTERNS = [
    "StremioX-iOS-",
    "StremioX-iOS"
]

def get_latest_release():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest"
    response = requests.get(url)
    return response.json()

def find_ios_ipa(release):
    for asset in release.get("assets", []):
        name = asset["name"]
        if any(pattern in name for pattern in IPA_PATTERNS) and name.endswith(".ipa"):
            return asset["browser_download_url"]
    return None

def generate_apps_json(download_url, release):
    version = release["tag_name"].replace("v", "")
    date = release["published_at"]
    
    return {
        "name": "StremioX",
        "sourceURL": "https://raw.githubusercontent.com//DominoLeChat/stremiox-altstore/apps.json",
        "apps": [{
            "name": "StremioX",
            "bundleIdentifier": "com.stremio.x",
            "developerName": "mamaclapper",
            "version": version,
            "versionDate": date[:10],
            "downloadURL": download_url,
            "localizedDescription": "Stremio sur iOS"
        }]
    }

if __name__ == "__main__":
    release = get_latest_release()
    download_url = find_ios_ipa(release)
    
    if not download_url:
        print("No iOS IPA found")
        exit(1)
    
    apps_json = generate_apps_json(download_url, release)
    
    with open("apps.json", "w") as f:
        json.dump(apps_json, f, indent=2)
    
    print(f"Updated to {release['tag_name']}")

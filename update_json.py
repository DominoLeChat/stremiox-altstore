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
    if response.status_code != 200:
        print(f"Error fetching release: {response.status_code}")
        print(response.text)
        exit(1)
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
        "subtitle": "Stremio on iOS",
        "description": "Altstore source for StremioX on iOS",
        "iconURL": "https://raw.githubusercontent.com/mamaclapper/StremioX/refs/heads/main/app/Resources/Assets.xcassets/AppIcon.appiconset/ios_1024.png",
        "headerURL": https://raw.githubusercontent.com/mamaclapper/StremioX/refs/heads/main/app/ResourcesTV/Assets.xcassets/App%20Icon%20%26%20Top%20Shelf%20Image.brandassets/Top%20Shelf%20Image%20Wide.imageset/tv_topshelf_wide.png,
        "website": "https://github.com/mamaclapper/StremioX",
        "apps": [{
            "name": "StremioX",
            "bundleIdentifier": "com.stremiox.app.native",
            "developerName": "mamaclapper",
            "iconURL": "https://raw.githubusercontent.com/mamaclapper/StremioX/refs/heads/main/app/Resources/Assets.xcassets/AppIcon.appiconset/ios_1024.png",
            "version": version,
            "versionDate": date[:10],
            "downloadURL": download_url,
            "localizedDescription": "Stremio on iOS"
        }],
        "news": []
    }

if __name__ == "__main__":
    print("Fetching latest StremioX release...")
    release = get_latest_release()
    print(f"Found release: {release['tag_name']}")

    download_url = find_ios_ipa(release)

    if not download_url:
        print("No iOS IPA found in assets!")
        print("Assets:", [a["name"] for a in release.get("assets", [])])
        exit(1)

    print(f"Found iOS IPA: {download_url}")
    apps_json = generate_apps_json(download_url, release)

    with open("apps.json", "w") as f:
        json.dump(apps_json, f, indent=2)

    print(f"Written apps.json with version {release['tag_name']}")
    print(f"Download URL: {download_url}")

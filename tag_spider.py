import re
import requests


def get_chromium_version():
    version_list = []
    major_version_list = []
    url = "https://chromium-downloads.herokuapp.com/builds"
    res = requests.get(url)
    if res.text:
        for i in res.json():
            channel = i['channel']
            if channel == "stable":
                version = i['version']
                version_list.append(version)
    else:
        print("Get Version Failed!")
    if version_list:
        with open("chrome_version.txt", "w", encoding="utf-8") as fw:
            fw.write("\n".join(version_list))


def get_edge_version():
    url = "https://packages.microsoft.com/yumrepos/edge/"
    res = requests.get(url)
    text = res.text
    version = re.findall(r"microsoft-edge-beta-(\S+)-1.x86_64.rpm\">", text)
    with open("edge_version.txt", "w", encoding="utf-8") as fw:
        fw.write("\n".join(version))


if __name__ == '__main__':
    get_edge_version()

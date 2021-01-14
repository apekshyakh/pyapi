#!/usr/bin/python3

import requests


def main():
    
    cameraOptions = ["FHAZ","RHAZ","MAST", "CHEMCAM","NAVCAM"]
    ans = ""
    while ans not in cameraOptions:
        ans = input(">").strip().upper()

    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()

    for img in roverresp["photos"]:
        print(f"ROVER: {img['rover']['name']}")
        print(f"DATE: {img['earth_date']}")
        print(f"{img['img_src']}")

if __name__ == "__main__":
    main()

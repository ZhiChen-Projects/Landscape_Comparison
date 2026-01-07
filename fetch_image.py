import requests
import numpy as np
import cv2

def fetch_gibs_image(date, bbox, label):
    url = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
    params = {
        "SERVICE": "WMS",
        "VERSION": "1.3.0",
        "REQUEST": "GetMap",
        "LAYERS": "MODIS_Terra_CorrectedReflectance_TrueColor",
        "TIME": date,
        "CRS": "EPSG:4326",
        "BBOX": bbox,
        "WIDTH": "800",
        "HEIGHT": "800",
        "FORMAT": "image/jpeg",
        "STYLES": ""
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if "image/jpeg" not in response.headers.get("Content-Type", ""):
            print(f"Data gap for {label} on {date}")
            return None
        img_array = np.frombuffer(response.content, np.uint8)
        return cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    except Exception as ex:
        print(f"Connection error for {label}: {ex}")
        return None


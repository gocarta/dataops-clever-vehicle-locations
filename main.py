# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "datablob",
#     "requests",
#     "simple-env",
#     "tzdata",
# ]
# ///
import datablob
from datetime import datetime
import math
import requests
import simple_env as se
from time import sleep
import zoneinfo

AWS_BUCKET_NAME = se.get("AWS_BUCKET_NAME")
AWS_BUCKET_PATH = se.get("AWS_BUCKET_PATH")
CLEVER_BUS_TIME_API_KEY = se.get("CLEVER_BUS_TIME_API_KEY")
CLEVER_TIMEZONE = se.get("CLEVER_TIMEZONE")
tzinfo = zoneinfo.ZoneInfo(CLEVER_TIMEZONE)

url = "https://bustracker.gocarta.org/bustime/api/v3/getroutes"
params = {"format": "json", "key": CLEVER_BUS_TIME_API_KEY}
response = requests.get(url, params=params)
data = response.json()
rts = [route["rt"] for route in data["bustime-response"]["routes"]]
print("[dataops-clever-vehicle-locations] got routes:", rts)

results = []
page_size = 10
for i in range(math.ceil(len(rts) / page_size)):
    url = "https://bustracker.gocarta.org/bustime/api/v3/getvehicles"
    params = {
        "format": "json",
        "key": CLEVER_BUS_TIME_API_KEY,
        "rt": ",".join(rts[i * page_size : (i + 1) * page_size]),
    }
    response = requests.get(url, params=params)
    data = response.json()
    bustime_response = data["bustime-response"]

    # sometime vehicle is not in bustime_response if a bus is no longer running
    if "vehicle" in bustime_response:
        for bus in bustime_response["vehicle"]:
            # 20260107 21:48
            tmstmp = bus["tmstmp"]

            dt = datetime.strptime(tmstmp, "%Y%m%d %H:%M")
            dt = dt.replace(tzinfo=tzinfo)
            timestamp = dt.isoformat()

            results.append(
                {
                    "vehicle_id": bus["vid"],
                    "route": bus["rt"],
                    # "delayed": bus["dly"],
                    "destination": bus["des"],
                    # "heading": bus["hdg"],
                    "latitude": float(bus["lat"]),
                    "longitude": float(bus["lon"]),
                    # "mode": bus["mode"],
                    # "path_id": bus["pid"],
                    # "speed": float(bus["spd"])
                    "timestamp": timestamp,
                }
            )

# client for data store
client = datablob.DataBlobClient(
    bucket_name=AWS_BUCKET_NAME, bucket_path=AWS_BUCKET_PATH
)

client.update_dataset(name="clever_vehicle_locations", version="1", data=results, latitude_key="latitude", longitude_key="longitude")
print(f"[dataops-clever-vehicle-locations] updated {len(results)} rows")

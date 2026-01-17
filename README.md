# dataops-clever-vehicle-locations
> Near Real-Time Location of all [CARTA](https://www.gocarta.org/) Buses and Shuttles

## background
Data access is important to us at CARTA and we built this pipeline to make it easier to access data about the locations of our buses and shuttles.  This data pipeline basically pulls the vehicle location data from the Clever Devices BusTime API hosted by CARTA and then converts it into user-friendly formats, CSV and JSON.  We'll continue to add more formats, but let us know if you have one you'd like to see.

## frequency
The pipeline runs every minute.

## columns
| column | example | description |
| :--- | :--- | :--- |
| **vehicle_id** | `131` | The unique internal identifier for the specific physical bus. |
| **timestamp** | `2026-01-07T22:51:00-05:00` | The standardized ISO 8601 date and time the location was reported. |
| **route** | `1` | The designated route number or shorthand name for the service. |
| **destination** | `ALTON PARK` | The final destination or headsign of the vehicle's current trip. |
| **latitude** | `35.01519088745117` | The current North-South geographic coordinate of the vehicle. |
| **longitude** | `-85.32403106689453` | The current East-West geographic coordinate of the vehicle. |

## download links
- [metadata](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_vehicle_locations/v1/meta.json)
- [csv](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_vehicle_locations/v1/data.csv)
- [geojson (points)](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_vehicle_locations/v1/data.points.geojson)
- [json](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_vehicle_locations/v1/data.json)

## preview links
You can view the dataset on geojson.io [here](https://geojson.io/#data=data:text/x-url,https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_vehicle_locations/v1/data.points.geojson).

## support
Post an issue [here](https://github.com/gocarta/dataops-clever-vehicle-locations/issues) or email the package author at DanielDufour@gocarta.org.

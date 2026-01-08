# dataops-vehicles-current
> Near Real-Time Location of all [CARTA](https://www.gocarta.org/) Buses and Shuttles

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
- [json](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_vehicle_locations/v1/data.json)

## support
Post an issue [here](https://github.com/gocarta/dataops-clever-vehicle-locations/issues) or email the package author at DanielDufour@gocarta.org.

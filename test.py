import json
import sys
print(sys.path)

a={
    "temperature": 25,
    "humidity": 60,
    "conductivity": 1.0,
    "ph": 6.5,
    "nitrogen": 20,
    "phosphorus": 15,
    "potassium": 25
}
print(json.dumps(a))

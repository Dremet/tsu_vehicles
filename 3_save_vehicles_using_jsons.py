import json
import codecs
import sqlite3
from pathlib import Path
from src.db import save_vehicle

VEHICLE_PATH = Path("vehicles")


con = sqlite3.connect("vehicles.db")
cur = con.cursor()

for path_in_vehicle_path in VEHICLE_PATH.iterdir():
    if (
        not path_in_vehicle_path.is_file()
        or not path_in_vehicle_path.suffix == ".json"
        or path_in_vehicle_path.name.startswith("_CONF")
    ):
        continue

    with codecs.open(path_in_vehicle_path, "r", "utf-8-sig") as vehicle_file:
        data = json.load(vehicle_file)

    save_vehicle(cur, data)

    con.commit()
con.close()

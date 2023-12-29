import sqlite3
from src.workshop import (
    get_all_vehicle_ids_from_workshop,
    get_workshop_data_by_id,
)
from src.db import save_maker_if_not_exists

con = sqlite3.connect("vehicles.db")
cur = con.cursor()

new_ids = get_all_vehicle_ids_from_workshop()

with open("sql/upsert_workshop_items.sql", "r") as upsert_sql:
    sql_template = upsert_sql.read().replace("\n", "")

    for id in new_ids:
        print(id)
        (
            preview_image_url,
            maker_name,
            maker_id,
            current_subs,
        ) = get_workshop_data_by_id(id)

        save_maker_if_not_exists(cur, maker_id, maker_name)

        cur.execute(
            sql_template,
            {
                "wi_id": id,
                "m_m_id": maker_id,
                "wi_url_image": preview_image_url,
                "wi_subscribers": current_subs,
            },
        )

    con.commit()
con.close()

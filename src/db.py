def save_maker_if_not_exists(cur, maker_id, maker_name):
    with open("sql/upsert_makers.sql", "r") as upsert_sql:
        sql_template = upsert_sql.read().replace("\n", "")

        cur.execute(
            sql_template,
            {"m_id": maker_id, "m_name": maker_name},
        )


def save_vehicle(cur, data):
    vehicle_dict = {
        "wi_wi_id": data["properties"]["guid"]["b"],
        "v_a_id": data["properties"]["guid"]["a"],
        "v_creationTime": data["properties"]["creationTime"],
        "v_name": data["properties"]["name"],
        "v_description": data["properties"]["description"],
        "v_tags_style": data["properties"]["tags"]["style"],
        "v_tags_speed": data["properties"]["tags"]["speed"],
        "v_tags_acceleration": data["properties"]["tags"]["acceleration"],
        "v_tags_turning": data["properties"]["tags"]["turning"],
        "v_tags_sliding": data["properties"]["tags"]["sliding"],
        "v_model": data["properties"]["model"],
        "v_collisionShape": data["properties"]["collisionShape"],
        "v_damage_maxHitPoints": data["properties"]["damage"]["maxHitPoints"],
        "v_weight_mass": data["carPhysics"]["weight"]["mass"],
        "v_weight_massY": data["carPhysics"]["weight"]["massY"],
        "v_weight_massZ": data["carPhysics"]["weight"]["massZ"],
        "v_weight_gravity": data["carPhysics"]["weight"]["gravity"],
        "v_contact_bounciness": data["carPhysics"]["contact"]["bounciness"],
        "v_contact_staticFriction": data["carPhysics"]["contact"]["staticFriction"],
        "v_contact_dynamicFriction": data["carPhysics"]["contact"]["dynamicFriction"],
        "v_contact_bounceCombine": data["carPhysics"]["contact"]["bounceCombine"],
        "v_contact_frictionCombine": data["carPhysics"]["contact"]["frictionCombine"],
        "v_speed_maxSpeed": data["carPhysics"]["speed"]["maxSpeed"],
        "v_speed_viscosity": data["carPhysics"]["speed"]["viscosity"],
        "v_speed_acceleration": data["carPhysics"]["speed"]["acceleration"],
        "v_speed_reverseMultiplier": data["carPhysics"]["speed"]["reverseMultiplier"],
        "v_speed_flyingViscosity": data["carPhysics"]["speed"]["flyingViscosity"],
        "v_braking_braking": data["carPhysics"]["braking"]["braking"],
        "v_braking_parkBraking": data["carPhysics"]["braking"]["parkBraking"],
        "v_braking_parkSpeed": data["carPhysics"]["braking"]["parkSpeed"],
        "v_braking_complexLocking": data["carPhysics"]["braking"]["complexLocking"],
        "v_steering_grip": data["carPhysics"]["steering"]["grip"],
        "v_steering_maxSteering": data["carPhysics"]["steering"]["maxSteering"],
        "v_steering_changeSpeed": data["carPhysics"]["steering"]["changeSpeed"],
        "v_steering_changeReturnSpeed": data["carPhysics"]["steering"][
            "changeReturnSpeed"
        ],
        "v_steering_neutralReturn": data["carPhysics"]["steering"]["neutralReturn"],
        "v_steering_flyingSteering": data["carPhysics"]["steering"]["flyingSteering"],
        "v_steering_flyingChangeMult": data["carPhysics"]["steering"][
            "flyingChangeMult"
        ],
        "v_steering_fullSteeringSpeed": data["carPhysics"]["steering"][
            "fullSteeringSpeed"
        ],
        "v_steering_reverseSteering": data["carPhysics"]["steering"]["reverseSteering"],
        "v_oversteering_always": data["carPhysics"]["oversteering"]["always"],
        "v_oversteering_sliding": data["carPhysics"]["oversteering"]["sliding"],
        "v_oversteering_braking": data["carPhysics"]["oversteering"]["braking"],
        "v_oversteering_accelerating": data["carPhysics"]["oversteering"][
            "accelerating"
        ],
        "v_sliding_slidingAngle": data["carPhysics"]["sliding"]["slidingAngle"],
        "v_sliding_gradualRange": data["carPhysics"]["sliding"]["gradualRange"],
        "v_sliding_gradualGrip": data["carPhysics"]["sliding"]["gradualGrip"],
        "v_sliding_slideBraking": data["carPhysics"]["sliding"]["slideBraking"],
        "v_sliding_slideAcceleration": data["carPhysics"]["sliding"][
            "slideAcceleration"
        ],
        "v_spring_maxLength": data["carPhysics"]["spring"]["maxLength"],
        "v_spring_maxAcceleration": data["carPhysics"]["spring"]["maxAcceleration"],
        "v_spring_damping": data["carPhysics"]["spring"]["damping"],
        "v_spring_backLength": data["carPhysics"]["spring"]["backLength"],
        "v_spring_backAcceleration": data["carPhysics"]["spring"]["backAcceleration"],
        "v_spring_backDamping": data["carPhysics"]["spring"]["backDamping"],
        "v_downforce_downforce": data["carPhysics"]["downforce"]["downforce"],
        "v_downforce_springAffectsGrip": data["carPhysics"]["downforce"][
            "springAffectsGrip"
        ],
        "v_downforce_springAffectsBraking": data["carPhysics"]["downforce"][
            "springAffectsBraking"
        ],
        "v_downforce_maxSpringGs": data["carPhysics"]["downforce"]["maxSpringGs"],
        "v_downforce_maxAccSpringGs": data["carPhysics"]["downforce"]["maxAccSpringGs"],
        "v_weightTransfer_turning": data["carPhysics"]["weightTransfer"]["turning"],
        "v_weightTransfer_braking": data["carPhysics"]["weightTransfer"]["braking"],
        "v_weightTransfer_accelerating": data["carPhysics"]["weightTransfer"][
            "accelerating"
        ],
        "v_weightTransfer_viscosityReduction": data["carPhysics"]["weightTransfer"][
            "viscosityReduction"
        ],
    }

    with open("sql/upsert_vehicles.sql", "r") as upsert_sql:
        sql_template = upsert_sql.read().replace("\n", "")

        cur.execute(
            sql_template,
            vehicle_dict,
        )

CREATE TABLE IF NOT EXISTS makers (
    m_id TEXT UNIQUE,
    m_name TEXT
);

CREATE TABLE IF NOT EXISTS workshop_items (
    wi_id UNSIGNED BIG INT UNIQUE,
    m_m_id TEXT,
    wi_url_image TEXT,
    wi_subscribers INTEGER
);

CREATE TABLE IF NOT EXISTS vehicles (
    v_id INTEGER PRIMARY KEY,
    wi_wi_id UNSIGNED BIG INT, -- called "b" in json files
    v_a_id UNSIGNED BIG INT,
    v_creationTime UNSIGNED BIG INT,
    v_name TEXT,
    v_description TEXT,
    v_tags_style INTEGER,
    v_tags_speed INTEGER,
    v_tags_acceleration INTEGER,
    v_tags_turning INTEGER,
    v_tags_sliding INTEGER,
    v_model INTEGER,
    v_collisionShape INTEGER,
    v_damage_maxHitPoints INTEGER,
    v_weight_mass REAL,
    v_weight_massY REAL,
    v_weight_massZ REAL,
    v_weight_gravity REAL,
    v_contact_bounciness REAL,
    v_contact_staticFriction REAL,
    v_contact_dynamicFriction REAL,
    v_contact_bounceCombine INTEGER, -- Dropdown
    v_contact_frictionCombine INTEGER, -- Dropdown
    v_speed_maxSpeed REAL,
    v_speed_viscosity REAL,
    v_speed_acceleration REAL,
    v_speed_reverseMultiplier REAL,
    v_speed_flyingViscosity REAL,
    v_braking_braking REAL,
    v_braking_parkBraking REAL,
    v_braking_parkSpeed REAL,
    v_braking_complexLocking INTEGER, -- Boolean
    v_steering_grip REAL,
    v_steering_maxSteering REAL,
    v_steering_changeSpeed REAL,
    v_steering_changeReturnSpeed REAL,
    v_steering_neutralReturn REAL,
    v_steering_flyingSteering REAL,
    v_steering_flyingChangeMult REAL,
    v_steering_fullSteeringSpeed REAL,
    v_steering_reverseSteering INTEGER, -- Dropdown
    v_oversteering_always REAL,
    v_oversteering_sliding REAL,
    v_oversteering_braking REAL,
    v_oversteering_accelerating REAL,
    v_sliding_slidingAngle REAL,
    v_sliding_gradualRange REAL,
    v_sliding_gradualGrip INTEGER, -- Boolean
    v_sliding_slideBraking REAL,
    v_sliding_slideAcceleration REAL,
    v_spring_maxLength REAL,
    v_spring_maxAcceleration REAL,
    v_spring_damping REAL,
    v_spring_backLength REAL,
    v_spring_backAcceleration REAL,
    v_spring_backDamping REAL,
    v_downforce_downforce REAL,
    v_downforce_springAffectsGrip INTEGER, -- Boolean
    v_downforce_springAffectsBraking INTEGER, -- Boolean
    v_downforce_maxSpringGs REAL,
    v_downforce_maxAccSpringGs REAL,
    v_weightTransfer_turning REAL,
    v_weightTransfer_braking REAL,
    v_weightTransfer_accelerating REAL,
    v_weightTransfer_viscosityReduction REAL,
    UNIQUE (wi_wi_id, v_creationTime)
);

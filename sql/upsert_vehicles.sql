INSERT INTO vehicles(
    wi_wi_id,
    v_a_id,
    v_creationTime,
    v_name,
    v_description,
    v_tags_style,
    v_tags_speed,
    v_tags_acceleration,
    v_tags_turning,
    v_tags_sliding,
    v_model,
    v_collisionShape,
    v_damage_maxHitPoints,
    v_weight_mass,
    v_weight_massY,
    v_weight_massZ,
    v_weight_gravity,
    v_contact_bounciness,
    v_contact_staticFriction,
    v_contact_dynamicFriction,
    v_contact_bounceCombine,
    v_contact_frictionCombine,
    v_speed_maxSpeed,
    v_speed_viscosity,
    v_speed_acceleration,
    v_speed_reverseMultiplier,
    v_speed_flyingViscosity,
    v_braking_braking,
    v_braking_parkBraking,
    v_braking_parkSpeed,
    v_braking_complexLocking,
    v_steering_grip,
    v_steering_maxSteering,
    v_steering_changeSpeed,
    v_steering_changeReturnSpeed,
    v_steering_neutralReturn,
    v_steering_flyingSteering,
    v_steering_flyingChangeMult,
    v_steering_fullSteeringSpeed,
    v_steering_reverseSteering,
    v_oversteering_always,
    v_oversteering_sliding,
    v_oversteering_braking,
    v_oversteering_accelerating,
    v_sliding_slidingAngle,
    v_sliding_gradualRange,
    v_sliding_gradualGrip,
    v_sliding_slideBraking,
    v_sliding_slideAcceleration,
    v_spring_maxLength,
    v_spring_maxAcceleration,
    v_spring_damping,
    v_spring_backLength,
    v_spring_backAcceleration,
    v_spring_backDamping,
    v_downforce_downforce,
    v_downforce_springAffectsGrip,
    v_downforce_springAffectsBraking,
    v_downforce_maxSpringGs,
    v_downforce_maxAccSpringGs,
    v_weightTransfer_turning,
    v_weightTransfer_braking,
    v_weightTransfer_accelerating,
    v_weightTransfer_viscosityReduction
) 
VALUES(
    :wi_wi_id,
    :v_a_id,
    :v_creationTime,
    :v_name,
    :v_description,
    :v_tags_style,
    :v_tags_speed,
    :v_tags_acceleration,
    :v_tags_turning,
    :v_tags_sliding,
    :v_model,
    :v_collisionShape,
    :v_damage_maxHitPoints,
    :v_weight_mass,
    :v_weight_massY,
    :v_weight_massZ,
    :v_weight_gravity,
    :v_contact_bounciness,
    :v_contact_staticFriction,
    :v_contact_dynamicFriction,
    :v_contact_bounceCombine,
    :v_contact_frictionCombine,
    :v_speed_maxSpeed,
    :v_speed_viscosity,
    :v_speed_acceleration,
    :v_speed_reverseMultiplier,
    :v_speed_flyingViscosity,
    :v_braking_braking,
    :v_braking_parkBraking,
    :v_braking_parkSpeed,
    :v_braking_complexLocking,
    :v_steering_grip,
    :v_steering_maxSteering,
    :v_steering_changeSpeed,
    :v_steering_changeReturnSpeed,
    :v_steering_neutralReturn,
    :v_steering_flyingSteering,
    :v_steering_flyingChangeMult,
    :v_steering_fullSteeringSpeed,
    :v_steering_reverseSteering,
    :v_oversteering_always,
    :v_oversteering_sliding,
    :v_oversteering_braking,
    :v_oversteering_accelerating,
    :v_sliding_slidingAngle,
    :v_sliding_gradualRange,
    :v_sliding_gradualGrip,
    :v_sliding_slideBraking,
    :v_sliding_slideAcceleration,
    :v_spring_maxLength,
    :v_spring_maxAcceleration,
    :v_spring_damping,
    :v_spring_backLength,
    :v_spring_backAcceleration,
    :v_spring_backDamping,
    :v_downforce_downforce,
    :v_downforce_springAffectsGrip,
    :v_downforce_springAffectsBraking,
    :v_downforce_maxSpringGs,
    :v_downforce_maxAccSpringGs,
    :v_weightTransfer_turning,
    :v_weightTransfer_braking,
    :v_weightTransfer_accelerating,
    :v_weightTransfer_viscosityReduction
) 
    ON CONFLICT(wi_wi_id, v_creationTime) DO NOTHING;
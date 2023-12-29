INSERT INTO workshop_items(wi_id, m_m_id, wi_url_image, wi_subscribers) VALUES(:wi_id,:m_m_id,:wi_url_image,:wi_subscribers) 
    ON CONFLICT(wi_id) DO UPDATE 
    SET 
        m_m_id=excluded.m_m_id,
        wi_url_image=excluded.wi_url_image,
        wi_subscribers=excluded.wi_subscribers;
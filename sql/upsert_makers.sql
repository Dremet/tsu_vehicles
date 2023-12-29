INSERT INTO makers(m_id, m_name) VALUES(:m_id,:m_name) 
    ON CONFLICT(m_id) DO UPDATE 
    SET 
        m_name=excluded.m_name;
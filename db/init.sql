CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO users (name, email)
VALUES
    ('Ivan Petrov', 'ivan@example.com'),
    ('Anna Smirnova', 'anna@example.com'),
    ('Petr Sidorov', 'petr@example.com')
ON CONFLICT (email) DO NOTHING;
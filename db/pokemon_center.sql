DROP TABLE IF EXISTS pokemons;
DROP TABLE IF EXISTS trainers;
DROP TABLE IF EXISTS nurses;

CREATE TABLE nurses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);

-- CREATE TABLE trainers (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     address VARCHAR(255),
--     pokenav INT
-- );

CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    trainer VARCHAR(255),
    -- trainer_id INT REFERENCES trainers(id) ON DELETE CASCADE, --> come back to this
    nurse_id INT REFERENCES nurses(id) ON DELETE CASCADE, --> come back to this, it might not be implemented correctly
    species VARCHAR(255),
    hatched VARCHAR(255), --> potentially change for extensions
    notes VARCHAR(255)

);
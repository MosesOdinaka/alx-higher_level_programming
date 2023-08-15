-- Create table second_table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows into table second_table
INSERT INTO second_table (id, name, score)
VALUES
    (1, 'Roy', 18),
    (2, 'Albert', 32),
    (3, 'Coby', 24),
    (4, 'Mathew',38);

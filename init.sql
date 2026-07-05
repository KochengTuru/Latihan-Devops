CREATE TABLE IF NOT EXISTS mahastudent (
    id SERIAL PRIMARY KEY,
    nama VARCHAR(100),
    jurusan VARCHAR(100)
);

INSERT INTO mahastudent(nama, jurusan)
VALUES
('Salgita', 'Teknologi Informasi');
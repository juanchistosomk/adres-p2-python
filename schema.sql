CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_archivo TEXT NOT NULL,
    numero_paginas INTEGER NOT NULL,
    CUFE TEXT NOT NULL,
    peso_archivo REAL NOT NULL
);
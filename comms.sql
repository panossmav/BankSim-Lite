CREATE table IF NOT EXISTS clients(
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dob TEXT NOT NULL,
    phoneno TEXT NOT NULL,
    email TEXT,
    homeaddr TEXT NOT NULL,
    vat TEXT NOT NULL,
    citizenof TEXT NOT NULL,
    idnum TEXT NOT NULL
);

CREATE table IF NOT EXISTS accounts(
    ban INTEGER PRIMARY KEY,
    owner_id INTEGER NOT NULL,
    balance FLOAT
);


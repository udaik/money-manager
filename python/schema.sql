CREATE TABLE MM_Account (
  _id TEXT NOT NULL UNIQUE,
  name CHAR(32) NOT NULL,
  type CHAR(32) NOT NULL,
  balance REAL,
  ifsc_code CHAR(64),
  account_number CHAR(32),
  interest_rate REAL,
  mab REAL,
  date DATE,
  _meta_used INTEGER,
  PRIMARY KEY(_id)
);

CREATE TABLE MUTUAL_FUND (
  _id TEXT NOT NULL UNIQUE,
  name CHAR(32),
  type CHAR(64) NOT NULL,
  balance REAL,
  folionumber CHAR(32),
  PRIMARY KEY(_id)
);

CREATE TABLE EXPENSE_ACCOUNT (
  _id TEXT NOT NULL UNIQUE,
  name CHAR(32) NOT NULL,
  type CHAR(64) NOT NULL,
  parent TEXT NULL,
  date DATE,
  PRIMARY KEY(_id),
  FOREIGN KEY (parent) REFERENCES EXPENSE_ACCOUNT(_id)
);

CREATE TABLE INCOME_ACCOUNT (
  _id TEXT NOT NULL UNIQUE,
  name CHAR(32) NOT NULL,
  type CHAR(64) NOT NULL,
  PRIMARY KEY(_id)
);

CREATE TABLE TRANSACTIONS (
  _id TEXT NOT NULL UNIQUE,
  debitAccount TEXT NOT NULL,
  creditAccount TEXT NOT NULL,
  category TEXT NOT NULL,
  PRIMARY KEY(_id)
  FOREIGN KEY (category) REFERENCES EXPENSE_ACCOUNT(_id)
);

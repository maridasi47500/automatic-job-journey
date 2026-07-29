CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists branche(
        id integer primary key autoincrement,
        name text
                    );
INSERT OR IGNORE INTO branche (name)
VALUES( 'esn');
create table if not exists domaine(
        id integer primary key autoincrement,
        name text
                    );
INSERT OR IGNORE INTO domaine (name)
VALUES( 'la cybersécurité');
INSERT OR IGNORE INTO domaine (name)
VALUES( 'les réseaux');
INSERT OR IGNORE INTO domaine (name)
VALUES( 'le développement');
create table if not exists secteurdapplication(
        id integer primary key autoincrement,
        name text
                    );
INSERT OR IGNORE INTO secteurdapplication (name)
VALUES( 'immobilier');
INSERT OR IGNORE INTO secteurdapplication (name)
VALUES( 'commercial');
INSERT OR IGNORE INTO secteurdapplication (name)
VALUES( 'vente');
create table if not exists job(
        id integer primary key autoincrement,
        name text
                    );
INSERT OR IGNORE INTO job (name)
VALUES( 'développeur(se) web');
INSERT OR IGNORE INTO job (name)
VALUES( 'technicien(ne) support informatique');
create table if not exists country(
        id integer primary key autoincrement,
        name text
                    );
INSERT OR IGNORE INTO country (name)
VALUES( 'spain');
INSERT OR IGNORE INTO country (name)
VALUES( 'italy');
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            email text,
            phone text,
            country_id text,
            job_id text,
            secteurdapplication_id text,
            domaine_id text,
            branche_id text
                    );


CREATE OR REPLACE VIEW current_games AS
select id, league_id from intramuralsApp_game as G where datediff(now(), date_add(G.StartTime, interval 2 week)) < 0;

CREATE OR REPLACE VIEW current_leagues AS
select L.id from intramuralsApp_league as L inner join current_games as CG on CG.league_id = L.id;  


/* Persons */
INSERT INTO `intramuralsApp_person` VALUES
(1, 123456, 'Bogus', 'Dude', 'bogusdude@gmail.com', '123-456-7890',
'XL', 'Bergwall Hall 123'),
(2, 123456, 'John', 'Wengatz', 'john@gmail.com', '123-456-7890', 'L',
'Wengatz Hall 321'),
(3, 123456, 'Austin', 'Brown', 'austin@gmail.com', '123-456-7890',
'M', 'Sammy Morris Hall 218'),
(4, 123456, 'Grace', 'Olson', 'grace@gmail.com', '123-456-7890', 'S',
'Olson Hall 123'),
(5, 123456, 'John', 'Smith', 'jsmith@gmail.com', '123-456-7890', 'L',
'Sammy Morris Hall 123'),
(6, 123456, 'Barry', 'Black', 'bblack@gmail.com', '123-456-7890',
'XL', 'Swallow Robin Hall 123'),
(7, 123456, 'Timmy', 'Jones', 'tjones@gmail.com', '123-456-7890', 'L',
'Wengatz Hall 123'),
(8, 123456, 'Susie', 'Floors', 'sfloors@gmail.com', '123-456-7890',
'M', '123 Barry Ave'),
(9, 123456, 'Toto', 'Dog', 'toto@gmail.com', '123-456-7890', 'S',
'English Hall 123'),
(10, 123456, 'Carol', 'Captain', 'ccaptain@gmail.com', '123-456-7890',
'L', 'English Hall 200'),
(11, 123456, 'Stuart', 'Effort', 'seffort@gmail.com', '123-456-7890',
'XL', 'Gerig Hall 412'),
(12, 123456, 'Charles', 'Esperanto', 'cesperanto@gmail.com',
'123-456-7890', 'M', 'Bergwall Hall 123');




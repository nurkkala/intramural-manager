/* Persons */
INSERT INTO `intramuralsApp_person` VALUES
(1, 123456, 'Bogus', 'Dude', 'bogusdude@gmail.com', '123-456-7890', 'XL', 'Bergwall Hall 123'),
(2, 123456, 'John', 'Wengatz', 'john@gmail.com', '123-456-7890', 'L', 'Wengatz Hall 321'),
(3, 123456, 'Austin', 'Brown', 'austin@gmail.com', '123-456-7890', 'M', 'Sammy Morris Hall 218'),
(4, 123456, 'Grace', 'Olson', 'grace@gmail.com', '123-456-7890', 'S', 'Olson Hall 123'),
(5, 123456, 'John', 'Smith', 'jsmith@gmail.com', '123-456-7890', 'L', 'Sammy Morris Hall 123'),
(6, 123456, 'Barry', 'Black', 'bblack@gmail.com', '123-456-7890', 'XL', 'Swallow Robin Hall 123'),
(7, 123456, 'Timmy', 'Jones', 'tjones@gmail.com', '123-456-7890', 'L', 'Wengatz Hall 123'),
(8, 123456, 'Susie', 'Floors', 'sfloors@gmail.com', '123-456-7890', 'M', '123 Barry Ave'),
(9, 123456, 'Toto', 'Dog', 'toto@gmail.com', '123-456-7890', 'S', 'English Hall 123'),
(10, 123456, 'Carol', 'Captain', 'ccaptain@gmail.com', '123-456-7890', 'L', 'English Hall 200'),
(11, 123456, 'Stuart', 'Effort', 'seffort@gmail.com', '123-456-7890', 'XL', 'Gerig Hall 412'),
(12, 123456, 'Charles', 'Esperanto', 'cesperanto@gmail.com', '123-456-7890', 'M', 'Bergwall Hall 123');

/* Divisions */
INSERT INTO `intramuralsApp_division` VALUES
(1, 'Unassigned', 1),
(2, 'Unassigned', 2),
(3, 'Unassigned', 3),
(4, 'Unassigned', 4);

/* Teams */
INSERT INTO `intramuralsApp_team` VALUES
(1, 'Test team', 'password', 10, 1, '2nd North English'),
(2, 'Wizard of Oz', 'password', 9, 1, 'Off campus'),
(3, 'Oldies', 'password', 4, 1, '1st West Olson'),
(4, 'Blackjacks', 'password', 6, 1, '1st Swallow Robin'),
(5, 'Live Comfort Eagle', 'password', 5, 1, 'Foundation'),
(6, 'Test team', 'password', 10, 2, '2nd North English'),
(7, 'Wizard of Oz', 'password', 9, 2, 'Off campus'),
(8, 'Oldies', 'password', 4, 2, '1st West Olson'),
(9, 'Blackjacks', 'password', 6, 2, '1st Swallow Robin'),
(10, 'Live Comfort Eagle', 'password', 5, 2, 'Foundation'),
(11, 'Test team', 'password', 10, 3, '2nd North English'),
(12, 'Wizard of Oz', 'password', 9, 3, 'Off campus'),
(13, 'Oldies', 'password', 4, 3, '1st West Olson'),
(14, 'Blackjacks', 'password', 6, 3, '1st Swallow Robin'),
(15, 'Live Comfort Eagle', 'password', 5, 3, 'Foundation'),
(16, 'Test team', 'password', 10, 4, '2nd North English'),
(17, 'Wizard of Oz', 'password', 9, 4, 'Off campus'),
(18, 'Oldies', 'password', 4, 4, '1st West Olson'),
(19, 'Blackjacks', 'password', 6, 4, '1st Swallow Robin'),
(20, 'Live Comfort Eagle', 'password', 5, 4, 'Foundation');

/* Leagues */
INSERT INTO `intramuralsApp_league` (id, Name, Season_id) VALUES
(1, 'Men''s League', 1),
(2, 'Women''s League', 1),
(3, 'Men''s Singles', 2),
(4, 'Women''s Singles', 2),
(5, 'Co-ed Doubles', 2),
(6, 'Men''s A League', 3),
(7, 'Men''s B League', 3),
(8, 'Women''s A League', 3),
(9, 'Women''s B League', 3),
(10, 'Men''s A League', 4),
(11, 'Men''s B League', 4),
(12, 'Men''s C League', 4),
(13, 'Women''s A League', 4),
(14, 'Women''s B League', 4);

/* Locations */
INSERT INTO `intramuralsApp_location` VALUES
(1, 'Field 1', 'Eastmost intramural football field on southeast corner of campus'),
(2, 'Field 2', 'Center intramural football field on southeast corner of campus');

/* Games */
INSERT INTO `intramuralsApp_game` VALUES
(1, '2009-09-16 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(2, '2009-09-16 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(3, '2009-09-18 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(4, '2009-09-18 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(5, '2009-09-16 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(6, '2009-09-16 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(7, '2009-09-18 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(8, '2009-09-18 17:00:00', 2, 0, 9, 7, 0, 0, 0);

/* Referees */
INSERT INTO `intramuralsApp_referee` VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1);

/* Games to Referees */
INSERT INTO `intramuralsApp_game_Referees` VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 2, 2),
(5, 3, 1),
(6, 4, 1),
(7, 5, 3),
(8, 6, 3),
(9, 7, 2),
(10, 8, 2),
(11, 8, 3);

/* Leagues to Referees */
INSERT INTO `intramuralsApp_league_Referees` VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 2),
(6, 3, 4);

/* Sports */
INSERT INTO `intramuralsApp_sport` VALUES
(1, 'Football', 'Grab ball and run.', ''),
(2, 'Tennis', 'Hit the ball over the net into the court with the racket.', ''),
(3, 'Soccer', 'Kick ball into goal.', ''),
(4, 'Basketball', 'Throw the ball through the hoop.', '');

/* Seasons */
INSERT INTO `intramuralsApp_season` VALUES
(1, 'Fall Football 2009-2010', '2009-09-16 17:53:18', '2009-08-30 17:52:24', '2009-09-12 17:52:41', 1),
(2, 'Tennis 2009-2010', '2009-09-16 17:53:18', '2009-08-30 17:52:24', '2009-09-12 17:52:41', 2),
(3, 'Soccer 2009-2010', '2009-10-13 17:53:18', '2009-09-08 17:52:24', '2009-09-15 17:52:41', 3),
(4, 'Basketball 2009-2010', '2010-04-24 17:53:18', '2010-04-08 17:52:24', '2010-04-21 17:52:41', 4);

/* Attributes */
INSERT INTO `intramuralsApp_attribute` VALUES
(1, 1, 'Amateur');

/* AttributeGroups */
INSERT INTO `intramuralsApp_attributegroup` VALUES
(1, 'Level', 'The level at which the referee is authorized to referee');
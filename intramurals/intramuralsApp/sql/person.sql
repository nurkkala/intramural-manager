/* Sports */
INSERT INTO `intramuralsApp_sport` VALUES
(1, 'Football', 'Grab ball and run.', '', ''),
(2, 'Tennis', 'Hit the ball over the net into the court with the racket.', '', ''),
(3, 'Soccer', 'Kick ball into goal.', '', ''),
(4, 'Basketball', 'Throw the ball through the hoop.', '', '');

/* Seasons */
INSERT INTO `intramuralsApp_season` VALUES
(1, 'Fall Football 2009-2010', '2009-09-16 17:53:18', '2009-08-30 17:52:24', '2009-09-12 17:52:41', 1),
(2, 'Tennis 2009-2010', '2009-09-16 17:53:18', '2009-08-30 17:52:24', '2009-09-12 17:52:41', 2),
(3, 'Soccer 2009-2010', '2009-10-13 17:53:18', '2009-09-08 17:52:24', '2009-09-15 17:52:41', 3),
(4, 'Basketball 2009-2010', '2010-04-24 17:53:18', '2010-04-08 17:52:24', '2010-04-21 17:52:41', 4),
(5, 'Fall Football 2008-2009', '2008-09-16 17:53:18', '2008-08-30 17:52:24', '2008-09-12 17:52:41', 1),
(6, 'Fall Football 2010-2011', '2010-09-16 17:53:18', '2010-08-30 17:52:24', '2010-09-12 17:52:41', 1);

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

/* Teams to Members */
INSERT INTO `intramuralsApp_teammember` (id, Member_id, Team_id, PaymentStatus) VALUES
(1, 1, 1, 1),
(2, 1, 2, 1),
(3, 2, 3, 1),
(4, 3, 7, 1),
(5, 4, 8, 1),
(6, 5, 11, 1),
(7, 5, 12, 1),
(8, 6, 1, 1),
(9, 6, 2, 1),
(10, 7, 3, 1),
(11, 8, 7, 1),
(12, 9, 8, 1),
(13, 10, 11, 1),
(14, 10, 12, 1),
(15, 11, 1, 1),
(16, 11, 2, 1),
(17, 12, 3, 1),
(18, 13, 7, 1),
(19, 14, 8, 1),
(20, 15, 11, 1),
(21, 15, 12, 1),
(22, 16, 1, 1),
(23, 16, 2, 1),
(24, 17, 3, 1),
(25, 18, 7, 1),
(26, 19, 8, 1),
(27, 20, 11, 1),
(28, 20, 12, 1);

/* Leagues */
INSERT INTO `intramuralsApp_league` VALUES
(1, 'Men''s League', 1, 0),
(2, 'Women''s League', 1, 1),
(3, 'Men''s Singles', 2, 0),
(4, 'Women''s Singles', 2, 1),
(5, 'Co-ed Doubles', 2, 2),
(6, 'Men''s A League', 3, 0),
(7, 'Men''s B League', 3, 0),
(8, 'Women''s A League', 3, 1),
(9, 'Women''s B League', 3, 1),
(10, 'Men''s A League', 4, 0),
(11, 'Men''s B League', 4, 0),
(12, 'Men''s C League', 4, 0),
(13, 'Women''s A League', 4, 1),
(14, 'Women''s B League', 4, 1);

/* Locations */
INSERT INTO `intramuralsApp_location` VALUES
(1, 'Field 1', 'Eastmost intramural football field on southeast corner of campus', 1),
(2, 'Field 2', 'Center intramural football field on southeast corner of campus', 1),
(3, 'Field 3', 'Westmost intramural football field on southeast corner of campus', 1),
(4, 'Court 1', 'Tennis courts closest to Rediger Auditorium', 2),
(5, 'Court 2', 'Tennis courts 2nd closest to Rediger Auditorium', 2),
(6, 'Court 3', 'Tennis courts 3rd closest to Rediger Auditorium', 2),
(7, 'Court 4', 'Tennis courts 4th closest to Rediger Auditorium', 2),
(8, 'Field 1', 'Soccer field closest to campus', 3),
(9, 'Field 2', 'Soccer field 2nd closest to campus', 3),
(10, 'Field 3', 'Soccer field 2nd furthest from campus', 3),
(11, 'Field 4', 'Soccer field furthest from campus', 3),
(12, 'Court 1', 'Basketball court in the KSAC closest to the lobby', 4),
(13, 'Court 2', 'Basketball court in the KSAC 2nd closest to the lobby', 4),
(14, 'Court 3', 'Basketball court in the KSAC 2nd furthest from the lobby', 4),
(15, 'Court 4', 'Basketball court in the KSAC furthest from the lobby', 4);

/* Location Groups */
INSERT INTO `intramuralsApp_locationgroup` VALUES
(1, 'Football fields', ''),
(2, 'Tennis courts', ''),
(3, 'Soccer fields', ''),
(4, 'KSAC courts', '');

/* Location Groups to Sports */
INSERT INTO `intramuralsApp_locationgroup_Sports` VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4);

/* Games */
INSERT INTO `intramuralsApp_game` VALUES
(1, '2009-09-01 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(2, '2009-09-01 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(3, '2009-09-02 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(4, '2009-09-02 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(5, '2009-09-03 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(6, '2009-09-03 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(7, '2009-09-04 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(8, '2009-09-04 17:00:00', 2, 0, 9, 7, 0, 0, 0),
(9, '2009-09-04 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(10, '2009-09-05 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(11, '2009-09-06 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(12, '2009-09-06 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(13, '2009-09-07 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(14, '2009-09-07 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(15, '2009-09-07 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(16, '2009-09-08 17:00:00', 2, 0, 9, 7, 0, 0, 0),
(17, '2009-09-08 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(18, '2009-09-09 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(19, '2009-09-10 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(20, '2009-09-10 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(21, '2009-09-11 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(22, '2009-09-11 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(23, '2009-09-12 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(24, '2009-09-12 17:00:00', 2, 0, 9, 7, 0, 0, 0),
(25, '2009-09-13 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(26, '2009-09-13 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(27, '2009-09-13 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(28, '2009-09-13 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(29, '2009-09-14 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(30, '2009-09-14 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(31, '2009-09-15 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(32, '2009-09-15 17:00:00', 2, 0, 9, 7, 0, 0, 0),
(33, '2009-09-16 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(34, '2009-09-16 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(35, '2009-09-18 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(36, '2009-09-18 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(37, '2009-09-16 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(38, '2009-09-16 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(39, '2009-09-18 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(40, '2009-09-18 17:00:00', 2, 0, 9, 7, 0, 0, 0),
(41, '2009-09-17 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(42, '2009-09-17 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(43, '2009-09-19 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(44, '2009-09-19 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(45, '2009-09-20 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(46, '2009-09-21 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(47, '2009-09-21 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(48, '2009-09-22 17:00:00', 2, 0, 9, 7, 0, 0, 0),
(49, '2009-09-23 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(50, '2009-09-23 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(51, '2009-09-23 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(52, '2009-09-24 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(53, '2009-09-24 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(54, '2009-09-25 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(55, '2009-09-25 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(56, '2009-09-25 17:00:00', 2, 0, 9, 7, 0, 0, 0),
(57, '2009-09-26 16:00:00', 1, 0, 1, 2, 0, 0, 0),
(58, '2009-09-27 17:00:00', 1, 0, 3, 4, 0, 0, 0),
(59, '2009-09-27 16:00:00', 1, 0, 1, 5, 0, 0, 0),
(60, '2009-09-28 17:00:00', 1, 0, 3, 2, 0, 0, 0),
(61, '2009-09-28 16:00:00', 2, 0, 6, 7, 0, 0, 0),
(62, '2009-09-29 17:00:00', 2, 0, 8, 9, 0, 0, 0),
(63, '2009-09-30 16:00:00', 2, 0, 8, 6, 0, 0, 0),
(64, '2009-09-30 17:00:00', 2, 0, 9, 7, 0, 0, 0);

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

/* Attributes */
INSERT INTO `intramuralsApp_attribute` VALUES
(1, 1, 'Amateur');

/* AttributeGroups */
INSERT INTO `intramuralsApp_attributegroup` VALUES
(1, 'Level', 'The level at which the referee is authorized to referee');

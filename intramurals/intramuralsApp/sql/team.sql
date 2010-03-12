
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
(17, 'Wizard of Oz', 'curtain', 9, 4, 'Off campus'),
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


CREATE OR REPLACE VIEW intramuralsApp_openleague AS
       select l.id as iid 
       from intramuralsApp_league as l 
           join intramuralsApp_season as s on l.Season_id = s.id  
       where s.RegistrationStart < now() && s.RegistrationEnd > now();

CREATE OR REPLACE VIEW intramuralsApp_openteam AS
       select t.* 
       from intramuralsApp_team as t
           join intramuralsApp_division as d on t.Division_id = d.id
	   join intramuralsApp_openleague as ol on ol.iid = d.League_id;

CREATE VIEW current_leagues AS
select * from intramuralsApp_league as L inner join (select id, league_id from intramuralsApp_game as G where datediff(now(), date_add(G.StartTime, interval 2 week)) < 0 ) as CG on CG.league_id = L.id;  

/* Leagues */
INSERT INTO `intramuralsApp_league` VALUES
(1, 'Men''s League', 1, 0),
(2, 'Women''s League', 1, 1),
(3, 'Men''s Singles', 2, 0),
(4, 'Women''s Singles', 2, 1);
-- /* These are commented out because not all of these leagues have divisions, making it hard to run tests 
-- (5, 'Co-ed Doubles', 2, 2),
-- (6, 'Men''s A League', 3, 0),
-- (7, 'Men''s B League', 3, 0),
-- (8, 'Women''s A League', 3, 1),
-- (9, 'Women''s B League', 3, 1),
-- (10, 'Men''s A League', 4, 0),
-- (11, 'Men''s B League', 4, 0),
-- (12, 'Men''s C League', 4, 0),
-- (13, 'Women''s A League', 4, 1),
-- (14, 'Women''s B League', 4, 1);
-- */





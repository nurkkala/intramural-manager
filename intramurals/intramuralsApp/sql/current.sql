CREATE OR REPLACE VIEW intramuralsApp_current AS
       SELECT G.id AS Game_id, G.League_id, T.id AS Team_id, T.Division_id
       FROM intramuralsApp_game AS G 
       	    JOIN intramuralsApp_team AS T ON G.HomeTeam_id = T.id OR G.AwayTeam_id = T.id  
       WHERE datediff(now(), date_add(G.StartTime, interval 2 week)) < 0;

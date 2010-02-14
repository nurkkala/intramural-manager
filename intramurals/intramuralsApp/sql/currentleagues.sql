CREATE OR REPLACE VIEW intramuralsApp_currentleagues AS
       SELECT G.League_id
       FROM intramuralsApp_game AS G 
       WHERE datediff(now(), date_add(G.StartTime, interval 2 week)) < 0;

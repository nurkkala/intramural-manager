CREATE OR REPLACE VIEW intramuralsApp_openleagues AS
       select l.*
       from intramuralsApp_league as l 
           join intramuralsApp_season as s on l.Season_id = s.id  
       where s.RegistrationStart < now() && s.RegistrationEnd > now();

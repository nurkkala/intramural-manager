create or replace view intramuralsApp_teamranking as 
       select count(name) as ties, T.id  
       from intramuralsApp_team AS T join intramuralsApp_game AS G 
       where (T.id = HomeTeam_id and HomeTeamScore = AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore = HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_ties as 
       select count(name) as ties, T.id  
       from intramuralsApp_team AS T join intramuralsApp_game AS G 
       where (T.id = HomeTeam_id and HomeTeamScore = AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore = HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_wins as 
       select count(name) as wins, T.id  
       from intramuralsApp_team AS T join intramuralsApp_game AS G 
       where (T.id = HomeTeam_id and HomeTeamScore > AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore > HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_losses as 
       select count(name) as losses, name, T.id  
       from intramuralsApp_team AS T join intramuralsApp_game AS G 
       where (T.id = HomeTeam_id and HomeTeamScore < AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore < HomeTeamScore) 
       GROUP BY id;


DROP PROCEDURE IF EXISTS `max_wins`;
create procedure max_wins()  
       select max(wins) as max_wins 
       from intramuralsApp_wins;
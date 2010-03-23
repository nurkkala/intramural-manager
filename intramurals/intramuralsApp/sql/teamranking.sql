create or replace view intramuralsApp_list_of_teams as
       select id
       from intramuralsApp_team;

create or replace view intramuralsApp_ties as 
       select T.id, count(T.id) as ties
       from intramuralsApp_team AS T join intramuralsApp_game AS G
       where (T.id = HomeTeam_id and HomeTeamScore = AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore = HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_wins as 
       select T.id, count(T.id) as wins
       from intramuralsApp_team AS T 
       	    join intramuralsApp_game AS G on (T.id = HomeTeam_id and HomeTeamScore > AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore > HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_losses as 
       select T.id, count(T.id) as losses
       from intramuralsApp_team AS T join intramuralsApp_game AS G 
       where (T.id = HomeTeam_id and HomeTeamScore < AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore < HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_teamranking as 
       select list.id as Team_id, W.wins as wins, L.losses as losses, T.ties as ties, (W.wins - L.losses) + (W.wins / 1000) as rank
       from intramuralsApp_list_of_teams as list
	    left join intramuralsApp_wins as W on W.id = list.id
       	    left join intramuralsApp_losses as L on L.id = list.id
	    left join intramuralsApp_ties as T on T.id = list.id
       order by rank desc;


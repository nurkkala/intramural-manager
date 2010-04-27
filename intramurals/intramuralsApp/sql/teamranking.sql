create or replace view intramuralsApp_list_of_teams as
       select id
       from intramuralsApp_team;

create or replace view intramuralsApp_ties as 
       select T.id, ifnull(count(T.id),0) as ties
       from intramuralsApp_team AS T join intramuralsApp_game AS G
       where (T.id = HomeTeam_id and HomeTeamScore = AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore = HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_wins as 
       select T.id, ifnull(count(T.id),0) as wins
       from intramuralsApp_team AS T 
       	    join intramuralsApp_game AS G on (T.id = HomeTeam_id and HomeTeamScore > AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore > HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_losses as 
       select T.id, ifnull(count(T.id),0) as losses
       from intramuralsApp_team AS T join intramuralsApp_game AS G 
       where (T.id = HomeTeam_id and HomeTeamScore < AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore < HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_teamranking as 
       select list.id as Team_id, ifnull(W.wins,0) as wins, ifnull(L.losses,0) as losses, ifnull(T.ties,0) as ties, (ifnull(W.wins,0) - ifnull(L.losses,0)) + (ifnull(W.wins,0) / 1000) as rank
       from intramuralsApp_list_of_teams as list
	    left join intramuralsApp_wins as W on W.id = list.id
       	    left join intramuralsApp_losses as L on L.id = list.id
	    left join intramuralsApp_ties as T on T.id = list.id
       order by rank desc;


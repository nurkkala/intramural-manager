
create or replace view intramuralsApp_teamranking as 
       select list.id, W.wins as wins, L.losses as losses, T.ties as ties, (W.wins - L.losses) + (W.wins / 1000) as rank
       from intramuralsApp_wins as W
       	    join intramuralsApp_losses as L on W.id = L.id
	    join intramuralsApp_ties as T on T.id = W.id
	    right join intramuralsApp_list_of_teams AS list on list.id = T.id
       order by rank desc;


create or replace view intramuralsApp_ties as 
       select count(T.id) as ties, T.id  
       from intramuralsApp_team AS T join intramuralsApp_game AS G
       where (T.id = HomeTeam_id and HomeTeamScore = AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore = HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_wins as 
       select count(T.id) as wins, T.id  
       from intramuralsApp_team AS T 
       	    join intramuralsApp_game AS G on (T.id = HomeTeam_id and HomeTeamScore > AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore > HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_losses as 
       select count(T.id) as losses, T.id  
       from intramuralsApp_team AS T join intramuralsApp_game AS G 
       where (T.id = HomeTeam_id and HomeTeamScore < AwayTeamScore) or (T.id = AwayTeam_id and AwayTeamScore < HomeTeamScore) 
       GROUP BY id;

create or replace view intramuralsApp_list_of_teams as
       select id
       from intramuralsApp_team;
       



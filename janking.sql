-- # female participants
-- # male participants
-- Total # participants
-- # male teams
-- # female teams
-- # co-ed teams
-- Total # of teams
-- # participants per dorm or off campus
-- List of team names by league
-- Total income
-- IMPORTANT!     Dr. Fincannon (and others) wants to be able to report the percentage of students involved in intramurals each year.  Since we ask for student ID #s on the online registration form, is there a way to compile the info from all sports and then use this number to sort the participants and figure out the number of unique participants each year?  I thought this number would be more accurate than names since some people use nicknames. 



-- # male participants
select "-----------------------------";
select count(gender) as "Number of Male Participants" from intramuralsApp_person where Gender=0;


-- # female participants
select "-----------------------------";
select count(gender) as "Number of Female Participants" from intramuralsApp_person where Gender=1;


-- Total # participants
select "-----------------------------";
select count(distinct StudentId) as "Total Number of Participants" from intramuralsApp_person;


-- # male teams
select "-----------------------------";
select count(*) as "Number of Male Teams" from intramuralsApp_team as T join intramuralsApp_division as D on T.Division_id = D.id join intramuralsApp_league as L on D.League_id = L.id  where L.Gender = 0;


-- # female teams
select "-----------------------------";
select count(*) as "Number of Female Teams" from intramuralsApp_team as T join intramuralsApp_division as D on T.Division_id = D.id join intramuralsApp_league as L on D.League_id = L.id  where L.Gender = 1;


-- # co-ed teams
select "-----------------------------";
select count(*) as "Number of Co-Ed Teams" from intramuralsApp_team as T join intramuralsApp_division as D on T.Division_id = D.id join intramuralsApp_league as L on D.League_id = L.id  where L.Gender = 2;


-- # total teams
select "-----------------------------";
select count(*) as "Total Number of Teams" from intramuralsApp_team as T join intramuralsApp_division as D on T.Division_id = D.id join intramuralsApp_league as L on D.League_id = L.id;


-- # total teams
select "-----------------------------";
select count(*) as "Total Number of Teams" from intramuralsApp_team as T join intramuralsApp_division as D on T.Division_id = D.id join intramuralsApp_league as L on D.League_id = L.id;


----------------------------------------
-- # participants per dorm or off campus
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from Wengatz" from intramuralsApp_person where Address like "%Wengatz%";
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from Olson" from intramuralsApp_person where Address like "%Olson%";
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from English" from intramuralsApp_person where Address like "%English%";
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from Swallow" from intramuralsApp_person where Address like "%Swallow%";
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from Gerig" from intramuralsApp_person where Address like "%Gerig%";
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from Berg" from intramuralsApp_person where Address like "%Berg%";
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from Sammy" from intramuralsApp_person where Address = 'Foundation' or Address = 'Sammy II' or Address = 'Broho' or Address = 'Penthouse' of Adress="Sammy";
select "-----------------------------";
select count(distinct StudentId) as "Number of Participants from Off-Campus" from intramuralsApp_person where Address = "Off Campus";


-- List of team names by league
select "-----------------------------";
select T.name as "Teams in League"
	from intramuralsApp_team as T join intramuralsApp_division as D on T.Division_id = D.id join intramuralsApp_league as L on D.League_id = L.id join intramuralsApp_season as S on L.Season_id = S.id
	where S.Start > '2009-7-1';



-- number of _people_
select "-----------------------------";
select count(distinct StudentId) from intramuralsApp_person;








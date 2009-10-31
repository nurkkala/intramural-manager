/* Persons */
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(1, 123456, 'Bogus', 'Dude', 'bogusdude@gmail.com', '123-456-7890', 'XL', 'Bergwall Hall 123');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(2, 123456, 'John', 'Wengatz', 'john@gmail.com', '123-456-7890', 'L', 'Wengatz Hall 321');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(3, 123456, 'Austin', 'Brown', 'austin@gmail.com', '123-456-7890', 'M', 'Sammy Morris Hall 218');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(4, 123456, 'Grace', 'Olson', 'grace@gmail.com', '123-456-7890', 'S', 'Olson Hall 123');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(5, 123456, 'John', 'Smith', 'jsmith@gmail.com', '123-456-7890', 'L', 'Sammy Morris Hall 123');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(6, 123456, 'Barry', 'Black', 'bblack@gmail.com', '123-456-7890', 'XL', 'Swallow Robin Hall 123');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(7, 123456, 'Timmy', 'Jones', 'tjones@gmail.com', '123-456-7890', 'L', 'Wengatz Hall 123');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(8, 123456, 'Susie', 'Floors', 'sfloors@gmail.com', '123-456-7890', 'M', '123 Barry Ave');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(9, 123456, 'Toto', 'Dog', 'toto@gmail.com', '123-456-7890', 'S', 'English Hall 123');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(10, 123456, 'Carol', 'Captain', 'ccaptain@gmail.com', '123-456-7890', 'L', 'English Hall 200');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(11, 123456, 'Stuart', 'Effort', 'seffort@gmail.com', '123-456-7890', 'XL', 'Gerig Hall 412');
INSERT INTO `intramuralsApp_person` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(12, 123456, 'Charles', 'Esperanto', 'cesperanto@gmail.com', '123-456-7890', 'M', 'Bergwall Hall 123');

/* Sports */
INSERT INTO `intramuralsApp_sport` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'1', 'Basketball', 'Throw the ball through the hoop.'
);

INSERT INTO `intramuralsApp_sport` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'2', 'Football', 'Grab ball and run.'
);

INSERT INTO `intramuralsApp_sport` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'3', 'Soccer', 'Kick ball into goal.'
);

INSERT INTO `intramuralsApp_sport` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'4', 'Tennis', 'Hit the ball over the net into the court with the racket.'
);



/* Seasons */
INSERT INTO `intramuralsApp_season` (
`id` ,
`SeasonStart` ,
`SeasonName` ,
`RegistrationStart` ,
`RegistrationEnd`
)
VALUES (
'1', '2009-09-21 17:53:18', 'Fall Football 2009-2010', '2009-09-08 17:52:24', '2009-09-15 17:52:41'
);

INSERT INTO `intramuralsApp_season` (
`id` ,
`SeasonStart` ,
`SeasonName` ,
`RegistrationStart` ,
`RegistrationEnd`
)
VALUES (
'2', '2009-09-21 17:53:18', 'Soccer 2009-2010', '2009-09-08 17:52:24', '2009-09-15 17:52:41'
);

INSERT INTO `intramuralsApp_season` (
`id` ,
`SeasonStart` ,
`SeasonName` ,
`RegistrationStart` ,
`RegistrationEnd`
)
VALUES (
'3', '2009-09-21 17:53:18', 'Basketball 2009-2010', '2009-09-08 17:52:24', '2009-09-15 17:52:41'
);

/* Sports to Seasons */

/* Referees */
INSERT INTO `intramuralsApp_referee` (`id`, `Person_id`, `Attribute_id`) VALUES(1, 1, 1);
INSERT INTO `intramuralsApp_referee` (`id`, `Person_id`, `Attribute_id`) VALUES(2, 2, 1);
INSERT INTO `intramuralsApp_referee` (`id`, `Person_id`, `Attribute_id`) VALUES(3, 3, 1);

/* Attributes */
INSERT INTO `intramuralsApp_attribute` VALUES(1, 1, 'Amateur');

/* AttributeGroups */
INSERT INTO `intramuralsApp_attributegroup` (`id`, `AttributeGroupName`, `AttributeGroupDescription`) VALUES(1, 'Level', 'The level at which the referee is authorized to referee');
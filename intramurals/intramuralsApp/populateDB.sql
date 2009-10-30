/* Persons */
INSERT INTO `intramuralsApp_persons` (`id`, `StudentID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `ShirtSize`, `Address`) VALUES(1, 123456, 'Bogus', 'Dude', 'bogusdude@gmail.com', '123-456-7890', 'XL', 'Bergwall Hall 123');


/* Sports */
INSERT INTO `cos371-dlaskows`.`intramuralsApp_sports` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'1', 'Basketball', 'Throw the ball through the hoop.'
);

INSERT INTO `cos371-dlaskows`.`intramuralsApp_sports` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'2', 'Football', 'Grab ball and run.'
);

INSERT INTO `cos371-dlaskows`.`intramuralsApp_sports` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'3', 'Soccer', 'Kick ball into goal.'
);

INSERT INTO `cos371-dlaskows`.`intramuralsApp_sports` (
`id` ,
`SportName` ,
`SportRules`
)
VALUES (
'4', 'Tennis', 'Hit the ball over the net into the court with the racket.'
);



/* Seasons */
INSERT INTO `cos371-dlaskows`.`intramuralsApp_seasons` (
`id` ,
`SeasonStart` ,
`SeasonName` ,
`RegistrationStart` ,
`RegistrationEnd`
)
VALUES (
'1', '2009-09-21 17:53:18', 'Fall Football 2009-2010', '2009-09-08 17:52:24', '2009-09-15 17:52:41'
);

INSERT INTO `cos371-dlaskows`.`intramuralsApp_seasons` (
`id` ,
`SeasonStart` ,
`SeasonName` ,
`RegistrationStart` ,
`RegistrationEnd`
)
VALUES (
'2', '2009-09-21 17:53:18', 'Soccer 2009-2010', '2009-09-08 17:52:24', '2009-09-15 17:52:41'
);

INSERT INTO `cos371-dlaskows`.`intramuralsApp_seasons` (
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
INSERT INTO `intramuralsApp_referees` (`id`, `Person_id`, `Attribute_id`) VALUES(1, 1, 1);

/* Attributes */
INSERT INTO `intramuralsApp_attributes` VALUES(1, 1, 'Soccer');

/* AttributeGroups */
INSERT INTO `intramuralsApp_attributegroups` (`id`, `AttributeGroupName`, `AttributeGroupDescription`) VALUES(1, 'Level', 'The level at which the referee is authorized to referee');
import unittest
from intramuralsApp.models import *
from intramuralsApp.views import *

# Tests go here..
	# e.g. (http://docs.djangoproject.com/en/dev/topics/testing/)
	# class PersonTestCase(unittest.TestCase):
		# def setUp(self):
			# test...

class helperFunctionsTestCase(unittest.TestCase):
    def setUp(self):
        # for currentSeason()
        self.football = Sport(1, 'Football', '', '', '')
        self.football.save()
        self.pastSeason = Season(1, 'Fall Football 2008-2009', '2008-09-16 17:53:18', '2008-08-30 17:52:24', '2008-09-12 17:52:41', self.football.id)
        self.pastSeason.save()
        self.presentSeason = Season(2, 'Fall Football 2009-2010', '2009-09-16 17:53:18', '2009-08-30 17:52:24', '2009-09-12 17:52:41', self.football.id)
        self.presentSeason.save()
        self.futureSeason = Season(3, 'Fall Football 2010-2011', '2010-09-16 17:53:18', '2010-08-30 17:52:24', '2010-09-12 17:52:41', self.football.id)
        self.futureSeason.save()
        # for record()
        self.teamCaptain = Person(1, 1234567, "Captain", "Amazing", "captainamazing@gmail.com", 1234567890, "XL", "Sammy Morris Hall 123")
        self.teamCaptain.save()
        self.testLeague = League(1, "Test League", 2, 0)
        self.testLeague.save()
        self.testDivision = Division(1, "Test Division", 1)
        self.testDivision.save()
        self.testTeamA = Team(1, "Team A", "Password", 1, 1, "Foundation")
        self.testTeamA.save()
        self.testTeamB = Team(2, "Team B", "Password", 1, 1, "Foundation")
        self.testTeamB.save()
        self.testTeamC = Team(3, "Team C", "Password", 1, 1, "Foundation")
        self.testTeamC.save()
        self.footballFields = LocationGroup(1, "Football fields", "Map")
        self.footballFields.save()
        self.footballFieldA = Location(1, "Football field A", "Test football field description", 1)
        self.footballFieldA.save()
        self.game1 = Game(1, '2009-09-16 16:00:00', 1, 0, 1, 2, 10, 5, 1) #home win for team A
        self.game1.save()
        self.game2 = Game(2, '2009-09-17 16:00:00', 1, 0, 2, 1, 5, 10, 2) #away win for team A
        self.game2.save()
        self.game3 = Game(3, '2009-09-18 16:00:00', 1, 0, 1, 2, 10, 5, 1) #home win for team A
        self.game3.save()
        self.game4 = Game(4, '2009-09-19 16:00:00', 1, 0, 1, 2, 5, 10, 2) #away win for team B
        self.game4.save()
        self.game5 = Game(5, '2009-09-20 16:00:00', 1, 0, 2, 1, 10, 5, 1) #home win for team B
        self.game5.save()
        self.game6 = Game(6, '2009-09-21 16:00:00', 1, 0, 1, 2, 5, 5, 3) #tie between teams A and B
        self.game6.save()
        
    def testCurrentSeason(self):
        self.assertEquals(currentSeason(self.football), self.presentSeason)

    def testRecord(self):
        print record(self.testTeamA.id)
        self.assertEquals(record(self.testTeamA.id), "3-2-1")
        print record(self.testTeamB.id)
        self.assertEquals(record(self.testTeamB.id), "2-3-1")
        print record(self.testTeamC.id)
        self.assertEquals(record(self.testTeamC.id), "0-0")

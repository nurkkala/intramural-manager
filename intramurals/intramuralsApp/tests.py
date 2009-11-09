import unittest
from intramuralsApp.models import *
from intramuralsApp.views import *

# Tests go here..
	# e.g. (http://docs.djangoproject.com/en/dev/topics/testing/)
	# class PersonTestCase(unittest.TestCase):
		# def setUp(self):
			# test...

class currentSeasonTestCase(unittest.TestCase):
    def setUp(self):
        self.Football = Sport(1000, 'Football', '', '', '')
        self.Past = Season(1000, 'Fall Football 2008-2009', '2008-09-16 17:53:18', '2008-08-30 17:52:24', '2008-09-12 17:52:41', Football.id)
        self.Present = Season(1001, 'Fall Football 2009-2010', '2009-09-16 17:53:18', '2009-08-30 17:52:24', '2009-09-12 17:52:41', Football.id)
        self.Future = Season(1002, 'Fall Football 2010-2011', '2010-09-16 17:53:18', '2010-08-30 17:52:24', '2010-09-12 17:52:41', Football.id)

    def testCurrentSeason(self):
        print Football.season_set
        self.assertEquals(currentSeason(self.Football), self.Present)

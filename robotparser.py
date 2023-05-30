#!/usr/bin/python3
# robotparser.py

from urllib import robotparser

sites  =  ['www.google.com', 'www.wral.com' ]

def getDenies(site):

	paths = []

	# Create a new robot parser instance and read the site's robots file
	robot = robotparser.RobotFileParser()
	robot.set_url("http://"+site+"/robots.txt")
	robot.read()

	# For each entry, look at the rule lines and add the path to paths if disallowed
	for entry in robot.entries:
		for line in entry.rulelines:
			not line.allowance and paths.append(line.path)

	return set(paths)

for site in sites:
	print("\nDenies for " + site)
	print("\t" + "\n\t".join(getDenies(site)))




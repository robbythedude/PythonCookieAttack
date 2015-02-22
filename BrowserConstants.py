#
# This script is used to hold shared values between the import/export scripts
#

import os

print 'entering'

appDataDir = os.getenv('APPDATA') #Storing the %Appdata% directory

firefoxCookieFile = "cookies.sqlite"  #Cook file to search for in the Firefox directory
firefoxCookieFileBackup = "cookies.sqlite.bak"  #Cookie file has a backup that must be accounted for
firefoxCookieFileBackupRe = "cookies.sqlite.bak-rebuild"  #Cookie file has a backup that must be accounted for
firefoxSessionCookies = "sessionstore.js"  #These are session cookies thatmust be accounted for

if not os.path.exists('exportedCookies/'):
	os.makedirs('exportedCookies/') #Create a directory for the script to export the cookies to

print 'leaving'
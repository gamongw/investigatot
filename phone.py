# Akudama
# Edit= jsdxiwwkakaj
import phonenumbers
import sys

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def banner():
	print(""" """)
banner()

try:
	text = input("\033[1;41mPHONE NUMBER OSINT\033[0m\n\033[1;36m[*] Enter Phone: \033[0m")
	if text == "":
		print("\033[1;41mEror!\033[0m")
		sys.exit()

	pn = phonenumbers.parse(text)
	x = geocoder.description_for_number(pn,"en")
	y = carrier.name_for_number(pn,"en")
	z = timezone.time_zones_for_number(pn)

	print("\033[1;33m> \033[1;32mInfo\033[0m: ",pn)
	print("\033[1;33m> \033[1;32mDevice Type \033[0m:  Mobile Phone ",phonenumbers.can_be_internationally_dialled(pn))
	print("\033[1;33m> \033[1;32mName \033[0m:  ******* ",phonenumbers.is_carrier_specific(pn))
	print("\033[1;33m> \033[1;32mValid\033[0m: ",phonenumbers.is_valid_number(pn))
	print("\033[1;33m> \033[1;32mISP\033[0m: ",y)
	print("\033[1;33m> \033[1;32mTime Zone\033[0m: ",z)
	print("\033[1;33m> \033[1;32mLocation\033[0m: ",x)

except KeyboardInterrupt:
	print("\033[1;41mThanks for use!\033[0m")

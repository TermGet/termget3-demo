import os

class PackageManager:
	def __init__(self, name, search, install):	#And so on
		self.name = name
		self.search = search
		self.install = install
		# And so on


#At the beginning we create package managers with their syntax
apt = PackageManager("apt", "apt search ", "apt install ")
dnf = PackageManager("dnf", "dnf search ", "dnf install ")
# And so on

print("1. Search")
print("2. Install")
user = input()
# Now check which is the default package manager and stuff like this and then do
if user == "1":
	user = input("Enter search query: ")
	os.system(apt.search + user)

elif user == "2":
	user = input("enter package to install: ")
	os.system(apt.install + user)
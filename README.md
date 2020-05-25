# Secure-Password-Checker
A command line utility built with python that checks the collection of characters and finds out whether it has ever been pawned, so that you build the most secure passwords for yourself.
It uses the first four characters of the SHA1 hashed password that you build, to find out if the have been pawned.
The password taken as input remains safe on your own system.

#Built with:
Python.

#Libraries used:
* requests
* hashlib
* sys

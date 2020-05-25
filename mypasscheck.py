import requests
import hashlib
import sys

"""
make api call to the password checker, password passed as first 4 characters of sha1 hash, hence secure 

"""

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api, try again!')
    return res



"""
Number of times the hashed password appears in the leak count.

"""


def get_password_leaks_count(hashes, hash_to_check):
    #give all hashes that match
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

"""
encode the password

"""


def pwned_api_check(password):
    #check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    #print(first5_char, tail)
    #print(response)
    return get_password_leaks_count(response, tail)






def main():
    f1 = open("my_password.txt", 'r')
    password_arr = f1.read()
    password_coll = password_arr.split(" ")
    for password in password_coll:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times.., you should change your password")
        else:
            print(f"{password} was NOT found. Carry on!")

    return("done!") 


   
if __name__ == '__main__':
    sys.exit(main())


'''
All user defined functions to be defined over here.
'''

# function to hash passwords
def hashingPassword(password):
    salt=[password[i] for i in range(0,len(password),2)]
    postsalt=''.join(salt[:len(salt)/2])
    presalt=''.join(salt[len(salt)/2:])
    return (presalt+password+postsalt)

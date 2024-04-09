import itertools

def guess_password(real):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é"(-è_çà)=\'$*ù%£µ!:;,?./§^#@<>|`[]{}\\'
    attempts = 0
    for password_length in range(1, 64):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'MDP est {}. trouvé en {} essaies.'.format(guess, attempts)
            print(guess, attempts)
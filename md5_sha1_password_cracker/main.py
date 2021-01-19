import hashlib

type_of_hash = str(input('MD5 or SHA1, what would you like to hash?: '))
password_list_path = str(input('Enter the path to your password list: '))
hash_to_decrypt = str(input('Enter the hash value: '))

with open(password_list_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5' or 'MD5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found password: ' + line.strip())
                exit(0)

        if type_of_hash == 'sha1' or 'SHA1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found password: ' + line.strip())
                exit(0)

    print('404, Password not found!')

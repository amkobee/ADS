import csv
import hashlib
import os


f = open('hash_table.csv', 'a', newline='')
f.close

classes = ['desert','sea','mountain','river','forest']

duplicates = 0

for class_name in classes:
    directory = f'photos/{class_name}'

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        file_path = f'{directory}/{filename}'

        sha256_hash = hashlib.sha256()
        with open(file_path,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
            hash_sha256 = sha256_hash.hexdigest()
            #print(hash_sha256)

            # check if duplicate
            with open('hash_table.csv', 'r') as fp:
                s = fp.read()

            missing = []

            if hash_sha256 not in s:
                #print(hash_sha256)
                #print('no duplicate')
                pass
            else:
                duplicates += 1
                print('duplicate: ' + file_path + '; ' + str(hash_sha256))

            f = open('hash_table.csv', 'a', newline='')
            writer = csv.writer(f)
            row = [file_path,str(hash_sha256)]
            writer.writerow(row)
            f.close

print('amount of duplicates: ' + str(duplicates))

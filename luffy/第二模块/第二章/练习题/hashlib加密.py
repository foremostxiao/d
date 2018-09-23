import hashlib
file2 = {"expire_date": "2020-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
hash_pass = file2['password']
m5 = hashlib.md5()
pass_data= m5.update(b"hash_pass")
print(m5.digest(),type(m5.digest()))
print(m5.hexdigest())

# b'\x8e2Za\x1a\x19|\xdc\x8a\xd7\xde\x1c \x8bm\x9b' <class 'bytes'>
# # 8e325a611a197cdc8ad7de1c208b6d9b
pass_word = input('>')
pass_input = m5.update(b'pass_word')
if pass_input == pass_data:
    print('nice')
import collections
import json
from random import sample

file_path = 'rockyou.txt'
output_file = 'passwords_frequency.json'

with open(file_path, "r", encoding="utf8", errors="ignore") as file:
    passwords = file.read().splitlines()

pw_count = len(passwords)

# q1: most common password length
lengths = [len(pw) for pw in passwords]

# counter to group by the amount of times a thing happens, thanks python
# https://docs.python.org/3/library/collections.html#collections.Counter.most_common
most_common_length,mcl_occurence_count = collections.Counter(lengths).most_common(1)[0]

# q2: fraction of passwords with at least 12 and 16 characters
at_least_12 = sum(1 for password in passwords if len(password) >= 12) / pw_count
at_least_16 = sum(1 for password in passwords if len(password) >= 16) / pw_count

# q3: select 10 unique passwords that appeared only once
password_freq = collections.Counter(passwords)
unique_passwords = [password for password, count in password_freq.items() if count == 1]
selected_passwords = sample(unique_passwords, 10) if len(unique_passwords) >= 10 else unique_passwords

print(f"Q1: Most common password length is {most_common_length} with {mcl_occurence_count} appearances")
print(f"Q2: Fraction with at least 12 characters: {at_least_12:.4f}, with at least 16 characters: {at_least_16:.4f}.")
print("Q3: Sample of 10 unique passwords:", selected_passwords)

# part1 4th section, save password frequency information

sorted_password_freq = dict(sorted(password_freq.items(), key=lambda item: item[1], reverse=True))
top_1000_passwords = dict(list(sorted_password_freq.items())[:1000])
with open(output_file, 'w') as json_file:
    json.dump(sorted_password_freq, json_file,indent=2)

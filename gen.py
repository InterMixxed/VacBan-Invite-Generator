import random
import string

# Generate 150 random 40-character URLs
urls = []
for _ in range(150):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
    url = "https://vacban.wtf/?Fvacinvite=" + random_string
    urls.append(url)

# Save the URLs to a text file
with open("output.txt", "w") as file:
    for url in urls:
        file.write(url + '\n')

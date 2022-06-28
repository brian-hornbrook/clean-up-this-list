websites = ["www.google.com",
            "www.youtube.com",
            "www.dropbox.com",
            "www.quora.com",
            "www.reddit.com",
            "www.instagram.com"]

# remove dropbox and add yahoo in it's place
find_replace = 2
websites.pop(find_replace)
websites.insert(find_replace, "www.yahoo.com")

# print websites
print(websites)

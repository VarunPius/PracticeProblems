import string
import random


class Codec:
    def __init__(self):
        self.alphabets = string.ascii_letters + "0123456789"
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.alphabets) for _ in range(6))
            self.url2code[longUrl] = code
            self.code2url[code] = longUrl
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
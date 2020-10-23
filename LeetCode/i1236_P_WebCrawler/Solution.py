# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        return


"""
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = {startUrl}
        domain = startUrl.split("http://")[1].split("/")[0]
        ans = [startUrl]
        queue = collections.deque([startUrl])
        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                check = htmlParser.getUrls(url)
                for new_url in check:
                    if new_url in visited:
                        continue
                    if new_url.split("http://")[1].split("/")[0] != domain:
                        continue
                    ans.append(new_url)
                    visited.add(new_url)
                    queue.append(new_url)
        return ans
"""
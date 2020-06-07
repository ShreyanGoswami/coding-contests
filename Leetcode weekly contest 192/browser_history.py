'''
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
'''

class BrowserHistory:
    '''
    Time complexity for each operation O(1)
    Space complexity O(n) where n is the maximum number of URLs visited consecutively
    '''
    def __init__(self, homepage: str):
        self.arr = []
        self.arr.append(homepage)
        self.curr = 0
        self.toAppend = 1

    def visit(self, url: str) -> None:
        #clear everything ahead of arr and append
        self.arr = self.arr[0:self.curr+1]
        self.arr.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        if self.curr - steps < 0:
            self.curr = 0
            return self.arr[0]
        else:
            self.curr -= steps
            return self.arr[self.curr]

    def forward(self, steps: int) -> str:
        if self.curr + steps >= len(self.arr):
            self.curr = len(self.arr)-1
            return self.arr[len(self.arr)-1]
        else:
            self.curr += steps
            return self.arr[self.curr]

if __name__ == "__main__":
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")       
    browserHistory.visit("facebook.com")   
    browserHistory.visit("youtube.com")  
    print(browserHistory.back(1));                  
    print(browserHistory.back(1))
    browserHistory.forward(1)                   
    browserHistory.visit("linkedin.com");     
    print(browserHistory.forward(2))               
    print(browserHistory.back(2))                   
    print(browserHistory.back(7))                 
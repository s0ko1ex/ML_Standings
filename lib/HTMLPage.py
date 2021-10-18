class HTMLPage:
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return self.data
    
    def getFirst(self, name, edit = False):
        def find_nth(haystack, needle, n):
            start = haystack.find(needle)
            while start >= 0 and n > 1:
                start = haystack.find(needle, start+len(needle))
                n -= 1
                
            return start
        
        op = '<' + name
        cl = '</' + name + '>'
        
        if self.data.find(op) == -1:
            return -1
        
        ndata = self.data[self.data.find(op)+ len(op):]
        ndata = ndata[ndata.find('>') + 1:] # Это позволяет проглотить тег с классами
        firstclose = ndata.find(cl)
        openings = ndata[:firstclose].count(op)
        true_close = find_nth(ndata, cl, openings + 1)
        ndata = ndata[:true_close]
        cut = find_nth(self.data, cl, openings + 1)
        self.data = self.data[cut + len(cl):]
        
        return HTMLPage(ndata)
    
    def getBlocks(self, name):
        temp = self.data
        
        response = []
        
        while len(self.data) > 0:
            page = self.getFirst(name, True)
            if page == -1:
                break
            response.append(page)
        
        self.data = temp
        
        if len(response) == 1:
            response = response[0]
        
        return response 

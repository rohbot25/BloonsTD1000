#Map Class

class MAP:
    #list of coordinate points for path and hazards
    def __init__(self,path,hazards):
        self.size = 8
        self.path = path
        self.hazards = hazards

    def get_path(self):
        return self.path
    
    def get_hazards(self):
        return self.hazards
    
    def get_size(self):
        return self.size

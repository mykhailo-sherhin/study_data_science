class OwnLogger():
    
    def __init__(self):
        self.logs = {'info': None, 'warning': None, 'error': None, 'all': None}
    
    def log(self, message, level):
        self.logs[level] = message
        self.logs['all'] = message
    
    def show_last(self, level='all'):
        return self.logs[level]
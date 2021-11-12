import datetime



class Param():
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)


init_time = datetime.datetime.now()
timestamp = str(init_time.timestamp()).split('.')[0]


RECENT_SEARCH_PARAM =Param(bearer_token ='xxx',
                  file_path =f'../data/recent_search_{timestamp}.json')


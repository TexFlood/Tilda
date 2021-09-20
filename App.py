import datetime


class App:



    def __init__(self,name,url,icon):
        self.name = name
        self.url = url
        self.icon = icon
    def get_sql_command(self):
        time = datetime.datetime.now()
        #Apparently unsafe, but I think it's fine in this context. Just bad practice.
        print(f"INSERT INTO apps(name,icon,isPinned,url,createdAt,updatedAt) VALUES('{self.name}','{self.icon}','{self.url}',1,'{time}','{time}')")
        return f"INSERT INTO apps(name,icon,isPinned,url,createdAt,updatedAt) VALUES('{self.name}','{self.icon}','{self.url}',1,'{time}','{time}')"


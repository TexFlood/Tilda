import datetime


class app:

    def __init__(self, name, url, icon):
        self.name = name
        self.url = url
        self.icon = icon

    def get_sql_command(self):
        time = datetime.datetime.now()
        return ("INSERT INTO apps(name,icon,isPinned,url,createdAt,updatedAt) VALUES(?,?,?,?,?,?)",
                (self.name, self.icon, "1", self.url, time, time))

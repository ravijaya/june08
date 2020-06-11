"""demo for the singleton class"""


class DBConnection:
    ___instance = None  # class variable

    def __init__(self, connect_id):
        self.connect_id = connect_id

        if DBConnection.___instance == None:
            DBConnection.___instance = self
        else:
            raise Exception('Singleton type can\'t be instantiated twice')


if __name__ == '__main__':
    db1 = DBConnection(1001)
    db1 = DBConnection(1002)
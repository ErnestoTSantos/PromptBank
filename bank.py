class Bank:

    def __init__(self, name):
        self._name = name
        self._client = []

    def __iter__(self):
        return self._client.__iter__()
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name.length() >= 3 and name != self._name:
            self._name = name

    def insert_client(self,client, count):
        self._client.append({"Name": client.name, "Count": count})
        
    def autenticate(self, client, agency, count):
        person = None
        agency_number = None
        count_number = None

        for i in self._client:
            if i["Name"] == client:
                person = client
            if i["Count"].count == count:
                count_number = count
            if i["Count"].agency == agency:
                agency_number = agency

        if person == client and agency_number == agency and count_number == count:
            return True

        return False

    def update_client(self, client, count, oldName=None):
        while len(self._client):
            value = 0
            if self._client[value]["Name"] == client:
                self._client[value]["Count"] = count
                break
            if self._client[value]["Name"] == oldName:
                self._client[value]["Name"] = client
            value += 1

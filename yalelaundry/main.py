import requests


class _base(dict):
    def __init__(self, raw):
        self.update(raw)
        self.update(self.__dict__)

    def __repr__(self):
        return self.__name__ + '(' + str(self) + ')'


class Room(_base):
    def __init__(self, raw):
        super().__init__(raw)

        self.campus_name = raw['campus_name']
        self.name = raw['laundry_room_name']
        self.location = raw['location']
        self.status = raw['status']
        self.online = (self.status == 'online')
        self.offline = not self.online


class YaleLaundry:
    API_ROOT = 'https://gw.its.yale.edu/soa-gateway/laundry/'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get(self, endpoint: str, params: dict = {}):
        """
        Make a GET request to the API.

        :param params: dictionary of custom params to add to request.
        """
        params.update({
            'apikey': self.api_key,
            'type': 'json',
        })
        request = requests.get(self.API_ROOT + endpoint, params=params)
        if request.ok:
            return request.json()
        else:
            # TODO: Can we be more helpful?
            raise Exception('API request failed. Data returned: ' + request.text)

    def get_rooms(self):
        return [Room(raw) for raw in
                self.get('school', {'method': 'getRoomData'})['school']['laundry_rooms']['laundryroom']]

    def get_availabilities(self):
        return self.get('room', {'method': 'getNumAvailable'})

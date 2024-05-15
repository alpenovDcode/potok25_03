import json
#
# with open('Moscow.json', 'r') as file:
#     file_data = json.load(file)
#
# print(file_data['max_temp'])
# print(type(file_data))


class CityData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.city_name = self.file_data['city_name']
        self.max_temp = self.file_data['max_temp']
        self.min_temp = self.file_data['min_temp']
        try:
            self.population = self.file_data['population']
        except KeyError:
            print('')
        # self.population = self.file_data['population']
        self.humidity = self.file_data['humidity']

    def read_data(self):
        with open(self.file_path) as f:
            return json.load(f)

class NewCityData(CityData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.rainy_days = self.file_data['rainy_days']

moscow = CityData("Moscow.json")
print(moscow.city_name)
print(moscow.max_temp)
print(moscow.min_temp)
print(moscow.population)
print(moscow.humidity)
# print(moscow.rainy_days)
print(20*'-')
kazan = NewCityData('Kazan.json')
print(kazan.city_name)
print(kazan.max_temp)
print(kazan.min_temp)
try:
    print(kazan.population)
except Exception:
    print('Error')
print(kazan.humidity)
print(kazan.rainy_days)
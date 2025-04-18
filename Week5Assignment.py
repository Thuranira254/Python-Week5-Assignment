class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population

    def describe(self):
        return f"{self.name} is a city in {self.country} with a population of {self.population}."

    def __str__(self):
        return f"{self.name}, {self.country}"


class TouristCity(City):
    def __init__(self, name, country, population, attractions):
        super().__init__(name, country, population)
        self.attractions = attractions

    def describe(self):
        return f"{self.name} is a popular tourist city in {self.country} with attractions like {', '.join(self.attractions)}."


class IndustrialCity(City):
    def __init__(self, name, country, population, industries):
        super().__init__(name, country, population)
        self.industries = industries

    def describe(self):
        return f"{self.name} is an industrial hub in {self.country} known for industries like {', '.join(self.industries)}."


# Example usage
cities = [
    City("Nairobi", "Kenya", 4397000),
    TouristCity("Cairo", "Egypt", 10230000, ["Pyramids of Giza", "Egyptian Museum"]),
    IndustrialCity("Lagos", "Nigeria", 15000000, ["Oil and Gas", "Textiles"]),
    TouristCity("Dakar", "Senegal", 1146000, ["Gorée Island", "African Renaissance Monument"]),
    IndustrialCity("Johannesburg", "South Africa", 5582000, ["Mining", "Finance"]),
    City("Abidjan", "Ivory Coast", 4765000),
]

for city in cities:
    print(city.describe())
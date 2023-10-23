from datetime import datetime

class AgeCalculator:
    def __init__(self, birthdate):
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        self.today = datetime.now()

    def calculate_age_in_decimals(self):
        age = self.today - self.birthdate
        years = age.days / 365
        seconds_in_a_year = 60 * 60 * 24 * 365
        age_in_decimals = years + age.seconds / seconds_in_a_year
        return age_in_decimals

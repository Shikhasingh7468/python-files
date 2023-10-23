from age_calculator import AgeCalculator
import os
import time

def main():
    while True:
        os.system('clear')
        birthdate = "2004-10-02"

        try:
            age_calculator = AgeCalculator(birthdate)
            age_in_decimals = age_calculator.calculate_age_in_decimals()
            print(f"{age_in_decimals:.8f} Waste")
            time.sleep(2)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            time.sleep(2)

if __name__ == "__main__":
    main()

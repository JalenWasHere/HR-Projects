from datetime import datetime


class ParkedCar:
    def __init__(self, license_plate: str, check_in: object):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingMachine:
    def __init__(self, capacity: int = 10, hourly_rate: float = 2.50, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def check_in(self, license_plate: str, check_in: object = datetime.now()) -> bool:
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            return True

        return False

    def check_out(self, license_plate: str) -> float:
        total_fee = self.get_parking_fee(license_plate)
        del self.parked_cars[license_plate]
        return total_fee

    def get_parking_fee(self, license_plate: str) -> float:
        parked_car = self.parked_cars.get(license_plate)

        if parked_car:
            hours_parked = float(-(-((datetime.now() - parked_car.check_in).total_seconds()) // 3600))
            hours_parked = min(hours_parked, 24)
            return round(hours_parked * self.hourly_rate, 2)

        return 24 * self.hourly_rate


def main(parking_machine: object) -> None:
    menu_input = input('''
[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program
    ''').upper()

    match menu_input:
        case 'I':
            license_plate = input('Enter license plate: ')
            if parking_machine.check_in(license_plate):
                print('License registered')
            else:
                print('Capacity reached')
            main(parking_machine)

        case 'O':
            license_plate = input('Enter license plate: ')
            fee = parking_machine.check_out(license_plate)
            print(f'Parking fee: {fee:.2f} EUR')
            main(parking_machine)

        case _:
            print('Successfully quit program')


if __name__ == "__main__":
    parking_machine = CarParkingMachine()
    main(parking_machine)

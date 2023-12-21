from datetime import datetime


def write_to_log(line: str):
    with open('carparklog.txt', 'a') as file:
        file.write(line + '\n')


def read_log_contents() -> str:
    with open('carparklog.txt', 'r') as file:
        # Read the content of the file
        file_contents = file.read()
    return file_contents


class ParkedCar:
    def __init__(self, license_plate: str, check_in: object):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingLogger:
    def __init__(self):
        self.file = read_log_contents()
        self.log_dict = self.create_log_dict(self.file)

    def create_log_dict(self, log) -> dict:
        if not log:
            return {}
        log_array = []
        line_array = log.split("\n")
        for line in line_array:
            attributes = line.split(";")
            log_array.append(attributes)

        cpm_dict = {}
        for entry in log_array:
            cpm_name = [attribute.split('=')[1] for attribute in entry if attribute.startswith('cpm_name=')][0]
            obj = {}
            for element in entry:
                if "=" in element:
                    key = element.split('=')[0]
                    value = element.split('=')[1]
                    obj[key] = value
                else:
                    obj['date'] = element

            if cpm_name not in cpm_dict:
                cpm_dict[cpm_name] = []

            cpm_dict[cpm_name].append(obj)
        return cpm_dict

    def get_machine_fee_by_day(self, car_parking_machine_id: str, search_date: str) -> float:
        cpm_logs = self.log_dict[car_parking_machine_id]
        cpm_checkout_logs = [log for log in cpm_logs if log.get('action') == 'check-out']
        search_date = datetime.strptime(search_date, '%d-%m-%Y')
        cpm_checkout_logs_at_date = [checkout_log for checkout_log in cpm_checkout_logs if
                                     datetime.strptime(checkout_log['date'],
                                                       '%d-%m-%Y %H:%M:%S').date() == search_date.date()]
        total_parking_fee = sum(float(checkout_log['parking_fee']) for checkout_log in cpm_checkout_logs_at_date if
                                'parking_fee' in checkout_log)
        print(total_parking_fee)
        return False

    def get_total_car_fee(self, license_plate: str, ) -> float:
        # This will be used in the next assignment?
        return False


class CarParkingMachine:
    def __init__(self, id: str = "0", capacity: int = 10, hourly_rate: float = 2.50, parked_cars: dict = {}):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

        # self.logger = CarParkingLogger()

    def check_in(self, license_plate: str, check_in: object = datetime.now()) -> bool:
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            log_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            write_to_log(f"{log_time};cpm_name={self.id};license_plate={license_plate};action=check-in")
            return True

        return False

    def check_out(self, license_plate: str) -> float:
        total_fee = self.get_parking_fee(license_plate)
        log_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        write_to_log(
            f"{log_time};cpm_name={self.id};license_plate={license_plate};action=check-out;parking_fee={total_fee}"
        )
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
    # main(CarParkingLogger().get_machine_fee_by_day("0", "21-12-2023"))

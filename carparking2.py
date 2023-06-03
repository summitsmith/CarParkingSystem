import re
from datetime import datetime

def validate_time_format(time_str):
    pattern = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
    return re.match(pattern, time_str)

def calculate_parking_fee(car_type, entry_time):
    # Implement the logic to calculate the parking fee based on the car type and entry time
    # You can define your own fee structure and time-based calculations here
    # This is just a placeholder example
    if car_type == "small":
        base_fee = 2000
    elif car_type == "medium":
        base_fee = 3000
    elif car_type == "large":
        base_fee = 4000
    else:
        base_fee = 0

    # Calculate additional fees based on the time difference
    current_datetime = datetime.now()
    time_format = "%H:%M"
    entry_datetime = datetime.strptime(entry_time, time_format)
    duration = current_datetime - entry_datetime

    hours = duration.total_seconds() // 3600
    parking_fee = base_fee + hours * 1000

    return parking_fee

def main():
    print("Entebbe Airport Parking Payment System")
    print("--------------------------------------")

    max_attempts = 3

    car_type = input("Enter car type (small/medium/large): ")

    attempts = 0
    while attempts < max_attempts:
        entry_time = input("Enter entry time (HH:MM in 24-hour format): ")

        if not validate_time_format(entry_time):
            print("Invalid time format. Please enter the time in 24-hour format (HH:MM).\n")
            attempts += 1
            continue

        parking_fee = calculate_parking_fee(car_type, entry_time)
        if parking_fee == 0:
            print("Invalid car type. Program terminated.")
            return

        print("Parking Fee: ", parking_fee)
        break

    if attempts == max_attempts:
        print("Maximum number of attempts reached for entering the time. Program terminated.")
        return

    attempts = 0
    while attempts < max_attempts:
        amount_paid = float(input("Enter amount paid (UGX): "))

        if amount_paid < parking_fee:
            print("Insufficient payment. Please add: ", parking_fee - amount_paid)
        elif amount_paid == parking_fee:
            print("Successful payment. No change.")
            break
        else:
            change = amount_paid - parking_fee
            print("Successful payment. Change: ", change)
            break

        attempts += 1

    if attempts == max_attempts:
        print("Maximum number of attempts reached for making the payment. Program terminated.")
        return

if __name__ == "__main__":
    main()

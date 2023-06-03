import re
import random
from datetime import datetime


def validate_time_format(time_str):
    pattern = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
    return re.match(pattern, time_str)


def calculate_parking_fee(car_type, entry_time):
    # Calculate the parking fee based on the car type and entry time
    if car_type == "small":
        fee = 2000
    elif car_type == "medium":
        fee = 3000
    elif car_type == "large":
        fee = 4000
    else:
        return None

    current_datetime = datetime.now()
    time_format = "%H:%M"
    entry_datetime = datetime.strptime(entry_time, time_format)

    if entry_datetime >= current_datetime:
        print("Invalid entry time. Entry time cannot be in the future.")
        return None

    duration = current_datetime - entry_datetime
    hours = duration.seconds // 3600

    if hours > 2:
        additional_hours = hours - 2
        fee += additional_hours * 1000

    return fee


def generate_receipt_number(name):
    random_numbers = ''.join(random.choices('0123456789', k=5))
    receipt_number = name.upper() + "-" + random_numbers
    return receipt_number

def main():
    print("Entebbe Airport Parking Payment System")
    print("--------------------------------------")

    max_attempts = 3

    name = input("Enter your name: ")

    car_type = None
    car_type_attempts = 0
    while car_type_attempts < max_attempts:
        car_type = input("Enter car type (small/medium/large): ")

        if car_type in ["small", "medium", "large"]:
            break

        car_type_attempts += 1
        remaining_attempts = max_attempts - car_type_attempts
        print("Invalid car type. Please enter a valid car type. Remaining attempts:", remaining_attempts)

    if car_type_attempts == max_attempts:
        print("Maximum number of attempts reached for entering the car type. Program terminated.")
        return

    entry_time = None
    entry_time_attempts = 0
    while entry_time_attempts < max_attempts:
        entry_time = input("Enter entry time (HH:MM in 24-hour format): ")

        if not validate_time_format(entry_time):
            entry_time_attempts += 1
            remaining_attempts = max_attempts - entry_time_attempts
            print("Invalid time format. Please enter the time in 24-hour format (HH:MM). Remaining attempts:", remaining_attempts)
            continue

        parking_fee = calculate_parking_fee(car_type, entry_time)
        if parking_fee is None:
            print("Invalid car type. Program terminated.")
            return

        print("Parking Fee: ", parking_fee)
        break

    if entry_time_attempts == max_attempts:
        print("Maximum number of attempts reached for entering the time. Program terminated.")
        return

    payment_attempts = 0
    while payment_attempts < max_attempts:
        amount_paid = float(input("Enter amount paid (UGX): "))

        if amount_paid < parking_fee:
            print("Insufficient payment. Please add:", parking_fee - amount_paid, "UGX")
        elif amount_paid == parking_fee:
            receipt_number = generate_receipt_number(name)
            print("Receipt Number:", receipt_number)
            print("Successful payment. No change")
            print("Successful payment. No change.")
            print("Please present the receipt number at the exit.")
            break
        elif amount_paid > parking_fee:
            change = amount_paid - parking_fee
            receipt_number = generate_receipt_number(name)
            print("Receipt Number:", receipt_number)
            print("Successful payment. Change:", change, "UGX")
            print("Please present the receipt number at the exit.")
            break

        payment_attempts += 1
        remaining_attempts = max_attempts - payment_attempts
        print("Invalid payment amount. Please enter a valid amount. Remaining attempts:", remaining_attempts)

    if payment_attempts == max_attempts:
        print("Maximum number of attempts reached for entering the payment amount. Program terminated.")

    print("Thank you for using Entebbe Airport.")


if __name__ == "__main__":
    main()

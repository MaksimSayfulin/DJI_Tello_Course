from djitellopy import Tello


def main():
    tello = Tello()

    try:
        print("Подключаемся к Tello...")
        tello.connect()

        battery = tello.get_battery()
        print(f"Заряд аккумулятора: {battery}%")

    finally:
        tello.end()


if __name__ == "__main__":
    main()
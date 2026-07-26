import threading

class TrafficLight:
    def __init__(self):
        # 1 represents Road 1 (East-West) is Green
        # 2 represents Road 2 (North-South) is Green
        self.green_road = 1
        self.lock = threading.Lock()

    def carArrived(
            self,
            carId: int,                  # ID of the car
            roadId: int,                 # ID of the road the car is on (1 or 2)
            direction: int,              # Direction of the car
            turnGreen: 'Callable[[], None]', # Method to turn light green for current road
            crossCar: 'Callable[[], None]'   # Method to let the car cross
    ) -> None:
        with self.lock:
            if roadId != self.green_road:
                turnGreen()
                self.green_road = roadId

            crossCar()


from threading import Thread
import threading
import time


# Создание класса
class Knight(threading.Thread):
        def __init__(self, name: str, power: int):
                threading.Thread.__init__(self)
                self.name = name
                self.power = power #сила рыцаря

        def run(self):
                stream = 100
                day = 0
                print(f'{self.name}, на нас напали!')
                for i in range(stream):
                        if stream > 0:
                                time.sleep(1)
                                day += 1
                                stream -= self.power
                                print(f'{self.name} сражается {day} дней, осталось {stream} воинов.')
                                if stream <=0:
                                        print(f'{self.name}, одержал победу спустя {day} дней!')

# Вывод строки об окончании сражения
if __name__ == "__main__":
        first_knight = Knight('Sir Lancelot', 10)
        second_knight = Knight("Sir Galahad", 20)
        first_knight.start()
        second_knight.start()
        first_knight.join()
        second_knight.join()
        print('Все битвы закончились!')




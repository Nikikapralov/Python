import queue
import threading

if __name__ == "__main__":
    my_queue = queue.Queue()
    [my_queue.put(i) for i in range(1, 101)]
    lock = threading.Lock()
    result = [0]

    class MyThread(threading.Thread):
        def __init__(self, name, lock, result):
            threading.Thread.__init__(self)
            self.name = name
            self.lock = lock
            self.result = result

        def run(self):
            print("Starting thread")
            while True:
                try:
                    lock.acquire()
                    self.result[0] += my_queue.get(block=False)
                    lock.release()
                except queue.Empty:
                    lock.release()
                    return
                else:
                    print(self.result[0])


    thread_1 = MyThread('A', lock, result)
    thread_2 = MyThread('B', lock, result)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    print(result)


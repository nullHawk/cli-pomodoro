import time
import threading

class Timer:
    def __init__(self,end_duration, on_complete=None):
        self.__end_duration = end_duration
        self.__cur_duration = 0
        self.__running = False
        self.__paused = False
        self.__timer_thread = None
        self.on_complete = on_complete

    def start(self):
        if not self.running:
            self.__running = True
            self.__timer_thread = threading.Thread(target=self.__countdown)
            self.__timer_thread.start()

    def pause(self):
        if self.running:
            self.__paused = True
    
    def reset(self):
        self.__running = False
        self.__paused = False
        self.__cur_duration = 0
        
        if self.__timer_thread and self.__timer_thread.is_alive():
            self.__timer_thread.join()

    def resume(self):
        if self.__running and self.__paused:
            self.__paused = False

    
    def __countdown(self):
        while self.__running and self.__cur_duration < self.__end_duration:
            if not self.__paused:
                self.__cur_duration +=1 
                time.sleep(1)
        if self.__cur_duration >= self.__end_duration:
                self.__running = False
                if self.on_complete:
                    self.on_complete()  
 
import time
import threading

class Timer:
    def __init__(self,duration):
        self.duration = duration
        self.thread = None
        self.running = False
    
    def run(self):
        self.running = True
        self.thread = threading.Thread(target=self._countdown)
        self.thread.start()
    
    def _countdown(self):
        while self.duration and self.running:
            mins, secs = divmod(self.duration, 60)
            time_formate = f'{mins:02d}:{secs:02d}'
            self.callback(time_formate)
            time.sleep(1)
            self.duration -= 1
        
        if self.running:
            self.callback("Time's up!")
    
    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()
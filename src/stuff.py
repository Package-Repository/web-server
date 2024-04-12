import subprocess
from typing import Callable

class Action:    
    def __init__(self, function: Callable[[], None], redirect=False):
        self.execute = function
        self.redirect = redirect

def start_bobot():
    try:
        subprocess.run(["python", "../../launch/startup.py"])
    except Exception as e:
        print("Error:", e)

actions = {
    "launch": Action(
        lambda: start_bobot()
    )
}
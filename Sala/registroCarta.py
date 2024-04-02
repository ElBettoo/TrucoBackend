from dataclasses import dataclass
from datetime import datetime

@dataclass
class RegistroCarta:
    _user: object
    _carta: object
    _time: str = "00:00:00"

    def __post_init__(self):
        CurrentTime = datetime.now().strftime('%H:%M:%S')
        self._time = CurrentTime

    def __str__(self):
        return f"[{self._time}] '{self._user}' tiro el {self._carta}"
    
    @property
    def user(self):
        return self._user
    
    @property
    def carta(self):
        return self._carta
    
    @property
    def time(self):
        return self._time
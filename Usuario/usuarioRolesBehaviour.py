from abc import ABC, abstractmethod

class UsuarioRolesBehaviour(ABC):
    @abstractmethod
    def get_role(self):
        pass

from typing import Literal, Callable

class PowerUp():
    def __init__(self, name:str, target: Literal["enemy", "self"], effect:Callable, cooldown:float, duration:float) -> None:
        self.name = name
        self.target = target
        self.effect = effect
        self.cooldown = cooldown
        self.duration = duration

    def apply_effect(self):

        print("Activating", self.name, "...")

        self.effect()

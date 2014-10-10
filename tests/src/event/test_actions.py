from src.synergy.event.Action import Action

class A(Action):
    _depend = []

class B(Action):
    _depend = [A]

class C(Action):
    _depend = [B]

class D(Action):
    _depend = []

class F(Action):
    _depend = [C]

class E(Action):
    _depend = [B, F]

class G(Action):
    _depend = []

class H(Action):
    _depend = [B]
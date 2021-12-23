from pytest import fixture
from examples import ExampleWarrior


@fixture
def warrior():
    war = ExampleWarrior()
    return war


@fixture
def warrior_played_once():
    war = ExampleWarrior()
    war.play()
    return war

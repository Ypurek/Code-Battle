def test_war(warrior):
    init = warrior.power
    warrior.play()
    assert warrior.power + 10 == init


def test_war_played_once(warrior_played_once):
    warrior_played_once.play()
    assert warrior_played_once.power == 80

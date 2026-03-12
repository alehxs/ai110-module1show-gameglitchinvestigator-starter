from logic_utils import update_score

def test_update_score_win_first_attempt():
    assert update_score(0, "Win", 0) == 90
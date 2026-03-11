from logic_utils import check_guess

def test_canary():
    assert(True)

def test_winning_guess():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

def test_guess_too_high():
    assert check_guess(60, 50) == ("Too High", "📈 Go LOWER!")

def test_guess_too_low():
    assert check_guess(40, 50) == ("Too Low", "📉 Go HIGHER!")

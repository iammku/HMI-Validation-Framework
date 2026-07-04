def test_theme(vehicle):
    print("Theme is Blue")
def test_welcome(vehicle):
    print("Welcome animation")
def test_warning_popup(vehicle):
    actual_warnings=vehicle.generate_warnings()
    assert "Low fuel" in actual_warnings
from vehicle import Vehicle
vehicle_obj=Vehicle()
def test_speed(capsys):
    vehicle_obj.display_speed()
    text=capsys.readouterr()
    assert text.out=="Current Speed : 120\n"
def test_fuel():
    print("Fuel Test")
def test_warnings(capsys):
    vehicle_obj.show_warning()
    text1=capsys.readouterr()
    assert "Low Fuel Warning\n" in text1.out
def test_cluster_log(tmp_path):
    logfile=vehicle_obj.save_cluster_log(tmp_path)
    assert logfile.read_text()=="Cluster Boot Successful"
def test_theme():
    assert vehicle_obj.display_theme() == "Dark Theme"

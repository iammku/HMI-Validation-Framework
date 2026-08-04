def test_vehicle(framework_logger, cluster):
    framework_logger.info("Running vehicle test")
    assert cluster.get_vehicle() == "Mustang"
    # cluster.show_cluster_info()
    # print(cluster.is_speeding())
    # print(cluster.is_dark_theme())
    # print(cluster.can_vehicle_move())
def test_speed(cluster):
    assert cluster.get_speed() == 120
    assert cluster.is_speeding() == True
def test_gear(cluster):
    assert cluster.get_gear() == "Park"
def test_theme(cluster):
    expected_theme= "dark"
    assert cluster.get_theme().lower() == expected_theme
    assert cluster.is_dark_theme() is True
def test_speeding(cluster):
    assert cluster.is_speeding() == True
def test_vehicle_move(cluster):
    assert cluster.can_vehicle_move() == False
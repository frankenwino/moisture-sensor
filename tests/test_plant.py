from moisture_sensor import plant


def test_plant_variables():
    assert test_plant.plant_name == "Trinidad Scorpion"
    assert test_plant.channel == 11


def test_plant_sensor_output():
    assert isinstance(test_plant.sensor_output(), int)


def test_plant_status():
    assert isinstance(test_plant.plant_status(), dict)

test_plant = plant.Plant(plant_name="Trinidad Scorpion", channel=11)

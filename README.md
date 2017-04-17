# moisture-sensor
* Detects moisture level in soil using a moisture sensor.
* Detects air temperature and humidity using a temp/humidity sensor
* Sends email alert when no moisture is detected.
* Uploads humidity/temperature sensor output to dweet.io so you can make a dashboard on freeboard.io.

Equipment:
* Raspberry Pi
* Soil moisture sensor: https://www.modmypi.com/electronics/sensors/soil-moisture-sensor
  * Tutorial: https://www.modmypi.com/blog/raspberry-pi-plant-pot-moisture-sensor-with-email-notification-tutorial
  * Driver: https://github.com/modmypi/Moisture-Sensor/
* Temperature and humidity sensor: https://www.adafruit.com/products/393
  * Driver: https://github.com/adafruit/Adafruit_Python_DHT

Third pary services used:
* Freeboard: https://freeboard.io/
* Dweet API: http://dweet.io/

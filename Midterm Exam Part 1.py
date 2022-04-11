def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):

        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class FahrenheitToCelsius(TemperatureConversion):

        def conversion(self):
            return (self._temp - 32) * 5/9

    class CelsiusToKelvin(TemperatureConversion):

        def conversion(self):
            return self._temp + 273.15

    class KelvinToCelsius(TemperatureConversion):

        def conversion(self):
            return self._temp - 273.15

    tempInCelsius = float(input("Enter the temperature that will convert from Celsius to Kelvin: "))

    convert = CelsiusToKelvin(tempInCelsius)

    print(str(convert.conversion()) + " Kelvin")

    tempInCelsius = float(input("Enter the temperature that will convert from Kelvin to Celsius: "))
    convert = KelvinToCelsius(tempInCelsius)

    print(str(convert.conversion()) + " Celsius")

    tempInCelsius = float(input("Enter the temperature that will convert from Celsius to Fahrenheit: "))
    convert = CelsiusToFahrenheit(tempInCelsius)

    print(str(convert.conversion()) + " Fahrenheit")

    tempInCelsius = float(input("Enter the temperature that will convert from Fahrenheit to Celsius: "))
    convert = FahrenheitToCelsius(tempInCelsius)

    print(str(convert.conversion()) + " Celsius")

main()

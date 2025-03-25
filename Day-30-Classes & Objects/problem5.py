class temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
print(temperature.celsius_to_fahrenheit(25))
print(temperature.fahrenheit_to_celsius(77))
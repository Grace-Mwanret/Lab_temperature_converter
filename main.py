celsius_list = [100,20,34,42,43]
def converted_temperature(celsius_list):
    result = []

    for temp in celsius_list:
        fahrenheit = (temp * 9 / 5) + 32
        kelvin = temp + 273.15

        temp = (temp, fahrenheit, kelvin)
        result.append(temp)


    return result

final = converted_temperature (celsius_list)


for unit in final:

    celsius, fahrenheit, kelvin = unit
    print(f'{celsius}°C, {fahrenheit}°F, {kelvin}K')




# Imports
import requests, genTxt, sys

# Variables ----------------------------------------------------------------

filename = sys.argv[0]

degree_sign = u'\N{DEGREE SIGN}'

# city_name = input("Enter city name : ") - Not used currently, will add in future and add exception handling
city_name = "Glasgow"

api_key = "fe7a66faf837f159cc5fc11a4c1196dd"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Return response object
response = requests.get(complete_url)
# Convert json format data into Python format data
x = response.json()

# Functions ----------------------------------------------------------------

def wind_check(degree):
  """_summary_

  Args:
      degree (_type_): _description_

  Returns:
      _type_: _description_
  """
  if degree > 337.5 or degree < 22.5:
      outcome = '- Northerly'
  elif degree > 22.5 and degree < 67.5:
      outcome = '- North Easterly'
  elif degree > 67.5 and degree < 112.5:
      outcome = '- Easterly'
  elif degree > 112.5 and degree < 157.5:
      outcome = '- South Easterly'
  elif degree > 157.5 and degree < 202.5:
      outcome = '- Southerly'
  elif degree > 202.5 and degree < 247.5:
      outcome = '- South Westerly'
  elif degree > 247.5 and degree < 292.5:
      outcome = '- Westerly'
  else:
      outcome = '- North Westerly'
  return outcome

# Now x contains list of nested dictionaries Check the value of "cod" key
# "404", means city is found otherwise city is not found
def get_weather():
  if x["cod"] != "404":
      y = x["main"]
      current_temperature = y["temp"] - 273.15

      z = x["weather"]
      weather_description = z[0]["description"]

      w = x["wind"]
      wind_speed = w["speed"]
      wind_deg = w["deg"]

      # print following values
      location_out = "\n{0:<30} {1}\n".format("Location:", city_name)
      temp_out = "{0:<30} {1}".format(
          "Temperature (in celcius):", "{:.2f}{}\n".format(current_temperature, degree_sign))
      desc_out = "{0:<30} {1}\n".format(
          "Description:", str(weather_description).capitalize())
      winds_out = "{0:<30} {1} knots\n".format("Wind speed:", wind_speed)
      windd_out = "{0:<30} {1}\n".format("Wind direction:", "{0}{1} {2}".format(
          wind_deg, degree_sign, wind_check(wind_deg)))
      print(location_out, temp_out, desc_out, winds_out, windd_out, sep="")
  else:
      print(" City Not Found ")

# Main ----------------------------------------------------------------

if __name__ == '__main__':
    get_weather()
    genTxt.generate_script(filename)

""" This is just me typing now, so remove this, but I have included the genTxt module which I made which simply takes the name of the file and prints out the code as a separate text file.

import io

def generate_script(filename):
    print(filename)
    output = filename + "script.txt"
    with open(filename, "r") as f:
        content = f.read()
    with open(output, "w") as f:
        f.write(content) """
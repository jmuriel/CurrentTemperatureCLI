import requests
import bs4

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.57027000000005&lon=-112.08536999999995')
res.raise_for_status()

weatherPage = bs4.BeautifulSoup(res.text, features='lxml')
currentTemp = weatherPage.select('.myforecast-current-lrg')
print('The current temperature in Phoenix is ' + currentTemp[0].getText() + '.')

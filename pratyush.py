import phonenumbers as ph
form phonenumbers import carrier
from phonenumbers import geocoder
form phonenumbers import timezone

number = "+919670716387"
number = ph.parse(number)

print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number,"en"))
print(geocoder.description_for_number())

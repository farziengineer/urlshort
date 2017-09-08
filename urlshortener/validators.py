from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
	url_validator = URLValidator()

	value_1_invalid = False
	value_2_invalid = False
	try:
		url_validator(value)
	except:
		value_1_invalid = True

	url_new = "http://" + value

	try:
		url_validator(url_new)
	except:
		value_2_invalid = True

	if value_2_invalid == True and value_1_invalid == True:
		raise ValidationError("Invalid url for this field")

	return value 




def validate_dot_com(value):
	if not "com" in value:
		raise ValidationError(".com is not in the url")
	return value
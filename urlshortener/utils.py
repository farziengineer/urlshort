import random
import string


def code_genr(size=7,chars= string.ascii_lowercase + string.digits):
	
	return ''.join(random.choice(chars) for _  in range(size))


def create_shortcode(instance, size=7):
	new_shcode = code_genr(size=size)
	instance_class = instance.__class__
	qs_exists = instance_class.objects.filter(shortcode=new_shcode).exists() 

	if qs_exists:
		return create_shortcode(instance,size=7)

	return new_shcode

import random
import string

def random_string_generator(size):
	
	# generated string will caontain lowercase, upercase letters and digits
	characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
	generated_string = ''
    
	for _ in range(size):
		generated_string += random.choice(characters)
	
	return generated_string
	
	
if __name__ == '__main__':
	print(random_string_generator(20)) # pass string size as parameter

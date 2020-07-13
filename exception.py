class InvalidVoter(Exception):
	def __init__(self,msg):
		self.msg=msg
# comment1
age=int(input('enter the age'))

try:
	if age>18:
		print('valid voter')
	else:
		raise InvalidVoter('age is less than 18')
except InvalidVoter as msg:
    print('not a valid voter')
else:
    print('in else block')
    
finally:
    print('in finally block')
	
print('done')
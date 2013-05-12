import random

def gseries(n,r=2,):
	result = []
	for i in range(n):
		result.append(pow(r,i))
	return result;

def checkem(n):
	"""
	Checking to see whether does it change the array.
	"""
	n.append(5);
	return n;

#Hello world!
statement = 'Hello' + ' World!'
print statement
statement = 'Goodbye' + statement[5:]
print statement

listA = [1,2,3,4,5,6,'what am i doing here?']
print listA

listB = ['why', 'me']
listA[0] = listB;
print listA

a = 14554
b = 43
r = b;
while r>1:
	r = a % b;
	a = b;
	b = r;


print 'GCD(14554,42) is',
if r==1:
	print r
else:
	print a

print gseries(8,3)

a=[1,2,3];
checkem(a);
print checkem.__doc__
print a
print "haha"

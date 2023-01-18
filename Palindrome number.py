def checkPalindrome(num):
    n=num
    revnum=0
    while(n!=0):
        digit=n%10
        revnum=revnum*10+digit
        n=n//10
    if revnum==num:
        return True
    else:
        return False

	
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')

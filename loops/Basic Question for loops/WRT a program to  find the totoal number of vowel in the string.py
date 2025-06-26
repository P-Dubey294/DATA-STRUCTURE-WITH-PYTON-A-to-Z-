str = input ( " Please provide the string")
count = 0;
for ch in str:
    # ch chechk in vowel is present or not 
 if ch.lower() in ['a' , 'e' ,'i' ,'o' , 'u']:
  count = count+1;
print ("the totoal number of vowel is " , count)
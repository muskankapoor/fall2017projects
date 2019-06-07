def near_ten(num):
  return (num%10==0 or num%10==1 or num%10==2 or abs(10-num%10)==2 or abs(10-
  num%10)==1 or abs(10-num%10)==0)



near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
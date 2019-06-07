def count_code(str):
    count=0
    for i in range(0, len(str)):
      if str[i:i+2]=='co' and str[i+3]=='e':
        count+=1
    return count



print (count_code('codexxcode')) 
print (count_code('cozexxcope')) 

def main():
  print("Hello learners!")
  
def addmultiplenumbers(nums: list): 
  total = 0
  for num in nums:
    total = total + num 
    return total
  
  def multiplymultiplenumbers(nums: list): 
    total = 1
  for num in nums:
    total = total * num 
    return total
  
  def isiteven(nums: int):
    if num % 2 == 0:
      return True
    else:
      return False
    
  def isitaninteger(nums: int):
    if type(num) == int:
      return True
    else: 
      return False 


if __name__=="__main__":
  main()

  print(addmultiplenumbers(nums= [2,4,6,8]))
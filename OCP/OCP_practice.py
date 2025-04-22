# Practice
# Bad OCP
def get_discount(user_type):
  if user_type == "regular":
    return 5
  elif user_type == "premium":
    return 10
  elif user_type == "vip":
    return 20  

# Good OCP
class DiscountStrategy:
  def get_discount(self):
    raise NotImplementedError
  
class RegularUser(DiscountStrategy):
  def get_discount(self):
    return 5

class PremiumUser(DiscountStrategy):
  def get_discount(self):
    return 10

class VIPUser(DiscountStrategy):
  def get_discount(self):
    return 20
# Easy: Refactor a function that calculates tax for different product types to follow OCP.
# Class Based Approach
# class TaxCalculator:
#   def calculate_tax(self):
#     raise NotImplementedError
  
# class Groceries(TaxCalculator):
#   def calculate_tax(self):
#     return "Calculating tax for groceries"

# class Clothing(TaxCalculator):
#   def calculate_tax(self):
#     return "Calculating tax for clothing"

# item = Groceries()
# print(item.calculate_tax())

# Function Based Approach
# Registry to hold tax calculators
tax_calculators = {}

# The Decorator
def register_tax_calculator(product_type):
  def wrapper(func):
    tax_calculators[product_type] = func
    return func
  return wrapper

# Actual Functions
@register_tax_calculator('groceries')
def groceries_tax():
  return "Calculating tax for groceries."

@register_tax_calculator('clothing')
def clothing_tax():
  return "Calculating tax for clothing."

# The Dispather
def calculate_tax(product_type):
  tax_func = tax_calculators.get(product_type)
  if not tax_func:
    return f"No tax calculator for '{product_type}'"
  return tax_func()

print(calculate_tax('groceries'))
print(calculate_tax('utensils'))

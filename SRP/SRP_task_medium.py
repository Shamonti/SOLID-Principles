# Medium: In a Django view that validates, saves, and emails user data—separate each into its own class/function.
def validate_user(data):
  return f"Validating: {data}"

def save_user(data):
  return f"Saving: {data}"

def email_service(data):
  return f"Emailing: {data}"


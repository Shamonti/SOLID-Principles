# Practice Time
# Bad SRP example
class Report:
  def __init__(self, data):
    self.data = data
  
  def generate(self):
    return f"Report: {self.data}"
  
  def save_to_file(self, filename):
    with open(filename, 'w') as f:
      f.write(self.generate())

# Good SRP
class Report:
  def __init__(self, data):
    self.data = data

  def generate(self):
    return f"Report: {self.data}"
  
class ReportSaver:
  def save_to_file(self, report, filename):
    with open(filename, 'w') as f:
      f.write(report.generate())



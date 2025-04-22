# Easy: Refactor a class that both fetches and processes API data. Split the concerns.
class FetchAPIData():
  def __init__(self, data):
    self.data = data
  
  def fetching(self):
    return f"Fetching: {self.data}"

class ProcessAPIData():
  def __init__(self, data):
    self.data = data

  def process_api_data(self):
    return f"Processing: {self.data}"

fetcher = FetchAPIData("some data")
processor = ProcessAPIData(fetcher.fetching())
print(fetcher.fetching())
print(processor.process_api_data())
# Hard: In Django, write a view/service that generates reports in PDF, CSV, or Excel using OCP principles—add new formats easily later.
from django.http import HttpResponse

class GenerateReport:
  def generate_report(self):
    raise NotImplementedError

class PDFReport(GenerateReport):
  def generate_report(self):
    print(f"[PDF]")

class CSVReport(GenerateReport):
  def generate_report(self):
    print(f"[CSV]")

class ExcelReport(GenerateReport):
  def generate_report(self):
    print(f"[Excel]")

def get_report_generator(format_type):
      generators = {
        "pdf": PDFReport(),
        "csv": CSVReport(),
        "excel": ExcelReport(),
      }
      return generators.get(format_type)()

def download_report(request, format_type):
    message = "User report data"
    generator = get_report_generator(format_type)

    if not generator:
        return HttpResponse("Invalid format", status=400)

    generator.generate_report(message)
    return HttpResponse("Report generated!")

report = CSVReport()
# report = UnknownReport()
report.generate_report()
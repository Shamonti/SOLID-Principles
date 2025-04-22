# Hard - In Django: Create a report-export system where ReportExport is a base, and you have PDFReport, CSVReport, EmailReport. Ensure each subclass can be used anywhere the base class is expected.

class ReportExport:
  def export_report(self):
    return NotImplementedError

class PDFReport(ReportExport):
  def export_report(self):
    return "I export PDF reports."

class CSVReport(ReportExport):
  def export_report(self):
    return "I export CSV reports."

class EmailReport(ReportExport):
  def export_report(self):
    return "I export Email reports."

def export_reports(report: ReportExport):
  print(report.export_report())

export_reports(CSVReport())

# 🧠 Stretch My Brain If your subclass doesn’t use or breaks a method from the parent class—should it even be a subclass?
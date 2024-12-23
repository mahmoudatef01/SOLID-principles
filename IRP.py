class Printer:
    def print(self, document):
        pass

class Fax:
    def fax(self, document):
        pass

class Scanner:
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class ModernPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")
    
    def fax(self, document):
        print(f"Faxing {document}...")
    
    def scan(self, document):
        print(f"Scanning {document}...")

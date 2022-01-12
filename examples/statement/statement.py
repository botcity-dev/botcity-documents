import json
from dataclasses import asdict, dataclass

from botcity.document_processing import *


@dataclass
class EnergyStatement:
    account_no: str = ""
    statement_date: str = ""
    due_date: str = ""
    client_name: str = ""
    client_address: str = ""
    total_due: float = 0.0

    def to_json(self) -> str:
        """
        Returns:
            JSON string representation of this object.
        """
        return json.dumps(asdict(self))


# Instantiate Reader
reader = PDFReader()
# Read file and get parser
parser = reader.read_file("statement.pdf")

# Instantiate Energy Statement object
statement = EnergyStatement()

# Read account number
_account_no = parser.get_first_entry("Account No:")
value = parser.read(_account_no, 1.368421052631579, -1.9166666666666667, 1.1929824561403508, 3.25)

# Store account number into statement object
statement.account_no = value

# Read statement date
_statement_date = parser.get_first_entry("Statement Date:")
value = parser.read(_statement_date, 1.46, -1.9166666666666667, 0.7466666666666667, 3.1666666666666665)

# Store statement date into statement object
statement.statement_date = value

# Read due date
_due_date = parser.get_first_entry("Due Date:")
value = parser.read(_due_date, 1.7248677248677249, -1.9166666666666667, 1.2010582010582012, 3.4166666666666665)

# Store due date into statement object
statement.due_date = value

# Read client name
_service_for = parser.get_first_entry("Service For:")
value = parser.read(_service_for, -0.04219409282700422, 2.75, 0.8734177215189873, 3.4166666666666665)

# Store client name into statement object
statement.client_name = value

# Read client address
value = parser.read(_service_for, -0.0759493670886076, 6.416666666666667, 1.4767932489451476, 7.5)

# Store client address into statement object
statement.client_address = value

# Read total amount due
_total_amount_due = parser.get_first_entry("Total Amount Due")
value = parser.read(_total_amount_due, 1.9411764705882353, -2.1333333333333333, 1.022408963585434, 4.133333333333334)

# Store total amount due into statement object
statement.total_due = float(value.replace("$", ""))

# Print to terminal the statement object as JSON
print(statement.to_json())

# Expected output:
# {"account_no": "1023456789-0", "statement_date": "03/08/2016", "due_date": "03/29/2016", "client_name": "Jane Smith", "client_address": "1234 Main Street San Jose, CA 92345", "total_due": 115.28}
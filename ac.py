import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox,
    QTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QTableWidget,
    QTableWidgetItem, QFrame, QCompleter
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from num2words import num2words
from pathlib import Path


class PurchaseInvoiceUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Purchase Invoice")
        self.setGeometry(100, 50, 1200, 700)

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # ================= HEADER =================
        header = QLabel("PURCHASE INVOICE")
        header.setStyleSheet("""
            background-color: #3b6ea5;
            color: white;
            font-size: 20px;
            padding: 10px;
        """)
        main_layout.addWidget(header)

        # ================= BUTTON BAR =================
        btn_layout = QHBoxLayout()

        btn_new = QPushButton("New")
        btn_save = QPushButton("Save")
        btn_print = QPushButton("Print")

        btn_new.setStyleSheet("background-color: green; color: white; padding:5px;")
        btn_save.setStyleSheet("background-color: lightgray; padding:5px;")
        btn_print.setStyleSheet("background-color: lightgray; padding:5px;")

        btn_layout.addWidget(btn_new)
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_print)
        btn_layout.addStretch()

        main_layout.addLayout(btn_layout)

        # ================= FORM SECTION =================
        form_layout = QHBoxLayout()

        # LEFT FORM
        left_form = QGridLayout()
        left_form.setContentsMargins(0, 0, 50, 200)
        left_form.addWidget(QLabel("Doc Code"), 0, 0)
        doc_code=QLineEdit("PU")
        doc_code.setFixedHeight(30)
        left_form.addWidget(doc_code, 0, 1)

        left_form.addWidget(QLabel("Year"), 0, 2)
        year=QLineEdit("2026")
        year.setFixedHeight(30)
        left_form.addWidget(year, 0, 3)

        left_form.addWidget(QLabel("Doc No"), 0, 4)
        doc_no=QLineEdit("678")
        doc_no.setFixedHeight(30)
        left_form.addWidget(doc_no, 0, 5)

        left_form.addWidget(QLabel("Date *"), 1, 0)
        date=QLineEdit("18/04/2026")
        date.setFixedHeight(30)
        left_form.addWidget(date, 1, 1, 1, 5)

        left_form.addWidget(QLabel("Supplier *"), 2, 0)
        supplier = QComboBox()
        supplier.setFixedHeight(40)
        supplier.addItems(["Gomak Tech", "Other Supplier"])
        left_form.addWidget(supplier, 2, 1, 1, 5)

        left_form.addWidget(QLabel("Address *"), 3, 0)
        address = QTextEdit("KUJE")
        address.setFixedHeight(40)
        left_form.addWidget(address, 3, 1, 1, 5)

        form_layout.addLayout(left_form)

        # RIGHT FORM
        right_form = QGridLayout()
        right_form.setContentsMargins(0, 0, 300, 200)
        right_form.addWidget(QLabel("Supplier Invoice"), 0, 0)
        supplier_invoice=QLineEdit()
        supplier_invoice.setFixedHeight(30)
        right_form.addWidget(supplier_invoice, 0, 1)

        right_form.addWidget(QLabel("Currency *"), 1, 0)
        currency = QComboBox()
        currency.setFixedHeight(30)
        currency.addItems(["NGN", "USD"])
        right_form.addWidget(currency, 1, 1)

        right_form.addWidget(QLabel("Credit Facility *"), 2, 0)
        credit = QComboBox()
        credit.setFixedHeight(30)
        credit.addItems(["30 Days", "60 Days"])
        right_form.addWidget(credit, 2, 1)

        form_layout.addLayout(right_form)

        # SUMMARY BOX
        summary = QFrame()
        summary.setGeometry(10, 13, 4, 10)
        summary.setStyleSheet("background-color: #dfe6ee;")
        summary_layout = QGridLayout()

        amount = QLabel("Amount: 220,000.00")
        amount.setStyleSheet("font-size: 20px; font-weight: bold;")
        summary_layout.addWidget(amount)

        discount = QLabel("Discount: 0.00")
        discount.setStyleSheet("font-size: 20px; font-weight: bold;")
        summary_layout.addWidget(discount)

        vat = QLabel("VAT: 0.00")
        vat.setStyleSheet("font-size: 20px; font-weight: bold;")
        summary_layout.addWidget(vat)

        summary_layout.setContentsMargins(0, 50, 50, 200)
        total = QLabel("NGN 220,000.00")
        total.setStyleSheet("font-size: 20px; font-weight: bold;")
        summary_layout.addWidget(total)

        # summary_layout.addWidget(QLabel("Unpaid: 220,000.00"))
        # summary_layout.addWidget(QLabel("Down Payment: 1,151,500.00"))

        summary.setLayout(summary_layout)
        form_layout.addWidget(summary)

        main_layout.addLayout(form_layout)

        # ================= ADD ROW BUTTON =================
        add_btn_layout = QHBoxLayout()
        self.add_row_btn = QPushButton("+ Add Row")
        self.add_row_btn.setStyleSheet("""
            background-color: #2d89ef;
            color: white;
            padding: 6px 12px;
            font-weight: bold;
        """)
        self.add_row_btn.clicked.connect(self.add_row)

        add_btn_layout.addWidget(self.add_row_btn)
        add_btn_layout.addStretch()

        main_layout.addLayout(add_btn_layout)

        # ================= TABLE =================
        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setColumnWidth(0, 10)
        self.table.setColumnWidth(1, 300)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(4, 90)
        self.table.setHorizontalHeaderLabels([
            "Product", "Description", "Warehouse",
            "Qty", "Unit", "Unit Price", "Amount",	"Disc%","Discount", "Gross Amount",
        ])


        # Optional: double click row to delete
        # self.table.doubleClicked.connect(self.remove_row)
        header_item = QTableWidgetItem("")
        header_item.setIcon(QIcon("icons/add_32x32.png"))
        self.table.setHorizontalHeaderItem(0, header_item)
        self.table.horizontalHeader().sectionClicked.connect(self.onHeader)

        self.table.itemChanged.connect(self.handle_item_change)

        # ===== FOOTER =====
        footer = QHBoxLayout()
        self.total_label = QLabel("Total: 0.00")
        self.total_label.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #22c55e;"
        )

        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

        footer.addStretch()
        footer.addWidget(self.total_label)
        main_layout.addLayout(footer)

        # ===== PRODUCTS =====
        self.products = {
            "Rice": 500,
            "Beans": 400,
            "Garri": 300,
            "Sugar": 450
        }
        # ===== PRODUCTS =====
        self.units = {
            "1": "Pcs",
            "2": "Set",
            "3": "Ltr"
        }
        self.add_row()
        # print(self.ngn_to_words(1090))
    # ===== SEARCHABLE DROPDOWN =====
    def create_combo(self):
        combo = QComboBox()
        combo.setEditable(True)

        items = list(self.units.values())
        combo.addItems(items)

        completer = QCompleter(items)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)

        combo.setCompleter(completer)
        return combo
    # ===== ADD ROW =====
    def add_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)

        combo = self.create_combo()
      
        self.table.setCellWidget(row, 4, combo)

        # 🔍 QLineEdit with dropdown
        line = QLineEdit()
        line.setPlaceholderText("Search product...")

        items = list(self.products.keys())
        completer = QCompleter(items)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)

        line.setCompleter(completer)

        # Show dropdown while typing
        line.textEdited.connect(lambda: completer.complete())

        # When selected
        line.editingFinished.connect(
            lambda r=row, le=line: self.product_selected(r, le.text())
        )

        self.table.setCellWidget(row, 1, line)



        # Default values
        for col in [3, 5, 7]:
            item = QTableWidgetItem("0")
            item.setTextAlignment(Qt.AlignRight)
            self.table.setItem(row, col, item)

        # Read-only calculated fields
        for col in [0, 6, 8, 9]:
            item = QTableWidgetItem("")
            item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(row, col, item)
        for col in [6, 8, 9]:
            item = QTableWidgetItem("")
            item.setFlags(Qt.ItemIsEnabled)
            # self.table.horizontalHeader().setSectionsClickable(False)
            self.table.setItem(row, col, item)
    def onHeader(self, index):
        if index == 0:
            self.add_row()

    # ===== HANDLE CHANGE (FIXED) =====
    def handle_item_change(self, item):
        row = item.row()
        col = item.column()

        product = self.get_value(row, 0)

        if not product:
            return

        if col in [0, 3, 5, 6, 8, 9]:
            self.calculate_row(row)
            # print("Hiiii")
        

    # ===== PRODUCT SELECT =====
    def product_selected(self, row, name):
        if name not in self.products:
            return
        price = self.products[name]

        self.table.blockSignals(True)
        self.table.setItem(row, 5, QTableWidgetItem(str(price)))
        self.table.blockSignals(False)

        self.calculate_row(row)
    # ===== CALCULATE =====
    def calculate_row(self, row):
        try:
            qty = float(self.get_value(row, 3))
            price = float(self.get_value(row, 5))
            disc = float(self.get_value(row, 7))

            amount = qty * price
            discount = (disc / 100) * amount
            gross = amount - discount

            self.table.blockSignals(True)

            self.table.setItem(row, 6, QTableWidgetItem(f"{amount:,.2f}"))
            self.table.setItem(row, 8, QTableWidgetItem(f"{discount:,.2f}"))
            self.table.setItem(row, 9, QTableWidgetItem(f"{gross:,.2f}"))

            self.table.blockSignals(False)

            self.update_total()

        except:
            pass

    # ===== TOTAL =====
    def update_total(self):
        total = 0
        naira_words_conv = 0
        for row in range(self.table.rowCount()):
            try:
                clean_val = self.get_value(row, 9).replace(",", "")
                total += float(clean_val)
            except:
                pass

        self.total_label.setText(f"Total: {total:,.2f}")

    # ===== GET VALUE =====
    def get_value(self, row, col):
        widget = self.table.cellWidget(row, col)
        if widget:
            return widget.text()

        item = self.table.item(row, col)
        return item.text() if item else "0"
    # =================  AMOUNT TO NAIRA FUNCTION =================
    def ngn_to_words(self, amount):
        # Split naira and kobo
        naira = int(amount)
        kobo = int(round((amount - naira) * 100))
        
        naira_words = num2words(naira)
        
        if kobo > 0:
            kobo_words = num2words(kobo)
            return f"{naira_words.capitalize()} Naira and {kobo_words} Kobo".replace(" and", ",")
        else:
            return f"{naira_words.capitalize()} Naira"
    # ================= REMOVE ROW FUNCTION =================
    def remove_row(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PurchaseInvoiceUI()
    window.show()
    sys.exit(app.exec_())
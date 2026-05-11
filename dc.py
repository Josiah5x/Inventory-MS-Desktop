import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QComboBox, QCompleter
)
from PyQt5.QtCore import Qt


class POS(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern POS System")
        self.resize(1200, 650)

        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #e5e7eb;
                font-family: Segoe UI;
            }
            QTableWidget {
                background-color: #111827;
                border: none;
                gridline-color: #1f2937;
            }
            QHeaderView::section {
                background-color: #1f2937;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
            QLineEdit, QComboBox {
                background-color: #1f2937;
                border: 1px solid #374151;
                padding: 6px;
                border-radius: 6px;
            }
            QPushButton {
                padding: 10px;
                border-radius: 8px;
                font-weight: bold;
                background-color: #2563eb;
            }
            QPushButton#addBtn {
                background-color: #16a34a;
            }
        """)

        main_layout = QVBoxLayout(self)

        # ===== HEADER =====
        header = QHBoxLayout()
        title = QLabel("🧾 POS Invoice")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.add_btn = QPushButton("➕ Add Item")
        self.add_btn.setObjectName("addBtn")
        self.add_btn.clicked.connect(self.add_row)

        self.save_btn = QPushButton("💾 Save")
        self.save_btn.clicked.connect(self.save_data)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.add_btn)
        header.addWidget(self.save_btn)
        main_layout.addLayout(header)

        # ===== TABLE =====
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels([
            "Product", "Description", "Warehouse",
            "Qty", "Unit", "Unit Price",
            "Amount", "Disc%", "Discount", "Gross"
        ])

        self.table.itemChanged.connect(self.handle_item_change)
        main_layout.addWidget(self.table)

        # ===== FOOTER =====
        footer = QHBoxLayout()
        self.total_label = QLabel("Total: 0.00")
        self.total_label.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #22c55e;"
        )
        footer.addStretch()
        footer.addWidget(self.total_label)
        main_layout.addLayout(footer)

        # ===== PRODUCTS =====
        self.products = [
            {"name": "Rice", "price": 500},
            {"name": "Beans", "price": 400},
            {"name": "Garri", "price": 300},
            {"name": "Sugar", "price": 450},
        ]

        self.create_db()

    # ===== DATABASE =====
    def create_db(self):
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            description TEXT,
            warehouse TEXT,
            qty REAL,
            unit TEXT,
            unit_price REAL,
            amount REAL,
            disc_percent REAL,
            discount REAL,
            gross_amount REAL
        )
        """)
        conn.commit()
        conn.close()

    # ===== SEARCHABLE DROPDOWN =====
    def create_combo(self):
        combo = QComboBox()
        combo.setEditable(True)

        items = [p["name"] for p in self.products]
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
        combo.currentTextChanged.connect(
            lambda text, r=row: self.product_selected(r, text)
        )
        self.table.setCellWidget(row, 0, combo)

        # Default values
        for col in [3, 5, 7]:
            item = QTableWidgetItem("0")
            item.setTextAlignment(Qt.AlignRight)
            self.table.setItem(row, col, item)

        # Read-only calculated fields
        for col in [6, 8, 9]:
            item = QTableWidgetItem("")
            item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(row, col, item)

    # ===== HANDLE CHANGE (FIXED) =====
    def handle_item_change(self, item):
        row = item.row()
        col = item.column()

        if col in [3, 5, 7]:  # Qty, Price, Discount %
            self.calculate_row(row)

    # ===== PRODUCT SELECT =====
    def product_selected(self, row, name):
        for p in self.products:
            if p["name"] == name:
                self.table.blockSignals(True)
                self.table.setItem(row, 5, QTableWidgetItem(str(p["price"])))
                self.table.blockSignals(False)

                self.calculate_row(row)
                break

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

            self.table.setItem(row, 6, QTableWidgetItem(f"{amount:.2f}"))
            self.table.setItem(row, 8, QTableWidgetItem(f"{discount:.2f}"))
            self.table.setItem(row, 9, QTableWidgetItem(f"{gross:.2f}"))

            self.table.blockSignals(False)

            self.update_total()

        except:
            pass

    # ===== TOTAL =====
    def update_total(self):
        total = 0
        for row in range(self.table.rowCount()):
            try:
                total += float(self.get_value(row, 9))
            except:
                pass

        self.total_label.setText(f"Total: {total:.2f}")

    # ===== GET VALUE =====
    def get_value(self, row, col):
        widget = self.table.cellWidget(row, col)
        if widget:
            return widget.currentText()

        item = self.table.item(row, col)
        return item.text() if item else "0"

    # ===== SAVE =====
    def save_data(self):
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        for row in range(self.table.rowCount()):
            data = [self.get_value(row, col) for col in range(10)]

            cursor.execute("""
            INSERT INTO products (
                product, description, warehouse,
                qty, unit, unit_price,
                amount, disc_percent, discount, gross_amount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, data)

        conn.commit()
        conn.close()
        print("Saved!")


# ===== RUN =====
app = QApplication(sys.argv)
window = POS()
window.show()
sys.exit(app.exec_())
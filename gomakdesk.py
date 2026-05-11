import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QComboBox, QTextEdit, QHBoxLayout, QVBoxLayout,
    QGridLayout, QFrame, QTableWidget, QTableWidgetItem,
    QHeaderView, QTabWidget,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QMessageBox
)

class PurchaseInvoiceUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Purchase Invoice")
        self.resize(1920, 950)
        self.setMinimumSize(1600, 850)

        self.setStyleSheet("""
            QWidget{
                background:#f3f3f3;
                font-family: Segoe UI;
                font-size:15px;
            }

            QLabel{
                color:#111;
                font-weight:600;
            }

            QLineEdit,QComboBox,QTextEdit{
                background:#ffffff;
                border:1px solid #cfcfcf;
                border-radius:6px;
                padding:10px;
                color:#333;
                font-size:15px;
            }

            QLineEdit:focus,QComboBox:focus,QTextEdit:focus{
                border:2px solid #2d7dd2;
            }

            QPushButton{
                background:#2d7dd2;
                color:white;
                border:none;
                border-radius:6px;
                padding:10px 18px;
                font-size:15px;
                font-weight:600;
            }

            QPushButton:hover{
                background:#1f6dc0;
            }

            QTableWidget{
                background:white;
                border:none;
                gridline-color:#e5e5e5;
                font-size:14px;
            }

            QHeaderView::section{
                background:#ffffff;
                padding:12px;
                border:none;
                border-bottom:2px solid #e0e0e0;
                font-weight:700;
                color:#222;
                font-size:14px;
            }

            QTabBar::tab{
                background:#d9d9d9;
                padding:12px 30px;
                font-size:15px;
                font-weight:600;
                border-top-left-radius:5px;
                border-top-right-radius:5px;
                margin-right:2px;
            }

            QTabBar::tab:selected{
                background:#2d7dd2;
                color:white;
            }
        """)

        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ================= TOP BLUE BAR =================
        top_bar = QFrame()
        top_bar.setFixedHeight(70)
        top_bar.setStyleSheet("background:#2d7dd2;")

        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(20, 10, 20, 10)

        menu = QLabel("☰")
        menu.setStyleSheet("color:white;font-size:28px;font-weight:bold;")

        title = QLabel("PURCHASE INVOICES")
        title.setStyleSheet("""
            color:white;
            font-size:30px;
            font-weight:700;
        """)

        user = QLabel("JOSIAH. agvision.")
        user.setStyleSheet("""
            color:white;
            font-size:18px;
            font-weight:600;
        """)

        top_layout.addWidget(menu)
        top_layout.addSpacing(15)
        top_layout.addWidget(title)
        top_layout.addStretch()
        top_layout.addWidget(user)

        # ================= ACTION BAR =================
        action_bar = QFrame()
        action_bar.setFixedHeight(85)
        action_bar.setStyleSheet("background:#575757;")

        action_layout = QHBoxLayout(action_bar)
        action_layout.setContentsMargins(15, 15, 15, 15)
        action_layout.setSpacing(15)

        new_btn = QPushButton("➕ New")
        new_btn.setFixedHeight(45)
        new_btn.setStyleSheet("""
            QPushButton{
                background:#55b84d;
                color:white;
                font-size:18px;
                font-weight:700;
                border-radius:6px;
                padding:10px 20px;
            }
            QPushButton:hover{
                background:#4ca644;
            }
        """)

        print_btn = QPushButton("🖨 Print")
        refresh_btn = QPushButton("⟳")
        search_btn = QPushButton("⌕")

        invoice_info = QLabel("ISHIAQ STORE  11/05/2026 15:34")
        invoice_info.setStyleSheet("""
            color:white;
            font-size:20px;
            font-weight:500;
        """)

        for b in [print_btn, refresh_btn, search_btn]:
            b.setFixedHeight(45)

        action_layout.addWidget(new_btn)
        action_layout.addWidget(print_btn)
        action_layout.addSpacing(25)
        action_layout.addWidget(refresh_btn)
        action_layout.addWidget(search_btn)
        action_layout.addSpacing(20)
        action_layout.addWidget(invoice_info)
        action_layout.addStretch()

        # ================= TABS =================
        tabs = QTabWidget()
        tabs.setDocumentMode(True)

        invoice_tab = QWidget()
        additional_tab = QWidget()

        tabs.addTab(invoice_tab, "Invoice")
        tabs.addTab(additional_tab, "Additional Info")

        # ================= MAIN CONTENT =================
        content_layout = QVBoxLayout(invoice_tab)
        content_layout.setContentsMargins(20, 20, 20, 20)

        top_content = QHBoxLayout()
        top_content.setSpacing(30)

        # ================= LEFT FORM =================
        left_form = QFrame()
        left_layout = QGridLayout(left_form)
        left_layout.setVerticalSpacing(15)
        left_layout.setHorizontalSpacing(15)

        row = 0

        # Invoice
        left_layout.addWidget(QLabel("Invoice"), row, 0)

        inv1 = QLineEdit("PU")
        inv2 = QLineEdit("2026")
        inv3 = QLineEdit("1422")

        inv1.setFixedHeight(45)
        inv2.setFixedHeight(45)
        inv3.setFixedHeight(45)

        invoice_box = QHBoxLayout()
        invoice_box.addWidget(inv1)
        invoice_box.addWidget(inv2)
        invoice_box.addWidget(inv3)

        invoice_widget = QWidget()
        invoice_widget.setLayout(invoice_box)

        left_layout.addWidget(invoice_widget, row, 1)

        # Supplier Invoice
        left_layout.addWidget(QLabel("Supplier Invoice"), row, 2)

        supplier_invoice = QLineEdit("#0129")
        supplier_invoice.setFixedHeight(45)

        left_layout.addWidget(supplier_invoice, row, 3)

        row += 1

        # Date
        left_layout.addWidget(QLabel("Date *"), row, 0)

        date_edit = QLineEdit("11/05/2026")
        date_edit.setFixedHeight(45)

        left_layout.addWidget(date_edit, row, 1)

        # Currency
        left_layout.addWidget(QLabel("Currency *"), row, 2)

        currency = QComboBox()
        currency.addItems(["NGN", "USD", "EUR"])
        currency.setFixedHeight(45)

        left_layout.addWidget(currency, row, 3)

        row += 1

        # Supplier
        left_layout.addWidget(QLabel("Supplier *"), row, 0)

        supplier = QComboBox()
        supplier.addItem("CEEJAY ELECTRICAL TECHNOLOGY LTD")
        supplier.setFixedHeight(45)

        left_layout.addWidget(supplier, row, 1)

        # Credit Facility
        left_layout.addWidget(QLabel("Credit Facility *"), row, 2)

        credit = QComboBox()
        credit.addItems(["CREDIT", "CASH"])
        credit.setFixedHeight(45)

        left_layout.addWidget(credit, row, 3)

        row += 1

        # Address
        left_layout.addWidget(QLabel("Address *"), row, 0)

        address = QTextEdit()
        address.setText("ABUJA")
        address.setFixedHeight(90)

        left_layout.addWidget(address, row, 1)

        row += 1

        # Project
        left_layout.addWidget(QLabel("Project"), row, 0)

        project = QLineEdit()
        project.setFixedHeight(45)

        left_layout.addWidget(project, row, 1)

        # ================= SUMMARY PANEL =================
        summary = QFrame()
        summary.setFixedWidth(500)
        summary.setStyleSheet("""
            QFrame{
                background:#dfeaf4;
                border-radius:10px;
            }
        """)

        summary_layout = QVBoxLayout(summary)
        summary_layout.setContentsMargins(25, 25, 25, 25)

        amount_top = QLabel("Amount                              40,000.00")
        amount_top.setStyleSheet("""
            font-size:18px;
            font-weight:700;
            background:transparent;
        """)

        discount_label = QLabel("Discount")
        discount_label.setStyleSheet("""
            font-size:18px;
            font-weight:700;
            background:transparent;
        """)

        discount_input = QLineEdit("0.00")
        discount_input.setFixedHeight(45)

        vat_label = QLabel("VAT")
        vat_label.setStyleSheet("""
            font-size:18px;
            font-weight:700;
            background:transparent;
        """)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background:#777;")

        ngn = QLabel("NGN")
        ngn.setStyleSheet("""
            font-size:48px;
            font-weight:900;
            color:black;
            background:transparent;
        """)

        total = QLabel("40,000.00")
        total.setAlignment(Qt.AlignRight)
        total.setStyleSheet("""
            font-size:50px;
            font-weight:900;
            color:#444;
            background:transparent;
        """)

        unpaid = QLabel("Unpaid 40,000.00")
        unpaid.setAlignment(Qt.AlignRight)
        unpaid.setStyleSheet("""
            font-size:16px;
            color:#2d7dd2;
            background:transparent;
        """)

        summary_layout.addWidget(amount_top)
        summary_layout.addSpacing(15)
        summary_layout.addWidget(discount_label)
        summary_layout.addWidget(discount_input)
        summary_layout.addSpacing(10)
        summary_layout.addWidget(vat_label)
        summary_layout.addSpacing(10)
        summary_layout.addWidget(line)
        summary_layout.addSpacing(20)
        summary_layout.addWidget(ngn)
        summary_layout.addWidget(total)
        summary_layout.addSpacing(20)
        summary_layout.addWidget(unpaid)

        top_content.addWidget(left_form, 3)
        top_content.addWidget(summary, 1)

        # ================= TABLE =================
        table = QTableWidget(1, 10)
        table.setMinimumHeight(300)

        headers = [
            "Product",
            "Description",
            "Warehouse",
            "Qty",
            "Unit",
            "Unit Price",
            "Amount",
            "Disc %",
            "Discount",
            "Gross Amount"
        ]

        table.setHorizontalHeaderLabels(headers)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)

        table.setItem(0, 0, QTableWidgetItem(
            "SX460 Automatic Voltage Regulator"
        ))
        table.setItem(0, 1, QTableWidgetItem(""))
        table.setItem(0, 2, QTableWidgetItem("--None--"))
        table.setItem(0, 3, QTableWidgetItem("1.0000"))
        table.setItem(0, 4, QTableWidgetItem("Pcs"))
        table.setItem(0, 5, QTableWidgetItem("40,000.00"))
        table.setItem(0, 6, QTableWidgetItem("40,000.00"))
        table.setItem(0, 7, QTableWidgetItem("0.00"))
        table.setItem(0, 8, QTableWidgetItem("0.00"))
        table.setItem(0, 9, QTableWidgetItem("40,000.00"))

        table.setRowHeight(0, 55)

        # ================= ADD TO MAIN =================
        content_layout.addLayout(top_content)
        content_layout.addSpacing(20)
        content_layout.addWidget(table)

        main_layout.addWidget(top_bar)
        main_layout.addWidget(action_bar)
        main_layout.addWidget(tabs)

class ModuleButton(QPushButton):
    def __init__(self, icon, text):
        super().__init__()

        self.module_name = text.replace("\n", " ")

        self.setFixedSize(220, 170)
        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton{
                background: transparent;
                border:none;
                border-radius:15px;
            }

            QPushButton:hover{
                background: rgba(45,125,210,0.08);
            }

            QPushButton:pressed{
                background: rgba(45,125,210,0.15);
            }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(12)

        # ================= ICON =================
        icon_circle = QLabel(icon)
        icon_circle.setAlignment(Qt.AlignCenter)
        icon_circle.setFixedSize(74, 74)

        icon_circle.setStyleSheet("""
            QLabel{
                background:white;
                border:1px solid #d6d6d6;
                border-radius:37px;
                color:#2d7dd2;
                font-size:34px;
                font-weight:600;
            }
        """)

        # ================= TEXT =================
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)

        label.setStyleSheet("""
            QLabel{
                color:#111;
                font-size:17px;
                font-weight:500;
            }
        """)

        layout.addWidget(icon_circle, alignment=Qt.AlignCenter)
        layout.addWidget(label)

        # ================= CLICK EVENT =================
        self.clicked.connect(self.open_module)

    # =====================================================
    # BUTTON CLICK FUNCTION
    # =====================================================
    def open_module(self):
        if self.module_name == "Purchases":
            purchase_window = PurchaseInvoiceUI()
            purchase_window.show()
        else:
            QMessageBox.information(
            self,
            "Module Opened",
            "Not Found")

        # Example:
        # if self.module_name == "Accounting":
        #     self.accounting_window = AccountingWindow()
        #     self.accounting_window.show()


class DashboardUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wizard Cloud Dashboard")
        self.resize(1920, 1000)
        self.setMinimumSize(1400, 850)

        self.setStyleSheet("""
            QWidget{
                background:#f4f4f4;
                font-family: Segoe UI;
            }
        """)

        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # =====================================================
        # TOP NAVBAR
        # =====================================================
        top_bar = QFrame()
        top_bar.setFixedHeight(58)

        top_bar.setStyleSheet("""
            QFrame{
                background:#2d7dd2;
            }
        """)

        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(18, 0, 18, 0)
        top_layout.setSpacing(18)

        # ================= MENU =================
        menu = QLabel("☰")
        menu.setStyleSheet("""
            color:white;
            font-size:28px;
            font-weight:bold;
        """)

        # ================= LOGO =================
        logo = QLabel("WIZARD\nCLOUD")
        logo.setAlignment(Qt.AlignCenter)

        logo.setStyleSheet("""
            color:white;
            font-size:16px;
            font-weight:900;
        """)

        # ================= USER =================
        user = QLabel("JOSIAH. agvision.")
        user.setStyleSheet("""
            color:white;
            font-size:15px;
            font-weight:600;
        """)

        # =====================================================
        # TOP ICON BUTTONS
        # =====================================================
        def top_icon(text):
            btn = QPushButton(text)
            btn.setFixedSize(38, 38)

            btn.setStyleSheet("""
                QPushButton{
                    background:#1668c8;
                    border:none;
                    border-radius:19px;
                    color:white;
                    font-size:17px;
                    font-weight:bold;
                }

                QPushButton:hover{
                    background:#0f5bb7;
                }
            """)

            return btn

        cart = top_icon("🛒")
        bell = top_icon("🔔")
        like = top_icon("👍")
        lang = top_icon("En")
        plus = top_icon("➕")
        profile = top_icon("👤")

        # ================= TOP BUTTON CLICKS =================
        cart.clicked.connect(lambda: self.top_clicked("Cart"))
        bell.clicked.connect(lambda: self.top_clicked("Notifications"))
        like.clicked.connect(lambda: self.top_clicked("Likes"))
        lang.clicked.connect(lambda: self.top_clicked("Language"))
        plus.clicked.connect(lambda: self.top_clicked("Add"))
        profile.clicked.connect(lambda: self.top_clicked("Profile"))

        top_layout.addWidget(menu)
        top_layout.addStretch(1)

        top_layout.addWidget(logo)

        top_layout.addStretch(2)

        top_layout.addWidget(user)
        top_layout.addSpacing(20)

        top_layout.addWidget(cart)
        top_layout.addWidget(bell)
        top_layout.addWidget(like)
        top_layout.addWidget(lang)
        top_layout.addWidget(plus)
        top_layout.addWidget(profile)

        # =====================================================
        # BODY
        # =====================================================
        body = QWidget()

        body_layout = QVBoxLayout(body)
        body_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        grid = QGridLayout()
        grid.setHorizontalSpacing(70)
        grid.setVerticalSpacing(40)

        modules = [
            ("🧮", "Accounting"),
            ("🏬", "Inventory"),
            ("📈", "Sales"),

            ("🏦", "Banking"),
            ("🛒", "Purchases"),
            ("🧾", "Reports"),

            ("💰", "Fixed Assets"),
            ("🏠", "Warehouse\nManagement"),
            ("👨‍💼", "Payroll Nigeria"),

            ("📋", "Project"),
        ]

        row = 0
        col = 0

        for icon, name in modules:
            card = ModuleButton(icon, name)

            grid.addWidget(card, row, col)

            col += 1

            if col > 2:
                col = 0
                row += 1

        body_layout.addSpacing(40)
        body_layout.addLayout(grid)
        body_layout.addStretch()

        # =====================================================
        # MAIN
        # =====================================================
        main_layout.addWidget(top_bar)
        main_layout.addWidget(body)

    # =====================================================
    # TOP ICON CLICK
    # =====================================================
    def top_clicked(self, name):
        QMessageBox.information(
            self,
            "Top Menu",
            f"{name} Clicked"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setFont(QFont("Segoe UI", 10))

    window = DashboardUI()
    window.showMaximized()

    sys.exit(app.exec_())
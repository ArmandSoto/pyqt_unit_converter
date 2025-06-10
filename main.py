import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QHBoxLayout, QLineEdit, QLabel

class Unit_Converter(QWidget):
    #define the unit_converter constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.setWindowTitle("Unit Converter")
        self.create_ui()

    def create_ui(self):
        # assign QLineEdit to add it to display and refer to it for later use
        self.input_field = QLineEdit()

        # unit input field
        self.input_field.setPlaceholderText("Enter a value...")
        self.input_field.setFixedHeight(40)
        self.input_field.setFixedWidth(150)

        # Dropdown Menu of Conversions
        self.from_unit_selector = QComboBox()
        self.to_unit_selector = QComboBox()

        unit_types = ('Fahrenheit', 'Celsius', 'Kelvin')
        
        # drop-down menus
        self.from_unit_label = QLabel("From:")
        self.from_unit_selector.addItems(unit_types)
        self.from_unit_selector.setMinimumWidth(100)

        self.to_unit_label = QLabel("To:")
        self.to_unit_selector.addItems(unit_types)
        self.to_unit_selector.setMinimumWidth(100)

        # Convert button
        self.convert_button = QPushButton("Convert")

        # Converted unit
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setPlaceholderText("Converted Unit")
        self.output_field.setFixedHeight(40)
        self.output_field.setFixedWidth(150)

        # Layouts
        
        # from/to label and dropdown layouts
        from_layout = QVBoxLayout()
        from_layout.addWidget(self.from_unit_label)
        from_layout.addWidget(self.from_unit_selector)

        to_layout = QVBoxLayout()
        to_layout.addWidget(self.to_unit_label)
        to_layout.addWidget(self.to_unit_selector)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.input_field)
        h_layout.addLayout(from_layout)
        h_layout.addLayout(to_layout)
        h_layout.addWidget(self.convert_button)
        

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.output_field)

        self.setLayout(v_layout)

        # connect input to button
        self.convert_button.clicked.connect(self.convert_unit)

    def convert_unit(self):
        input_value = self.input_field.text()

        self.output_field.setText(input_value)


def main():
    app = QApplication(sys.argv)
    unit_converter = Unit_Converter()
    unit_converter.show()
    sys.exit(app.exec())
    


if __name__ == "__main__":
    main()
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QHBoxLayout, QLineEdit, QLabel
from conversions import convert

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
        
        self.from_unit_selector.addItems(unit_types)
        self.from_unit_selector.setMinimumWidth(100)

        
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
        
        # from/to dropdown layouts
        from_layout = QVBoxLayout()
        from_layout.addWidget(self.from_unit_selector)

        to_layout = QVBoxLayout()
        to_layout.addWidget(self.to_unit_selector)

        # first line -- input
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.input_field)
        h_layout.addLayout(from_layout)
        h_layout.addLayout(to_layout)
        h_layout.addWidget(self.convert_button)
        
        # second line --output
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.output_field)

        self.setLayout(v_layout)

        # connect input to button
        self.convert_button.clicked.connect(self.convert_unit)

    #dummy function that just connects convert to button
    def convert_unit(self):
        try:
            input_value = float(self.input_field.text())
            from_unit = self.from_unit_selector.currentText()
            to_unit = self.to_unit_selector.currentText()
            
            result = convert(from_unit, to_unit, input_value)
            self.output_field.setText(str(round(result, 2)))
        except ValueError:
            self.output_field.setText("Invalid input")


def main():
    app = QApplication(sys.argv)
    unit_converter = Unit_Converter()
    unit_converter.show()
    sys.exit(app.exec())
    


if __name__ == "__main__":
    main()
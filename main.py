import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QHBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import Qt
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

        unit_types = ('Fahrenheit', 'Celsius', 'Kelvin', 'Inches', 'Feet', 'Miles', 'Meters', 'Kilometers', 'Pounds', 'Kilograms', 'Ounces', 'Grams', 'Tons')
        
        # drop-down menus
        self.from_unit_selector.addItems(unit_types)
        self.from_unit_selector.setMinimumWidth(100)

        
        self.to_unit_selector.addItems(unit_types)
        self.to_unit_selector.setMinimumWidth(100)

        # Convert button
        self.convert_button = QPushButton("Convert")
        self.convert_button.setMaximumHeight(60)
        self.convert_button.setMaximumWidth(100)
        self.convert_button.setStyleSheet(
            """
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    border-radius: 20px;     
                    padding: 5px 15px;      
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
        

        # Converted unit
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setPlaceholderText("Converted Unit")
        self.output_field.setFixedHeight(40)
        self.output_field.setFixedWidth(150)


    
        # Arrow Label
        self.arrow_label = QLabel("→")
        self.arrow_label.setFixedWidth(20)
        self.arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        # Horizontal Input layout
        input_h_layout = QHBoxLayout()
        input_h_layout.addWidget(self.input_field)
        input_h_layout.addWidget(self.from_unit_selector)
        input_h_layout.addWidget(self.arrow_label)
        input_h_layout.addWidget(self.to_unit_selector)
        input_h_layout.addWidget(self.convert_button)

        # Horizontal Output layout
        output_h_layout = QHBoxLayout()
        self.converted_unit_text = QLabel("")
        output_h_layout.addWidget(self.output_field)
        output_h_layout.addWidget(self.converted_unit_text)

        
        # App Vertical Layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(input_h_layout)
        v_layout.addLayout(output_h_layout)

        self.setLayout(v_layout)

        # connect input to button
        self.convert_button.clicked.connect(self.convert_unit)

        #pushes content to the top
        v_layout.addStretch()

    def convert_unit(self):
        try:
            input_value = float(self.input_field.text())
            from_unit = self.from_unit_selector.currentText()
            to_unit = self.to_unit_selector.currentText()
            
            result = convert(from_unit, to_unit, input_value)
            
            if isinstance(result, str):
                self.output_field.setText(result)
                self.converted_unit_text.setText("")
                return # exit early if invalid conversion

            self.output_field.setText(str(round(result, 2)))
            unit = self.to_unit_selector.currentText()
            # only use degrees sign if to_unit is a temperature
            self.converted_unit_text.setText(f"° {unit}" if unit in ("Fahrenheit", "Celsius", "Kelvin") else unit)
        except ValueError:
            self.output_field.setText("Invalid Input")


def main():
    app = QApplication(sys.argv)
    unit_converter = Unit_Converter()
    unit_converter.show()
    sys.exit(app.exec())
    


if __name__ == "__main__":
    main()
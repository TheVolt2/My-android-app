# Universal Calculator Application

This application is a universal unit converter and calculator built using the Flet library for the user interface and the Pint library for handling units of measurement.

## Description

The application provides functionalities to:
1. Convert between different units of measurement.
2. Add two quantities with possibly different units.
3. Subtract one quantity from another with possibly different units.

## Features

- Supports a wide range of units including length, time, area, data, mass, temperature, and volume.
- User-friendly interface with text fields for input and buttons for actions.
- Error handling for incorrect unit inputs and non-numeric values.

## Units Mapping

A dictionary (`unit_map`) is used to map user-friendly unit abbreviations to Pint-compatible unit names. This allows users to enter units in a more intuitive way.

### Supported Units

- **Length:** мм (millimeter), см (centimeter), м (meter), км (kilometer)
- **Time:** с (second), мин (minute), час (hour), сутки (day), год (year)
- **Area:** кв.мм (square millimeter), кв.см (square centimeter), кв.м (square meter), кв.км (square kilometer)
- **Data:** бит (bit), байт (byte), кб (kilobyte), мб (megabyte), гб (gigabyte), тб (terabyte), пб (petabyte)
- **Mass:** т (tonne), кг (kilogram), мг (milligram), мкг (microgram), ц (quintal)
- **Temperature:** C (celsius), F (fahrenheit), K (kelvin)
- **Volume:** мл (milliliter), л (liter), куб.м (cubic meter)

## Functions

### Conversion

The `convert_units` function takes a value and its units and converts it to the target units using the Pint library.

### Addition and Subtraction

The `add_or_subtract_units` function handles both addition and subtraction of quantities. It converts the quantities to their base units and then performs the specified operation.

## User Interface

### Input Fields

- `value1_input`: Input field for the first value.
- `unit1_input`: Input field for the unit of the first value.
- `value2_input`: Input field for the second value.
- `unit2_input`: Input field for the unit of the second value.
- `to_unit_input`: Input field for the target unit in conversion operations.

### Buttons

- **Convert**: Converts the first value from its unit to the target unit.
- **Add**: Adds the first value and the second value with their respective units.
- **Subtract**: Subtracts the second value from the first value with their respective units.
- **Clear**: Clears all input fields and the result text.

### Result Display

- `result_text`: Displays the result of the operations.

## Main Function

The `main` function sets up the UI elements, defines event handlers for the buttons, and updates the page.

## Running the Application

To run the application, call the `ft.app(target=main)` function.

```python
ft.app(target=main)

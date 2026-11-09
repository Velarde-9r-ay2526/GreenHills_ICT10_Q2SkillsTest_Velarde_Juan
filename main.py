from pyscript import display, document

def search_element(e):

    document.getElementById('result').innerHTML = ''
    
   
    symbol = document.getElementById('elementSymbol').value.strip()

    non_metals = {
        'h': {'name': 'Hydrogen', 'number': 1, 'mass': '1.008'},
        'c': {'name': 'Carbon', 'number': 6, 'mass': '12.011'},
        'n': {'name': 'Nitrogen', 'number': 7, 'mass': '14.007'},
        'o': {'name': 'Oxygen', 'number': 8, 'mass': '15.999'},
        'f': {'name': 'Fluorine', 'number': 9, 'mass': '18.998'},
        'p': {'name': 'Phosphorus', 'number': 15, 'mass': '30.974'},
        's': {'name': 'Sulfur', 'number': 16, 'mass': '32.06'},
        'cl': {'name': 'Chlorine', 'number': 17, 'mass': '35.45'},
        'se': {'name': 'Selenium', 'number': 34, 'mass': '78.971'},
        'br': {'name': 'Bromine', 'number': 35, 'mass': '79.904'},
        'i': {'name': 'Iodine', 'number': 53, 'mass': '126.90'},
        'he': {'name': 'Helium', 'number': 2, 'mass': '4.0026'},
        'ne': {'name': 'Neon', 'number': 10, 'mass': '20.180'},
        'ar': {'name': 'Argon', 'number': 18, 'mass': '39.948'},
        'kr': {'name': 'Krypton', 'number': 36, 'mass': '83.80'},
        'xe': {'name': 'Xenon', 'number': 54, 'mass': '131.29'},
        'rn': {'name': 'Radon', 'number': 86, 'mass': '222'}
    }

    symbol_lower = symbol.lower()
    element_check = symbol_lower in non_metals

    if element_check:
        el = non_metals[symbol_lower]
        details_text = f"Symbol: {symbol} | Name: {el['name']} | Atomic Number: {el['number']} | Atomic Mass: {el['mass']}"
        display_message = ('Error: The element does not exist in the non-metals list.', details_text)
    else:
        display_message = (f"Error: The element '{symbol}' does not exist in the non-metals list.", '')

    display(display_message[element_check], target='result')
import re

def escape_quotes(text):
    def replace_func(match):
        word = match.group(1)
        return f"\\'{''.join(c if c != "'" else '\\'' for c in word)}\\'"

    pattern = r"'([^']+)'"
    return re.sub(pattern, replace_func, text)

# Example usage
input_text = "This is a 'sample' text with 'multiple' quotations. Don't touch unquoted text."
output_text = escape_quotes(input_text)
print(output_text)

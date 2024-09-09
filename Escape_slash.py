import re

def escape_quoted_text(text):
    # Pattern to find text within single quotes or contractions like You're, Don't
    pattern = r"(?<!\w)'([^']+)'(?!\w)|(\b\w*'\w*\b)"

    def replace_func(match):
        if match.group(1):  # Matches quoted text like 'khajur'
            word = match.group(1)
            escaped_word = "\\'" + word + "\\'"  # Add escaped single quotes around the word
            return escaped_word
        elif match.group(2):  # Matches contractions like You're
            word = match.group(2)
            escaped_word = word.replace("'", "\\'")
            return escaped_word

    # Substitute with the escaped text using the replace function
    return re.sub(pattern, replace_func, text)

# Example usage
input_text = "You're amazing. This is a 'khajur'. Don't touch unquoted text. I can't believe it, 'really'."
output_text = escape_quoted_text(input_text)
print(output_text)

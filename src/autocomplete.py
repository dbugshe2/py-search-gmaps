import readline

def autocomplete_input(prompt, options):
    def complete(text, state):
        matches = [opt for opt in options if opt.startswith(text)]
        return matches[state] if state < len(matches) else None

    readline.set_completer(complete)
    readline.parse_and_bind('tab: complete')

    user_input = input(prompt)
    return user_input

# Example usage
options = ["apple", "banana", "cherry", "grape", "orange", "pear", "pineapple"]

selected_option = autocomplete_input("Select a fruit: ", options)

print("You selected:", selected_option)

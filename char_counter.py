class CharCounter:
    """
    CharCounter is a class that counts occurrences of each character
    in a given string and prints the result.
    """

    def __init__(self, text):
        """
        Initialize the CharCounter with the input string.

        :param text: The input string containing characters to be counted.
        """
        self.text = text

    def count_chars(self):
        """
        Counts the occurrences of each character in the input string.

        :return: A dictionary with characters as keys and their occurrences as values.
        """
        char_dict = {}

        # Count each character in the provided string
        for char in self.text:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        return char_dict

    def print_results(self, char_dict):
        """
        Prints the character counts to the console.

        :param char_dict: A dictionary with characters as keys and their counts as values.
        """
        for char, count in sorted(char_dict.items()):
            # Print each character and its count
            print(f'{repr(char)}: {count}')

    def process(self):
        """
        Processes the input string by counting characters and printing the results.
        """
        # Count the characters in the input string
        char_count = self.count_chars()

        # Print the counted characters
        self.print_results(char_count)


if __name__ == '__main__':
    # Example usage:
    input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    # Create an instance of CharCounter with the string
    char_counter = CharCounter(input_text)

    # Run the process to count characters and print results
    char_counter.process()

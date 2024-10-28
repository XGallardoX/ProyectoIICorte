# main.py
import sys
from lexer import lex  # Import lexer
from parser import Parser  # Import parser

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Lexical analysis: generate tokens
    tokens = lex(input_file)

    # Debugging: print the generated tokens
    #print(tokens)  # Add this line to inspect the tokens

    # Create parser instance and parse the tokens
    parser = Parser(tokens)
    try:
        parser.parse_statements()  # Start parsing
        print("Parsing completed successfully.")
    except SyntaxError as e:
        print(f"Syntax error: {e}")

if __name__ == "__main__":
    main()


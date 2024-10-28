# parser.py

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        # Get the current token
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        # Move to the next token
        self.pos += 1

    def match(self, expected_type):
        token = self.current_token()
        
        if token and len(token) >= 4:
            line_num, column_num = token[2], token[3]
        else:
            line_num, column_num = "unknown", "unknown"
        
        if token and token[0] == expected_type:
            self.advance()
            return token
        else:
            found_token = token[0] if token else "EOF"
            raise SyntaxError(f'<{line_num},{column_num}> Syntax error: found "{found_token}" Expected "{expected_type}"')


    def parse_expression(self):
        # Example of a function to parse an expression
        if self.current_token()[0] == 'id':
            return self.match('id')
        else:
            raise SyntaxError(f"Invalid expression at {self.current_token()}")

    def parse_statements(self):
    # Parse multiple statements
        while self.current_token():
            self.parse_statement()  # Parse each statement
            self.advance()          # Ensure to advance to the next token


    def parse_statement(self):
        token = self.current_token()
        if token[0] == 'if':
            self.parse_if_statement()
        elif token[0] == 'while':
            self.parse_while_statement()
        # Add other statements following the rules in pyGrammar.txt

    def parse_if_statement(self):
        # Parse if statements following the grammar
        self.match('if')
        self.parse_expression()
        self.match(':')

        # Parse the block inside the if statement
        self.parse_block()

    def parse_block(self):
        # Handle indented block parsing (for compound statements)
        pass  # Implement block parsing as per grammar

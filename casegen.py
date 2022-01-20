import sys
LEXER_START = 101
PARSER_START = 201


templateHeader ='''import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):'''

templateString ='''
    def test_case_{}(self):
        self.assertTrue(TestLexer.test(\"\"\"{}\"\"\",\"{}\",{}))'''


parserHeader ='''import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):'''

parserString ='''
    def test_case_{}(self):
        self.assertTrue(TestParser.test(
\"\"\"{}\"\"\"
    ,\"{}\",{}))'''


if (sys.argv[1] =='lexer'):
    with open("lexer_case.txt", "r") as f:
        with open("./test/LexerSuite.py", "w") as o:
            o.write(templateHeader + "\n")
            for line in f.readlines():
                newInput = line.split('|')
                templateTest = templateString.format(LEXER_START , newInput[0], newInput[1][:-1], LEXER_START)
                LEXER_START += 1
                o.write(templateTest)

if (sys.argv[1] =='parser'):
    with open("parser_case.txt", "r") as f:
        with open("./test/ParserSuite.py", "w") as o:
            o.write(parserHeader + "\n")
            for line in f.read().split('---\nin:\n')[1:]:
                newInput = line.split('\nout:')
                parserTest = parserString.format(PARSER_START , newInput[0], newInput[1][:-1], PARSER_START)
                PARSER_START += 1
                o.write(parserTest)
                # print('===')
                # print(parserTest)
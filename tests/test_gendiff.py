from gendiff.gendiff import generate_diff
import os
from gendiff import parser


FILE1_JSON_PATH = "tests/fixtures/file1.json"
FILE2_JSON_PATH = "tests/fixtures/file2.json"
FILE1_YAML_PATH = "tests/fixtures/file1.yaml"
FILE2_YAML_PATH = "tests/fixtures/file2.yaml"
RESULT_PATH = "tests/fixtures/result.txt"


def test_geneate_diff():
  print('!!!!!!!!!!!!!!!!!!!!')
  print(parser.file_parsing(FILE1_JSON_PATH))
  print('!!!!!!!!!!!!!!!!!!!!')
  print(parser.file_parsing(FILE1_YAML_PATH))
  print('!!!!!!!!!!!!!!!!!!!!')
  print(parser.file_parsing(FILE2_JSON_PATH))
  print('!!!!!!!!!!!!!!!!!!!!')
  print(parser.file_parsing(FILE2_YAML_PATH))
  result = open(os.path.abspath(RESULT_PATH)).read()
  assert result == generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH)
  assert result == generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH)

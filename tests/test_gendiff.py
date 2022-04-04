from gendiff.gendiff import generate_diff
import os



FILE1_JSON_PATH = "tests/fixtures/file1.json"
FILE2_JSON_PATH = "tests/fixtures/file2.json"
FILE1_YAML_PATH = "tests/fixtures/file1.yaml"
FILE2_YAML_PATH = "tests/fixtures/file2.yaml"

RESULT_STYLISH_PATH = "tests/fixtures/result_stylish.txt"
RESULT_PLAIN_PATH = "tests/fixtures/result_plain.txt"


def test_geneate_diff_stylish():

  result_stylish = open(os.path.abspath(RESULT_STYLISH_PATH)).read()
  assert result_stylish == generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH)
  assert result_stylish == generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH)

def test_geneate_diff_plain():

  result_plain = open(os.path.abspath(RESULT_PLAIN_PATH)).read()
  assert result_plain == generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH, 'plain')
  assert result_plain == generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH, 'plain')



from gendiff.gendiff import generate_diff

FILE1_JSON_PATH = "tests/fixtures/file1.json"
FILE2_JSON_PATH = "tests/fixtures/file2.json"
RESULT = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

def test_geneate_diff():
    assert RESULT == generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH)
from pathlib import Path

ROOT_PATH = Path(__file__).parent

FILE_PATH = ROOT_PATH.joinpath('data', 'library.json')
TEST_FILE_PATH = ROOT_PATH.joinpath('tests', 'test_library.json')
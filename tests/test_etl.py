import os
import pytest


file_path = './data/hans.csv'


def test_file_exists():
    assert os.path.exists(file_path), f'O arquivo {file_path} não existe.'


def test_file_not_empty():
    assert os.path.getsize(file_path) > 0, f'O arquivo {file_path} está vazio.'


if __name__ == '__main__':
    pytest.main()

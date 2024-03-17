from tests.data.test_make_dataset import test_categories_to_ids

from .src.make_dataset import categories_to_ids

if __name__ == "__main__":
    test_categories_to_ids()
    print(categories_to_ids())

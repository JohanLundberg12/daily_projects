import pytest

from review_len_in_fibbonaci_sequence import (
    fibonacci_numbers,
    length_of_review_in_fibonacci_sequence,
    review_to_text,
)


@pytest.mark.parametrize(
    "review, is_fibonacci", [([1, 2, 3, 4, 5], True), ([1, 2, 3, 4, 5, 6], False)]
)
def test_fibonacci_sequence(review, is_fibonacci):
    assert length_of_review_in_fibonacci_sequence(review) == is_fibonacci


def test_review_43():
    from tensorflow.keras.datasets import imdb

    (X_train, _), _ = imdb.load_data(num_words=100, maxlen=100, seed=42)
    review_43 = X_train[43]

    assert length_of_review_in_fibonacci_sequence(review_43) == True


def test_all_fibbonaci_reviews():
    from tensorflow.keras.datasets import imdb

    (X_train, _), _ = imdb.load_data(num_words=100, maxlen=100, seed=42)
    fibbonaci_reviews = [
        review for review in X_train if length_of_review_in_fibonacci_sequence(review)
    ]

    assert len(fibbonaci_reviews) == 104


def test_review_43_to_text():
    from tensorflow.keras.datasets import imdb

    (X_train, _), _ = imdb.load_data(num_words=100, maxlen=100, seed=42)
    review_43 = X_train[43]

    assert (
        review_to_text(review_43)
        == """the by br and and and for was well and and and have and and and of and not like and make out and and and but and and and and and to and an and and and in also and or and but out is and my and of and and film and and"""
    )

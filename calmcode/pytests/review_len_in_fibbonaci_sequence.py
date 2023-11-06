from tensorflow.keras.datasets import imdb

(X_train, y_train), (X_test, y_test) = imdb.load_data(
    num_words=100, maxlen=100, seed=42
)

word_to_index = imdb.get_word_index()
index_to_word = {val: key for key, val in word_to_index.items()}


fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def length_of_review_in_fibonacci_sequence(review):
    return len(review) in fibonacci_numbers


def review_to_text(review):
    return " ".join([index_to_word[index] for index in review])

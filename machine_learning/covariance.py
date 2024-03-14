import numpy as np


def magnitude_of_vector(vector):
    sum_of_squares = sum(x**2 for x in vector)
    return np.sqrt(sum_of_squares)


def cosine_similarity(a, b):
    return np.dot(a, b) / (magnitude_of_vector(a) * magnitude_of_vector(b))


def projection_onto_unit_vector(vector, unit_vector):
    """
    This function calculates the projection of a vector onto a unit vector.

    Args:
        vector: A numpy array representing the vector to be projected.
        unit_vector: A numpy array representing the unit vector onto which to project.

    Returns:
        The projection of the vector onto the unit vector.
    """
    return np.dot(unit_vector, vector) * unit_vector


def covariance_matrix(data):
    """
    This function calculates the covariance matrix of a dataset.

    Args:
        data: A numpy array representing the dataset.

    Returns:
        The sample covariance matrix of the dataset.
        It is divided by the number of samples to normalize it to get
        an unbiased estimate of the population covariance matrix.
    """
    mean = np.mean(data, axis=0)
    centered_data = data - mean
    return np.dot(centered_data.T, centered_data) / len(data) - 1

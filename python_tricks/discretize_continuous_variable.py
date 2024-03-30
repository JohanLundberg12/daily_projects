import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import KBinsDiscretizer


def main():
    """
    This function demonstrates the benefits of discretizing a continuous variable and
    how to discretize a continuous variable and use it in a logistic regression model.
    """

    X, y = make_moons(n_samples=100, noise=0.2)
    model = LogisticRegression()
    lr_model = model.fit(X, y)

    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.show()

    # Create a mesh to plot in
    h = 0.02  # step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Predict the function value for the whole grid
    Z = lr_model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors="k")
    plt.show()

    # Create a new model with a binning strategy
    lr_model_dis = make_pipeline(
        KBinsDiscretizer(encode="onehot", n_bins=8),
        LogisticRegression(),
    )
    lr_model_dis = lr_model_dis.fit(X, y)

    Z = lr_model_dis.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors="k")
    plt.show()


if __name__ == "__main__":
    main()

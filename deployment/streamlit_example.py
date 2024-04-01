# import stream lit and numpy
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier

# function to generate a new set of random numbers


def _new_random_numbers(number_of_random_numbers):
    X = np.random.randint(1, 100, number_of_random_numbers)
    y = X - 1

    return X, y


# make the function lazy, i.e. if inputs are the same as before, no need to
# train and predict again
@st.cache_data
def _make_predictions(X, y, n_est):
    # create a decision tree classifier
    clf = DecisionTreeClassifier(max_depth=1)
    clf.fit(X, y)
    y1 = clf.predict(X)

    # create an adaboost regressor
    regr = AdaBoostRegressor(random_state=0, n_estimators=n_est)
    # fit the regressor to the data
    regr.fit(X, y)
    # make predictions
    y2 = regr.predict(X)
    return y1, y2


# create a title for the app
st.title("Streamlit Example")

# Slide for number of random numbers 1, 100
st.sidebar.markdown("## Controls")
st.sidebar.markdown("Change the number of random numbers to generate")
number_of_random_numbers = st.sidebar.slider("Number of random numbers", 1, 100)

n_est = st.sidebar.slider("Number of estimators", 1, 100)
scatter_plot_checkbox = st.sidebar.checkbox("Toggle Scatterplot")

generate_button = st.sidebar.button("Generate new random numbers")

# create a button to generate a new random number
if generate_button:
    random_numbers = _new_random_numbers(number_of_random_numbers)
else:
    random_numbers = None

# show the random numbers if they exist

if random_numbers:
    X, y = random_numbers
    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)

    if number_of_random_numbers < 10:
        st.write("The new random numbers are:", X)
    else:
        st.write("Too many numbers to show")

    # plot to show a histogram of the random numbers
    fig, ax = plt.subplots()
    ax.hist(X)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    st.line_chart(X)

    if scatter_plot_checkbox:
        # show code snippet
        y1, y2 = _make_predictions(X, y, n_est)

        x = np.linspace(0, 100, number_of_random_numbers)
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=0.1)
        plt.plot(x, y1, label="mod1")
        plt.plot(x, y2, label="mod2")
        plt.legend()
        st.pyplot(fig)

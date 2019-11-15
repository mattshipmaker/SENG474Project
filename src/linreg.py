import db
import numpy as np

np.set_printoptions(suppress=True)

def predict(X, weight):
    return np.dot(X, weight)

def cost_function(X, y, weight):
    n = len(y)
    predictions = predict(X, weight)
    sq_error = (predictions - y)**2
    return 1.0/(2*n) * sq_error.sum()
  

def update_weights(X, y, weight, learning_rate):
    n = len(X)
    predictions = predict(X, weight)
    error = y - predictions
  
    gradient = np.dot(-X.T, error)
    gradient /= n
    gradient *= learning_rate
    weight -= gradient
  
    return weight

def train(X, y, weight, learning_rate, iters):
    cost_history = []
  
    for i in range(iters):
        weight = update_weights(X,y,weight, learning_rate)
        cost = cost_function(X, y, weight)
        cost_history.append(cost)
      
    return weight, cost_history

def scale(X, x_min, x_max):
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom==0] = 1
    return x_min + nom/denom

def create_weights(n):
    return np.array([[0.0] for i in range(n)])


def main():
    
    year = db.get_year(2015)
    countries = db.get_countries()
    #labels: life expectancy for a year 

    Y = [] 
    X = []
   
    for c in countries:
        x = db.get_country_data_by_year(c[0], 2015)
        if len(x) != 0:
            X.append(list(x[0]))
            y = db.get_le_by_year_id(c[0], year[0])
            Y.append(list(y))

    Y = np.array(Y)
    X = np.array(X)

    X_scaled = scale(X, 0, 1)
    X_scaled = np.insert(X_scaled, 0, 1, axis=1)

    W = create_weights(len(X_scaled[1]))

    w, ch = train(X_scaled, Y, W, 0.01, 1000)

    #return w

if __name__ == "__main__":
    main()
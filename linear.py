import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(314159)

X = 10*rng.rand(50)

y = 2*X - 5 + rng.randn(50)

plt.scatter(X,y)

#plt.show()

model = LinearRegression(fit_intercept=True)

model.fit(X.reshape(50,1),y.reshape(50,1))

print("Pendiente (deberia ser 2): {}".format(model.coef_[0]))
print("Ordenada (debeeria ser 5): {}".format(model.intercept_))

y_prec = 1.94895102*X - 4.52401901
plt.plot(X,y_prec)
plt.show()
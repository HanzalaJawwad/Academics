import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

data = pd.read_csv('exp7&8_data.csv')

model = DiscreteBayesianNetwork([('Difficulty', 'Grade'), ('Intelligence', 'Grade')])
model.fit(data, estimator=MaximumLikelihoodEstimator)

inference = VariableElimination(model)

print("P(Grade):")
print(inference.query(variables=['Grade']))
print("\nP(Grade | Intelligence=High):")
print(inference.query(variables=['Grade'], evidence={'Intelligence': 'High'}))

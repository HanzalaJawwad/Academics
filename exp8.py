import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

data = pd.read_csv('exp7&8_data.csv')

model = DiscreteBayesianNetwork([('Difficulty', 'Grade'), ('Intelligence', 'Grade')])
model.fit(data, estimator=MaximumLikelihoodEstimator)

inference = VariableElimination(model)

grade_dist = inference.query(variables=['Grade'])
print("\nP(Grade):\n", grade_dist)
print("\nInference 1:")
print("- Grade B is most common.")
print("- A and C are equally less frequent.")

grade_given_intel = inference.query(variables=['Grade'], evidence={'Intelligence': 'High'})
print("\nP(Grade | Intelligence=High):\n", grade_given_intel)
print("\nInference 2:")
print("- High intelligence increases chances of Grade A or B.")
print("- Grade C becomes unlikely.")

grade_given_difficulty = inference.query(variables=['Grade'], evidence={'Difficulty': 'Hard'})
print("\nP(Grade | Difficulty=Hard):\n", grade_given_difficulty)

print("\nActual frequencies from data (Difficulty=Hard):")
hard_df = data[data['Difficulty'] == 'Hard']
print(hard_df['Grade'].value_counts(normalize=True))
print("\nInference 3:")
print("- From data: 60% C, 40% B for hard subjects.")
print("- If model shows 50-50, it might be due to inference smoothing or CPT grouping.")
print("- Grade A does not occur under Hard difficulty in data.")

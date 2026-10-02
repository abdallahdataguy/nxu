# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
cancer_data = load_breast_cancer()
X = cancer_data.data
y = cancer_data.target
features = cancer_data.feature_names

# Step 2: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: PCA Implementation
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Explained Variance
explained_variance = pca.explained_variance_ratio_
print(f'\nExplained variance by each component (PC1, PC2): {explained_variance}')
print(f'\nCumulative variance for the two components (PC1 + PC2): {round(sum(explained_variance), 3) * 100}%')

# Get the loadings (coefficients of the original features on the principal components)
loadings = pca.components_

# Convert to a DataFrame for easier interpretation
loadings_df = pd.DataFrame(loadings.T, columns=['PC1', 'PC2'], index=features)

# Sort the loadings by absolute values for the first two components
# to find the most important variables for each principal component
essential_variables_pc1 = loadings_df['PC1'].abs().sort_values(ascending=False).head()
essential_variables_pc2 = loadings_df['PC2'].abs().sort_values(ascending=False).head()

# Print the essential variables (Top 5) for each component
print(f'\nEssential variables for component 1:\n {essential_variables_pc1}')
print(f'\nEssential variables for component 2:\n {essential_variables_pc2}')

# Step 4(Bonus): Logistic Regression + visualization of PCA components
# A: Logistic Regression
# Splitting the data for logistic regression
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)
# Logistic regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
# Print classification accuracy
print(f'\nClassification Accuracy: {accuracy}')
# Print confusion matrix
print('\nConfusion Matrix:\n', confusion_matrix(y_test, y_pred))
# Print classification report
print('\nClassification Report:\n', classification_report(y_test, y_pred))

# B: Visualize PCA components
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA of Breast Cancer Dataset')
plt.show()

from utils.role_predictor import predict_role

resume_text = """
python sql power bi excel dashboards reporting
"""

predicted_role, top_roles = predict_role(
    resume_text
)

print("Predicted Role:")
print(predicted_role)

print("\nTop Predictions:")
print(top_roles)
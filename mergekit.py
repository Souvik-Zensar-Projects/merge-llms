import mergekit as mk

# Paths to the fine-tuned models (Ensure they are downloaded locally)
model_paths = {
    "mistral_7b": "./Mistral-7B-v0.1",
    "codellama_python": "./CodeLlama-7b-Python",
    "deepseek_v2": "./deepseek-llm-7b-v2",
    "starcoder2": "./starcoder2-7b",
    "mistral_large_2": "./Mixtral-8x7B"
}

# Merge Step 1: IT Support + Coding
it_code_model = mk.merge(
    models=[model_paths["mistral_7b"], model_paths["codellama_python"]],
    method="slerp",
    weights=[0.6, 0.4],  # Mistral 7B has stronger general IT knowledge
    save_path="merged_it_code_model"
)

# Merge Step 2: Security + Business Intelligence
security_bi_model = mk.merge(
    models=[model_paths["deepseek_v2"], model_paths["starcoder2"]],
    method="slerp",
    weights=[0.5, 0.5],  # Equal balance between security & BI
    save_path="merged_security_bi_model"
)

# Final Merge: Enterprise Model
final_enterprise_llm = mk.merge(
    models=["merged_it_code_model", "merged_security_bi_model", model_paths["mistral_large_2"]],
    method="slerp",
    weights=[0.35, 0.35, 0.3],  # Balanced across IT, coding, security & business intelligence
    save_path="final_enterprise_llm"
)

print("Enterprise LLM merged successfully! Model saved at 'final_enterprise_llm'")

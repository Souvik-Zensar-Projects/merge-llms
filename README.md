# merge-llms

---

## install git lfs
```bash
apt update && apt install git-lfs -y  # For Debian/Ubuntu
yum install git-lfs -y                # For RHEL/CentOS
git lfs install                       # Windows
```
---

## download open-source models
```bash
git clone https://huggingface.co/mistralai/Mistral-7B-v0.1
git clone https://huggingface.co/codellama/CodeLlama-7b-Python
git clone https://huggingface.co/deepseek-ai/deepseek-llm-7b-v2
git clone https://huggingface.co/bigcode/starcoder2-7b
git clone https://huggingface.co/mistralai/Mixtral-8x7B
```
---

## verify downloads
```bash
ls -lh
```
---

## model dirs
Mistral-7B-v0.1
CodeLlama-7b-Python
deepseek-llm-7b-v2
starcoder2-7b
Mixtral-8x7B

---

## model paths
model_paths = {
    "mistral_7b": "./Mistral-7B-v0.1",
    "codellama_python": "./CodeLlama-7b-Python",
    "deepseek_v2": "./deepseek-llm-7b-v2",
    "starcoder2": "./starcoder2-7b",
    "mistral_large_2": "./Mixtral-8x7B"
}

---

## run merging code
```bash
pip install mergekit
python mergekit.py
```
---
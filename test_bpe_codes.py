import subprocess
import os

# 定义函数来使用完整路径调用learn_bpe.py
def train_bpe(input_file, output_file, num_symbols):
    # 使用os.path.join确保路径正确处理
    learn_bpe_path = os.path.join("D:\Program Files\AI\subword-nmt\subword_nmt", "learn_bpe.py")
    # 构建命令
    command = [
        "python",
        learn_bpe_path,
        "--input", input_file,
        "--output", output_file,
        "--symbols", str(num_symbols)
    ]
    subprocess.run(command)

# 定义函数来使用完整路径调用apply_bpe.py
def apply_bpe(input_file, output_file, bpe_codes):
    # 使用os.path.join确保路径正确处理
    apply_bpe_path = os.path.join("D:\Program Files\AI\subword-nmt\subword_nmt", "apply_bpe.py")
    # 构建命令
    command = [
        "python",
        apply_bpe_path,
        "-c", bpe_codes,
        "--input", input_file,
        "--output", output_file
    ]
    subprocess.run(command)

# 合并输入文件的函数保持不变
def merge_files(file_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for fname in file_list:
            with open(fname, 'r', encoding='utf-8') as infile:
                for line in infile:
                    outfile.write(line)

# 使用你的文件路径
cs_file = 'D:\Program Files\AI\europarl-v7.cs-en.cs'
en_file = 'D:\Program Files\AI\europarl-v7.cs-en.en'
merged_file = 'D:\Program Files\AI\combined.txt'
# 使用os.path.join确保路径正确处理
bpe_codes = os.path.join("D:\Program Files\AI", "bpe_codes")
num_symbols = 30000

# 合并文件
merge_files([cs_file, en_file], merged_file)

# 训练BPE模型
train_bpe(merged_file, bpe_codes, num_symbols)

# 应用BPE模型
apply_bpe(cs_file, os.path.join("D:\Program Files\AI", "europarl-v7.bpe.cs"), bpe_codes)
apply_bpe(en_file, os.path.join("D:\Program Files\AI", "europarl-v7.bpe.en"), bpe_codes)
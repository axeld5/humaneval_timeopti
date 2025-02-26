import re

def extract_python_code(text):
    pattern = r"```python([\s\S]*?)```"
    matches = re.findall(pattern, text)
    if matches:
        return matches[0].strip()
    else:
        return text

def max_index_of_min_value(lst):
    min_val = float('inf')
    max_index = -1
    for i in range(len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
            max_index = i
        elif lst[i] == min_val:
            max_index = i
    return max_index

def get_all_split(answer):
    split_answer = answer.split('```python')
    intro = split_answer[0]
    split_split_answer = split_answer[1].split('```')
    python_code = split_split_answer[0]
    reasoning = split_split_answer[1]
    return intro, python_code, reasoning
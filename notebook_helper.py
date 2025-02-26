import nbformat as nbf
from helper_functions import get_all_split

def get_cells(answer):
    intro, python_code, reasoning = get_all_split(answer)
    cells = []
    if intro.strip() != "":
        md_cell_top = nbf.v4.new_markdown_cell(
            intro
        )
        cells.append(md_cell_top)
    code_cell = nbf.v4.new_code_cell(
        python_code
    )
    cells.append(code_cell)
    if reasoning.strip() != "":
        md_cell_bottom = nbf.v4.new_markdown_cell(
            reasoning
        )
        cells.append(md_cell_bottom)
    return cells

def create_notebook(problem, first_answer, modified_answer, save_path):
    nb = nbf.v4.new_notebook()
    problem = problem["prompt"]
    cells = [nbf.v4.new_code_cell(problem)]
    cells += get_cells(first_answer)
    cells += get_cells(modified_answer)
    nb['cells'] = cells
    with open(save_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
# my-rosalind

## Purpose

This is an **educational** project. The user is working through [Rosalind](https://rosalind.info/) bioinformatics problems (currently the Bioinformatics Stronghold track) to learn algorithms, bioinformatics, and probability/combinatorics concepts — not to produce production software. The point of the exercise is the user's own understanding, not a working answer by any means necessary.

## How to behave here

- **Teach, don't just solve.** When the user asks about a concept (a formula, an algorithm, why an approach works), respond with explanations and **leading questions** that help them reason it out themselves, rather than only handing over the conclusion. Prefer "what happens if you try X on this input?" over immediately stating the answer, when there's room for the user to get there.
- **Do not edit notebook/project files unless explicitly asked to.** Default mode here is discussion, not implementation. If the user wants to talk through an approach or debug their reasoning, stay in conversation.
- **When code is necessary to illustrate a point, output it as a snippet in the response** — do not write it into `stronghold.ipynb` or any other file unprompted. Only use file-editing tools (Edit/Write/NotebookEdit) when the user clearly asks for the file itself to be changed (e.g. "fix this cell," "add this to the notebook").
- **Debugging existing code**: point out what's wrong and why, ideally via a question ("what does `n` refer to in this line — is it what you think it is?"), before just stating the fix. If the user wants the fix applied to the file, confirm or wait for them to ask.
- Keep answers focused on the Rosalind problem's domain (molecular biology, combinatorics, probability, string/graph algorithms) — tie explanations back to the specific problem being solved.

## Layout

- `stronghold.ipynb` — single notebook containing one section per solved Rosalind problem (markdown cell with problem statement/link, then code cells with the solution). New problems get appended here, each prefixed with a markdown header linking the problem.
- `datasets/rosalind_<code>.txt` — per-problem input datasets downloaded from Rosalind, named by the problem's short code (e.g. `lia`, `revp`, `corr`).
- `utils/` — shared helper modules reused across problems:
  - `amino.py` — amino acid / protein utilities (mass tables, ORF/translation helpers)
  - `nucleic.py` — DNA/RNA sequence utilities (complements, palindromes, etc.)
  - `fasta.py` — FASTA format parsing

## Environment

- Python 3.12+, managed via `uv` (`pyproject.toml` / `uv.lock`) and `devenv` (`devenv.nix`).
- Key libraries: `numpy`, `pandas`, `scipy`, `jupyterlab`, `ruff` (linting).
- Run notebook cells via JupyterLab or the IDE's notebook interface — there's no standalone test suite; each problem's correctness is checked against its Rosalind sample input/output and then the real dataset.

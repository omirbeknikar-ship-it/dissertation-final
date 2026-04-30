# Render Instructions

Quarto PDF rendering was attempted with:

```bash
quarto render Paper/final_paper.md --to pdf
```

The render failed because the `quarto` executable is not installed or not available on `PATH`:

```text
zsh:1: command not found: quarto
```

To render the paper:

1. Install Quarto from https://quarto.org/docs/get-started/.
2. Install a LaTeX distribution if Quarto reports a missing PDF engine, for example TinyTeX:

```bash
quarto install tinytex
```

3. From the repository root, rerun:

```bash
quarto render Paper/final_paper.md --to pdf
```

The markdown draft remains available at `Paper/final_paper.md`.

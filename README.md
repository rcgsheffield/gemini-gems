# Gemini Gems for Research

A version-controlled repository of custom **Google Gemini Gems** designed for the entire research lifecycle including literature synthesis, paper editing, and data analysis. 

> [!WARNING]
> This is a prototype experimental repository — **do not use** for research purposes.

This repository serves as the single source of truth for our research group's custom AI assistants, prompt instructions, and reference knowledge bases.

## Documentation

- University of Sheffield [Google Gemini and Gemini Notebooks](https://students.sheffield.ac.uk/it-services/google/google-gemini-and-google-notebooklm)
- Google [Get started with Gems in Gemini Apps](https://support.google.com/gemini/answer/15236321?hl=en)

## Repository Structure

The repository is organized by individual Gem workflows. Each folder contains the system prompts (`instructions.md`) and external links to heavier assets (like full-text PDFs or datasets).

```text
.
├── README.md
└── gems/
    ├── literature-synthesizer/
    │   ├── README.md                 # Prompt instructions & metadata
    │   └── instructions.md           # Drive/arXiv links to target papers
    │
    ├── latex-formatter/
    │   ├── README.md
    │   ├── instructions.md
    │   └── knowledge/
    │       └── math-notation-guide.md
    │
    └── peer-reviewer/
        ├── README.md
        ├── instructions.md
        └── knowledge/
            └── review-rubric.md
```

## Support

Please contact [Research & Innovation IT](https://students.sheffield.ac.uk/it-services/research).

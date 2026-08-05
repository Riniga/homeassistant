# Documentation Standard

## Language

* All project documentation is written in English.
* File and folder names use English and `kebab-case`.
* Business data or externally supplied content may remain in its original language when appropriate.

## Format

* All documentation uses Markdown (`.md`).
* Use clear headings and short sections.
* Prefer bullet lists and tables over long paragraphs.
* Keep formatting consistent throughout the repository.

## File and Folder Naming

```text
kebab-case-file-name.md
kebab-case-folder-name/
```

## Length and Tone

* Keep documentation concise, practical, and easy to scan.
* Write for someone who needs to understand the project quickly.
* Prefer examples over lengthy explanations.
* Remove obsolete information instead of adding disclaimers.

## Purpose

Documentation explains:

* Why something exists.
* What it does.
* When it should be used.
* Any important assumptions or constraints.

Source code explains **how** something is implemented.

Avoid repeating information that is already obvious from the implementation.

## Single Source of Truth

Each topic should have exactly one authoritative document.

Avoid duplicating information across multiple documents. Instead, reference the appropriate document.

If implementation and documentation disagree, update one of them immediately.

## When to Update Documentation

Documentation changes are part of the implementation and should be included in the same pull request.

Documentation should be updated whenever changes affect:

* Architecture
* Repository structure
* Development workflow
* Standards or conventions
* Dependencies
* Configuration
* Deployment
* User-visible functionality
* Operational procedures

## What Not to Document

Do not document:

* Implementation details that are obvious from the code.
* Temporary experiments or throwaway work.
* Information that quickly becomes outdated.
* Duplicate information maintained elsewhere.

## Document Quality

Good documentation should be:

* Accurate
* Current
* Actionable
* Easy to navigate
* Easy to maintain

Delete outdated documentation rather than allowing conflicting information to accumulate.

## Document Types

| Type                | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| Architecture        | System structure and major design decisions                  |
| ADR                 | Significant architectural or technical decisions             |
| Vision              | Long-term goals and guiding principles                       |
| Roadmap             | Planned future work                                          |
| MVP                 | Scope for each delivery increment                            |
| Implementation Plan | Step-by-step implementation guidance                         |
| Development         | Development environment and workflows                        |
| Standards           | Coding, Git, testing, documentation, and project conventions |
| Operations          | Deployment, maintenance, backup, and recovery procedures     |

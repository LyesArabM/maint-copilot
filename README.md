# Predictive Maintenance Copilot

Predictive-maintenance MLOps project for the SE4AI lab. The project will use
GitHub for source code and CI, and DagsHub for DVC data versioning and MLflow
experiments.

The dataset and maintenance documents are synthetic. The classifier owns the
failure probability and risk level; the future RAG assistant will only explain
those results using cited maintenance procedures.

## Team branches

- `rayan/data-model-pipeline` - dataset validation, DVC pipeline, features,
  training, and evaluation
- `ali/api-rag` - API, MCP server, and RAG integration
- `main` - reviewed and integrated code

Use short-lived branches and pull requests. Do not commit datasets, model
artifacts, tokens, or `.env` files.

## First setup

Install Python 3.11, `uv`, and Git. From the repository root:

```powershell
uv sync
```

Create a DagsHub access token and configure it only in your local environment:

```powershell
$env:DAGSHUB_TOKEN = "your-token"
```

The exact DVC remote URL must be copied from **DagsHub > Remote > Data > DVC**.
The token must never be committed to Git.

## Rayen's first milestone

On `rayan/data-model-pipeline`, complete the following in order:

1. Obtain the AI4I 2020 Predictive Maintenance CSV from the approved source.
2. Store it under `data/raw/ai4i2020.csv`.
3. Run `dvc init` and configure the DagsHub DVC remote.
4. Track the CSV with `dvc add data/raw/ai4i2020.csv`.
5. Add validation, train/test splitting, feature engineering, training, and
   evaluation stages to `dvc.yaml`.
6. Make `dvc repro` produce reproducible outputs and reports.
7. Add tests for schema validation, splitting, training, and evaluation.
8. Open a pull request into `main`.

The first acceptance check is:

```powershell
dvc repro
pytest
```

Do not start the RAG or cloud deployment until this reproducible model
pipeline is working.

## Phase 0 foundation checks

The repository foundation can be checked locally with:

```powershell
uv sync --frozen
uv run ruff check .
uv run ruff format --check .
uv run pytest -q
```

The dataset is intentionally excluded from Git and must be tracked with DVC.
After obtaining the team-approved DagsHub DVC remote URL, configure it locally
without committing credentials:

```powershell
dvc remote add -d dagshub <DAGSHUB_DVC_REMOTE_URL>
dvc add data/raw/ai4i2020.csv
dvc push
```

The remote configuration is stored in `.dvc/config.local` when credentials are
needed; that file is ignored by Git.

# Known Issues

- **Vercel rejects `pyproject.toml` without a `[project]` table.** During the build Vercel executes `uv lock` and fails with `No 'project' table found in: pyproject.toml` unless that table already exists.

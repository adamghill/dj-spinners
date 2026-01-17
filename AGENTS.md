# AGENTS guide for dj-spinners

This document helps AI/code assistants contribute safely and effectively to `dj-spinners`.

## Project overview
- **Purpose:** Inline SVG loading spinners for Django templates.
- **Primary API:** Django template tag `{% spinner "name" %}`.
- **Assets:** SVG files under `src/dj_spinners/assets/svg/`.

## Repo layout
- `src/dj_spinners/`
  - `apps.py`: Django `AppConfig` (`DjSpinnersConfig`).
  - `templatetags/spinners.py`: `{% spinner %}` tag implementation.
  - `assets/svg/*.svg`: Spinner definitions.
- `README.md`: Quick start and examples.
- `pyproject.toml`: Build, lint, test config.
- `AGENTS.md`: You are here.

## Development guidelines
- **Scope small, PRs small.** Prefer focused, minimal diffs.
- **No silent breaking changes.** Preserve the `{% spinner %}` contract.
- **Follow lint/format rules.** See `[tool.ruff]` and `ty` settings in `pyproject.toml`.
- **No inline import reordering beyond top-level.** Keep imports at file top.
- **Do not add or delete comments/docs unless requested.** Maintainers prefer explicit requests for docs changes.

## Template tag contract (`templatetags/spinners.py`)
- Tag: `{% spinner "<name>" %}` renders inline SVG.
- Name validation: `[a-z0-9._-]`, optional `.svg` suffix allowed.
- Loading order:
  1. `importlib.resources.files("dj_spinners")/assets/svg/<name>.svg`
  2. Filesystem fallback for dev: `src/dj_spinners/assets/svg/<name>.svg`
- Caching: `functools.lru_cache` for file contents.
- Security: Returns `mark_safe(svg)`; only from curated asset directory after validation.
- Do not introduce network or template context side effects.

## Assets and packaging
- Ensure all SVGs in `src/dj_spinners/assets/svg/` are included in built artifacts.
- If packaging excludes assets, update build configuration accordingly (e.g., `uv_build` include paths) and verify via a local build and install.
- Keep SVGs optimized and readable; avoid huge files. Prefer consistent attribute patterns where possible.

## Testing
- Commands:
  - Install: `uv install && pip install -e .[dev]`
  - Tests: `just test`
- Add tests for:
  - Valid/invalid spinner names.
  - Missing file errors.
  - Cache hit path (optional via instrumentation or count reads).
  - Basic render in a template context.

## Release hygiene
- Update `CHANGELOG.md` in Keep a Changelog style.
- Bump version in `pyproject.toml`.
- Verify wheels include SVG assets.

## Contribution workflow
- Branch naming: `feat/...`, `fix/...`, `chore/...`.
- Keep commits logical and message clear.
- Include before/after notes for behavior changes.

## Do / Don’t checklist
- **Do**: Preserve `{% spinner %}` API and validation rules.
- **Do**: Keep imports at the top of modules.
- **Do**: Add tests for new behaviors.
- **Don’t**: Add runtime dependencies without discussion.
- **Don’t**: Change asset loading paths without updating docs/tests.
- **Don’t**: Embed remote content or fetch over network at render time.

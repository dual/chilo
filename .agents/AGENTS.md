# Chilo Agent Guide

This document summarizes the conventions every AI agent must follow when configuring or editing apps that use **Chilo**. Reference this before generating code, scaffolding handlers, or modifying configuration.

## 1. Router Setup

1. **Always configure `Chilo()` in a dedicated module (e.g., `api/main.py`).** Minimum keys:
   - `base_path` (string, typically `/`).
   - `handlers` (glob/directory to your handler files, e.g., `api/handlers`).
2. Optional but common flags:
   - `cors`, `host`, `port`, `reload`, `verbose`.
   - `before_all`, `after_all`, `when_auth_required`, `on_error`, `on_timeout` for cross-cutting logic.
   - `openapi` (path to `openapi.yml`) if request/response validation is desired.
   - `openapi_validate_request` / `openapi_validate_response` (only enable when `openapi` exists).
3. Remember: Chilo maps directories → routes automatically. Dynamic segments are prefixed with `_` in file names (e.g., `handlers/user/_user_id.py` → `/user/{user_id}`). No manual route decorators are needed.

## 2. Handlers & Requirements

1. Each handler file exposes one function per HTTP method (`get`, `post`, `put`, `patch`, `delete`, etc.). The router matches by method name.
2. Use the `@requirements(...)` decorator from `chilo_api` to declare validation and middleware hooks. Key arguments:
   - `required_headers`, `available_headers`.
   - `required_query`, `available_query`.
   - `required_route` (mandatory when using dynamic `_param` files).
   - `required_body` / `required_response` (schema references or inline JSON schema dicts).
   - `auth_required`, `timeout`, `before`, `after`, `request_class`, `summary`, `deprecated`, and any custom keys.
3. Requirements are enforced even without OpenAPI validation (as long as `openapi_validate_request` is `False`). When OpenAPI validation is enabled, ensure the referenced schemas exist.

## 3. Request & Response Objects

Chilo injects strongly-typed helpers into every handler.

### Request (`request` argument)
- Read-only properties for `method`, `headers`, `query_params`, `path_params`, `route`, `path`, `content_type`, `host_url`, etc.
- Convenience accessors: `.json`, `.form`, `.xml`, `.graphql`, `.body`, `.raw`.
- `request.context` is the only mutable attribute—use it to pass data between middleware and handlers.

### Response (`response` argument)
- Set `response.code`, `response.body`, or `response.raw` (body auto-serializes to JSON when possible).
- Append headers via tuple assignment (e.g., `response.headers = ('x-request-id', 'abc')`).
- Use `response.set_error(key_path, message)` to accumulate validation/business errors; inspect `response.has_error` before sending success bodies.
- `response.compress = True` if compression is required.

## 4. OpenAPI Workflow

1. Generate specs from code via the CLI:
   ```bash
   python -m chilo_api generate-openapi --api=api.main --output=docs --format=yml,json --delete
   ```
   - `--handlers`: optional override for handler glob.
   - `--output`: directory for emitted `openapi.yml` / `.json`.
   - `--format`: comma-delimited list of `yml`, `json`.
   - `--delete`: remove paths/methods not present in code.
2. When `openapi_validate_request` is enabled, Chilo validates incoming payloads against the generated spec. Ensure schemas referenced in `required_body` / `required_response` live in `components.schemas`.

## 5. Logging

- Import via `from chilo_api import logger, log`.
- Use `logger.log(level='INFO', log=...)` for ad-hoc messages.
- Decorate functions with `@log(level='INFO', condition=callable)` to auto-log inputs/outputs when conditions match.

## 6. Implementation Checklist for Agents

1. **Router**: confirm `Chilo()` is instantiated once and exported (e.g., `api` module). Don’t hardcode routes elsewhere.
2. **Handlers**: obey directory-based routing conventions; create `_param.py` files for dynamic segments. Ensure each HTTP method is lowercase.
3. **Validation**:
   - Use `@requirements` for headers/query/body rules even if no OpenAPI file exists.
   - If OpenAPI validation is enabled, make sure `openapi` path is correct and schemas exist.
4. **CLI Usage**: prefer `python -m chilo_api serve --api=<module>` for development servers; avoid inventing custom runners.
5. **Middleware**: pass shared logic via router callbacks (`before_all`, `after_all`, etc.) or per-endpoint `before`/`after` requirements.
6. **Responses**: always set `response.body` or `response.set_error`; do not return raw dicts/tuples from handlers.
7. **Docs**: update `openapi.yml` via the CLI when handler requirements change.

Following this guide ensures AI-generated changes stay aligned with Chilo’s conventions and keeps auto-routing, validation, and tooling working as intended.

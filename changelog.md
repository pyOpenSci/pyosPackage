# Change Log

## Unreleased

## v0.4

This release fixes many issues with the original template run in "full mode"

* Fix: release.yml broken and combine publish and release builds (@lwasser, #71)
* Add: fix ci, linting, docs and tests run docs separately (@lwasser)
* Fix readthedocs build issues fixed by updating .readthedocs.yaml to install docs dependencies and build docs directly & redundant api docs (@lwasser)
* Add: Move to optional-dependency groups and call those groups in hatch envs (@lwasser)

## 0.1.12

* Add: CI based pypi release workflow & dynamic versioning (@lwasser, #32)
* Add: readthedocs config for building documentation (@lwasser)
* Add: Cleanup documentation structure (@lwasser)

## 0.1.11

* Fix: Drop support for python 3.9, add for 3.12 (@lwasser, #15)
* Add: Code of conduct to repo following contributors covenant (@lwasser, #17)
* Add: Linting & code format using ruff / precommit (@lwasser, #19)

## 0.1.10

* Initial publish to PyPI & Conda forge

## 0.1.9

* Use Hatch

## 0.1.8

* Fix: License should be MIT throughout

## 0.1.7

* Fix: Python version should be >3.9

## 0.1.6

* Fix: Add `readme` and `pyproject.toml` file

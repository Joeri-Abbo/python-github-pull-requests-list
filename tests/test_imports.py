"""Basic import and sanity tests."""


def test_yaml_import():
    import yaml
    assert yaml is not None


def test_github_import():
    from github import Github
    assert Github is not None


def test_requirements_parseable():
    """Verify requirements.txt exists and is non-empty."""
    import os
    req_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
    with open(req_path) as f:
        content = f.read()
    assert len(content.strip()) > 0

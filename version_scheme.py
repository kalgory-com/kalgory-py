from setuptools_scm.version import get_local_node_and_date


def custom_version_scheme(version):
    if version.exact:
        return version.format_with("{version}")
    else:
        return version.format_next_version("{version}.rc{distance}")


def custom_local_scheme(version):
    from os import getenv

    if version.exact:
        return ""
    elif getenv("GITHUB_REF") and "refs/pull/" in getenv("GITHUB_REF"):
        pr_number = getenv("GITHUB_REF").split("/")[2]
        return f"pr{pr_number}"
    elif getenv("GITHUB_SHA"):
        return getenv("GITHUB_SHA")[:7]
    else:
        return get_local_node_and_date(version)

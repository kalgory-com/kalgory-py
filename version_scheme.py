from setuptools_scm.version import get_local_node_and_date


def custom_version_scheme(version):
    return version.format_with("{tag}")


def custom_local_scheme(version):
    from os import getenv

    if version.exact:
        return ""
    elif getenv("GITHUB_REF") and "refs/pull/" in getenv("GITHUB_REF"):
        pr_number = getenv("GITHUB_REF").split("/")[2]
        return f"+pr{pr_number}"
    elif getenv("GITHUB_SHA"):
        sha_num = getenv("GITHUB_SHA")[:8]
        return f"+{sha_num}"
    else:
        return ""

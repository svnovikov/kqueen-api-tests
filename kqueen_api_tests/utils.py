import os


def get_abspath(base_dir, rel_path):
    return os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(base_dir)), rel_path)
    )

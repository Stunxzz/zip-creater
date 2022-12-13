import zipfile
import pathlib


def make_archive(file_paths, destination_folder, archive_name):
    dest_path = pathlib.Path(destination_folder, f"{archive_name}.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in file_paths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


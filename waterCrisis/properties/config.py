# -*- coding: utf-8 -*-
"""Configuration file for the properties module."""
import os


def _get_file_paths():
    """Build and return configured paths for reading and writing files.

    @return: Tuple of path to var directory, path to metadata CSV file
        and path to HTML out directory.
    """
    var_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "var"))

    metadata_csv_path = os.path.join(var_path, "property_data.csv")
    assert os.access(var_path, os.R_OK), \
        "Unable to read path to CSV input: {}".format(var_path)

    html_out_dir = os.path.join(var_path, "unprocessed_html")
    assert os.access(html_out_dir, os.W_OK), \
        "Unable to write to HTML out dir: {}".format(html_out_dir)

    return var_path, metadata_csv_path, html_out_dir


VAR_PATH, METADATA_CSV_PATH, HTML_OUT_DIR = _get_file_paths()

HOST_DOMAIN = "https://www.property24.com"
PROVINCE_PATHS = {
    'western-cape': "/property-values/western-cape/9",
    'gauteng': "/property-values/gauteng/1"
}

# Number of seconds to wait for response before aborting.
REQUEST_TIMEOUT = 5
# Fake a browser visit to avoid getting blocked as a scraper.
REQUEST_HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;"
              "q=0.9,image/webp,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
# Number of seconds to wait between requests to avoid being blocked.
REQUEST_SPACING = 0.5

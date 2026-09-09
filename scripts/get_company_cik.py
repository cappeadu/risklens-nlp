from pathlib import Path

import pandas as pd


def download_company_cik(file_name: str = "company_ciks", sample: int | None = None):
    """Download company CIK for S&P 500 companies as .txt file.

    Args:
        file_name (str, optional): File name for CIKs. Defaults to "company_ciks".
        sample (int | None, optional): If chosen, select a sample of CIKs. Defaults to None.
    """
    sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    companies_df = pd.read_html(
        sp500_url, storage_options={"User-Agent": "Mozilla/5.0"}
    )[0]
    companies_df = companies_df.sample(sample) if sample else companies_df
    path_to_save = Path(__file__).resolve().parent.parent / f"data/{file_name}.txt"

    try:
        with open(path_to_save, "w") as f:
            ciks_str = [f"{cik!s}\n" for cik in companies_df.CIK]
            f.writelines(ciks_str)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    download_company_cik(sample=5)

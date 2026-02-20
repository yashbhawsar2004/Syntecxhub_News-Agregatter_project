def export_to_csv(articles, filename="news.csv"):
    import csv

    if not articles:
        print("No data to export.")
        return

    keys = articles[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(articles)

    print("Exported to CSV successfully")


def export_to_excel(articles, filename="news.xlsx"):
    import pandas as pd

    if not articles:
        print("No data to export.")
        return

    df = pd.DataFrame(articles)
    df.to_excel(filename, index=False)

    print("Exported to Excel successfully")
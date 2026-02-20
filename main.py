import argparse
from fetcher import fetch_from_newsapi, fetch_from_bbc
from filters import filter_by_keyword, filter_by_source, filter_by_date
from storage import save_to_json, save_to_sqlite
from exporter import export_to_csv, export_to_excel
from deduplicator import remove_duplicates


def main():
    parser = argparse.ArgumentParser(description="News Aggregator CLI")

    parser.add_argument("--fetch", action="store_true", help="Fetch news")
    parser.add_argument("--source", type=str, help="Filter by source")
    parser.add_argument("--keyword", type=str, help="Filter by keyword")
    parser.add_argument("--date", type=str, help="Filter by date (YYYY-MM-DD)")
    parser.add_argument("--export", type=str, choices=["csv", "excel"])
    parser.add_argument("--storage", type=str, choices=["json", "sqlite"])

    args = parser.parse_args()

    articles = []

    if args.fetch:
        print("Fetching news...")
        articles.extend(fetch_from_newsapi())
        articles.extend(fetch_from_bbc())

    articles = remove_duplicates(articles)
    articles = filter_by_source(articles, args.source)
    articles = filter_by_keyword(articles, args.keyword)
    articles = filter_by_date(articles, args.date)

    if args.storage == "json":
        save_to_json(articles)
        print("Saved to JSON")

    elif args.storage == "sqlite":
        save_to_sqlite(articles)
        print("Saved to SQLite")

    if args.export == "csv":
        export_to_csv(articles)
        print("Exported to CSV")

    elif args.export == "excel":
        export_to_excel(articles)
        print("Exported to Excel")

    print(f"\nTotal Articles: {len(articles)}")


if __name__ == "__main__":
    main()
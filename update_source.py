#!/usr/bin/env python3

import json
import argparse
from pathlib import Path

SOURCE_FILE = Path(__file__).parent / "source.json"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--size", required=True, type=int)
    parser.add_argument("--description", default="Auto update")
    args = parser.parse_args()

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    app = data["apps"][0]

    new_version_entry = {
        "version": args.version,
        "date": args.date,
        "downloadURL": args.url,
        "size": args.size,
        "localizedDescription": args.description,
    }
  
    app["versions"] = [
        v for v in app.get("versions", []) if v["version"] != args.version
    ]
    app["versions"].insert(0, new_version_entry)

    app["version"] = args.version
    app["versionDate"] = args.date
    app["downloadURL"] = args.url
    app["size"] = args.size

    with open(SOURCE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"source.json updated to version {args.version}")


if __name__ == "__main__":
    main()

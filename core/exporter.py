# core/exporter.py

import json
from datetime import datetime


def export_payloads(payloads, export_type):
    """
    Export payloads to:
    - json
    - txt
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if export_type == "json":
        filename = f"payload_export_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(payloads, f, indent=4)

        print(f"\n✔ Payloads exported successfully to {filename}")

    elif export_type == "txt":
        filename = f"payload_export_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            for payload in payloads:
                f.write("=====================================\n")
                for key, value in payload.items():
                    f.write(f"{key}: {value}\n")
                f.write("\n")

        print(f"\n✔ Payloads exported successfully to {filename}")

    else:
        print("Unsupported export format.")


import argparse
from modules.xss import generate_xss
from modules.sqli import generate_sqli
from modules.command_injection import generate_cmd
from core.encoder import apply_encoding
from core.obfuscator import apply_obfuscation
from core.waf_notes import attach_waf_notes
from core.exporter import export_payloads


def print_banner():
    print("\n=== PayloadForge ===")
    print("Educational Payload Generation Framework")
    print("Aligned with OWASP ethical guidelines\n")


def main():
    parser = argparse.ArgumentParser(description="PayloadForge - Educational Payload Generator")

    parser.add_argument("--module", choices=["xss", "sqli", "cmd"], required=True)
    parser.add_argument("--context", choices=["html", "attribute", "js"])
    parser.add_argument("--xss-type", choices=["reflected", "stored", "dom"])
    parser.add_argument("--db", choices=["mysql", "postgresql", "mssql"])
    parser.add_argument("--sqli-type", choices=["error", "union", "blind"])
    parser.add_argument("--os", choices=["linux", "windows"])
    parser.add_argument("--encode", choices=["url", "base64", "hex"])
    parser.add_argument("--obfuscate", choices=["comment", "whitespace", "mixed"])
    parser.add_argument("--export", choices=["json", "txt"])

    args = parser.parse_args()

    print_banner()

    # Generate payloads
    if args.module == "xss":
        payloads = generate_xss(context=args.context, xss_type=args.xss_type)

    elif args.module == "sqli":
        payloads = generate_sqli(db_type=args.db, injection_type=args.sqli_type)

    elif args.module == "cmd":
        payloads = generate_cmd(os_type=args.os)

    else:
        print("Invalid module selected.")
        return

    # Apply obfuscation if selected
    if args.obfuscate:
        payloads = apply_obfuscation(payloads, args.obfuscate)

    # Apply encoding if selected
    if args.encode:
        payloads = apply_encoding(payloads, args.encode)

    # Attach WAF notes
    payloads = attach_waf_notes(payloads)

    # Export or print
    if args.export:
        export_payloads(payloads, args.export)
    else:
        for p in payloads:
            print("\n-----------------------------------")
            for key, value in p.items():
                print(f"{key}: {value}")


if __name__ == "__main__":
    main()

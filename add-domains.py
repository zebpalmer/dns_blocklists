#!/usr/bin/env python3
import argparse
from datetime import datetime


def get_header(target):
    header = []
    with open(target) as t:
        for line in t.readlines():
            if line.startswith("#"):
                if "STATS:" not in line:
                    header.append(line.strip("\n").strip())
            else:
                break
    return header


def get_domains(filename):
    domains = set()
    with open(filename) as f:
        for line in f.readlines():
            if not line.startswith("#"):
                domains.add(line.split("#")[0].strip("\n").strip())
    return domains


def combine(header, existing, new, whitelisted=None):
    output = []
    domains = existing | new
    if whitelisted:
        full_count = len(domains)
        domains = domains - whitelisted
        excluded_count = full_count - len(domains)
        print(f"{excluded_count} domains were excluded by whitelist")
    stats = f"# STATS: Total {len(domains)}, Diff {len(domains) - len(existing)}, TS {datetime.utcnow()}"
    for line in header:
        output.append(line)
    output.append(stats)
    for domain in sorted(domains):
        output.append(domain)
    return output


def write_file(filename, output):
    with open(filename, "w") as wf:
        for line in output:
            wf.write(line + "\n")


def run(source, target, whitelist=None, dryrun=False):
    header = get_header(target)
    new = get_domains(source)
    existing = get_domains(target)
    if whitelist:
        whitelisted = get_domains(whitelist)
    output = combine(header, existing, new, whitelisted=whitelisted)
    if not dryrun:
        write_file(target, output)
    else:
        for line in output:
            print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="add domains from source to target, sorted output"
    )
    parser.add_argument(
        "source", type=str, help="Source file with the domains you want to add"
    )
    parser.add_argument(
        "target",
        type=str,
        help="existing block/white list, source domains will be added to this file",
    )
    parser.add_argument(
        "--dryrun",
        type=bool,
        default=False,
        dest="dryrun",
        help="print result instead of writing file",
    )
    parser.add_argument(
        "--whitelist",
        type=str,
        default=None,
        dest="whitelist",
        help="domains in whitelist will be removed from output",
    )
    args = parser.parse_args()
    run(args.source, args.target, whitelist=args.whitelist, dryrun=args.dryrun)

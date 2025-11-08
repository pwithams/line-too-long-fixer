from ruff_e501_patch import cli
import sys

def run():
    if len(sys.argv) != 2:
        print("Usage: ltlf [source]")
        sys.exit(1)
    source = sys.argv[1]
    cli.run(["check", source, "--fix", "--select", "E501", "--unsafe-fixes"])

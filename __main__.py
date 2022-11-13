import argparse, sys
from validate import run_validator

EXAMPLES = """
examples:
  Current folder, ban . and .., with 3 layers: ui, core, data, max slash 1
    basic-lint . -b . -b .. -l ui -l core -l data -s 1
"""
parser = argparse.ArgumentParser(
    prog = "typescript-layers",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description = "Common TS import/export validator for piston projects",
    epilog = EXAMPLES)

parser.add_argument(
    "input",
    help="File or root directory to lint")
parser.add_argument(
    "-b",
    "--ban",
    metavar="BANNED_IMPORT",
    action="append",
    help="Ban import (matched exactly) ")
parser.add_argument(
    "-l",
    "--layer",
    metavar="LAYER",
    action="append",
    help="Add a layer (previous layers can depend on new layers)")
parser.add_argument(
    "-s",
    "--max-slash",
    metavar="NUMBER",
    type=int,
    action="store",
    default=1,
    help="Maximum number of slashes allowed")

args = parser.parse_args()

options = {
    "banned": args.ban,
    "layers": args.layer,
    "max_slashes": args.max_slash
}

sys.exit(run_validator(args.input, options))
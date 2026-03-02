from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from identify import identify


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='identify')
    # https://stackoverflow.com/a/8521644/812183
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {identify.__version__}')
    parser.add_argument(
        '--filename-only', action='store_true', help="Generate tags purely from the filename string passed in, avoiding any disk interaction.
    )
    parser.add_argument('path', help="The path to the file on disk to identify or a string representing a potential file name.")
    args = parser.parse_args(argv)

    if args.filename_only:
        func = identify.tags_from_filename
    else:
        func = identify.tags_from_path

    try:
        tags = sorted(func(args.path))
    except ValueError as e:
        print(e)
        return 1

    if not tags:
        return 1
    else:
        print(json.dumps(tags))
        return 0


if __name__ == '__main__':
    raise SystemExit(main())

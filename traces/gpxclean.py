# -*- coding: utf-8 -*-

from pathlib import Path

from majordome.cartography import GpxManager
from majordome.cartography import display_track

# TODO refactor this to automate conversion from sources to output; use
# path globbing + with_suffix to perform the conversions of names.

# if __name__ == "__main__":
#     gpx_mgnr = GpxManager.from_file("track-orig.gpx")
#     gpx_mngr = gpx_mgnr.sanitize(dump="track-sanitized.gpx")

#     track_map = display_track(gpx_mngr, colored=True, vmin=750, vmax=1000)
#     track_map.save("track.html")


# def process_dump(fname: str) -> None:
#     gpx_mgnr = GpxManager.from_file(f"{fname}.gpx")
#     gpx_mngr = gpx_mgnr.sanitize(dump=f"{fname}-sanitized.gpx")

#     track_map = display_track(gpx_mngr, colored=True, vmin=750, vmax=1000)
#     track_map.save(f"{fname}.html")
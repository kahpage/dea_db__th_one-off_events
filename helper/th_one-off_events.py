# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = "maikomitouhousai"  # ==== まいこみ東方祭 ====
    if i not in disabled_events:
        event_name = f"{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "maikomitouhousai_20100711073143_top201001271.jpg",
                [
                    Source(
                        "http://web.archive.org/web/20100711073143fw_/http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="イラスト：伽藍快 【ENJOY MIX】",
            ),
            Medium(
                "maikomitouhousai_20100711073143_top007.gif",
                [
                    Source(
                        "http://web.archive.org/web/20100711073143fw_/http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.3139509, 136.2813635),
                address="2 Chome-137 Shimotara, Maibara, Shiga 521-0016, Japan",
                description="滋賀県立文化産業交流会館　大ホール",
                sources=[
                    Source(
                        "http://web.archive.org/web/20100908094512fw_/http://www.taiga-s.co.jp/rhs/maicomi/009.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9SwxYrFGS9nGVCprunaMscMx9TTm6u1Dgou4lK86jbBwxgHWZUtu_q8BrPkX0fzBm4t1VRZ9l_XsZE42qJDnr2lQm11Qgtkqc1jAvhjy211oQ9VTqP9FSrv4OqtuZSu1j39rSdr=s0?imgmax=0",
                url="https://maps.app.goo.gl/eTo8g8LyekY7ibgu6",
            ),
        ]
        event = Event(
            links=["http://www.taiga-s.co.jp/rhs/maicomi/index.html"],
            aliases=["まいこみ東方祭", "Maikomi Touhou Sai"],
            dates="2010.09.19",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: http://web.archive.org/web/20100908094512fw_/http://www.taiga-s.co.jp/rhs/maicomi/009.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description=None,
            comments="Simultaneous event with まいばらこみゅにけっと2010",
            last_edited="2026.10.13",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "maibaracommuniket2010"  # ==== まいばらこみゅにけっと2010 ====
    if i not in disabled_events:
        event_name = f"{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "maibaracommuniket2010_20100711073143_top2010518.jpg",
                [
                    Source(
                        "http://web.archive.org/web/20100711073143fw_/http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="イラスト：天森つるは 様 【Oriental Lattice】",
            ),
            Medium(
                "maibaracommuniket2010_20100711073143_top2010518-3.jpg",
                [
                    Source(
                        "http://web.archive.org/web/20100711073143fw_/http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="イラスト：嶋田海 様 【BlueCrescentMoon】",
            ),
            Medium(
                "maibaracommuniket2010_20100711073143_top2010518-4.jpg",
                [
                    Source(
                        "http://web.archive.org/web/20100711073143fw_/http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="イラスト：アルフィア 様 【マジックテープ】",
            ),
            Medium(
                "maibaracommuniket2010_20100711073143_top006-2.gif",
                [
                    Source(
                        "http://web.archive.org/web/20100711073143fw_/http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "maibaracommuniket2010_20100928053858_top20100126.jpg",
                [
                    Source(
                        "http://web.archive.org/web/20100711073143fw_/http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.3139509, 136.2813635),
                address="2 Chome-137 Shimotara, Maibara, Shiga 521-0016, Japan",
                description="滋賀県立文化産業交流会館　大ホール",
                sources=[
                    Source(
                        "http://web.archive.org/web/20100908094512fw_/http://www.taiga-s.co.jp/rhs/maicomi/009.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9SwxYrFGS9nGVCprunaMscMx9TTm6u1Dgou4lK86jbBwxgHWZUtu_q8BrPkX0fzBm4t1VRZ9l_XsZE42qJDnr2lQm11Qgtkqc1jAvhjy211oQ9VTqP9FSrv4OqtuZSu1j39rSdr=s0?imgmax=0",
                url="https://maps.app.goo.gl/eTo8g8LyekY7ibgu6",
            ),
        ]
        event = Event(
            links=[
                "http://www.taiga-s.co.jp/rhs/maicomi/index.html",
                "http://u-go.to/mmc/",
            ],
            aliases=["まいばらこみゅにけっと2010", "Maibara Communiket 2010", "mmc"],
            dates="2010.09.19",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: http://web.archive.org/web/20100908094512fw_/http://www.taiga-s.co.jp/rhs/maicomi/009.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    'Alias "mmc": See maibaracommuniket2010_20100711073143_top2010518-4.jpg',
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description=None,
            comments="Simultaneous with まいこみ東方祭.",
            last_edited="2026.10.29",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ====  ====
    # if i not in disabled_events:
    #     # event_name = f"{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[f"{i}"],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         # last_edited="",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = []
    links = []

    event_group = EventGroup(
        aliases=[
            "One-off Touhou Project events",
        ],
        events=events,
        media=media,
        links=links,
        sources=[],
        comments=None,
        description="Collection of one-off events with Touhou Project themes.",
        last_edited="2026.10.13",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")

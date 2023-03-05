"""
Feladat:

A kapott rar-ból ki kellene csomagolnotok a file-okat - ezt manuálisan tegyétek szerintem.

A kapott mappában lévő .txt file-okból kellene statisztikákat készíteni,
amelyeket egy statistics.json nevű fileba kellene majd kiírni.

A feladat megoldása során törekedjetek arra, hogy jól stukturált kódot írjatok - modulokat.

Szükséges statisztikák:

2 féle statisztikát szeretnék kapni.

1. statisztika:

Minden file-hoz készüljön egy statisztika, ebben az esetben a statisztika neve: a txt_file_neve.json legyen:
Statisztikák:
    - Megjelenés ideje
    - Könyv neve
    - Oldal szám: 3000 karakter számít 1 oldalnak

2. statisztika:
Itt egyetlen egy file készüljön, az összes könyvet megvizsgálva kell elkészíteni:

    - leghosszabb könyv
    - legrövidebb könyv
    - legrégebben megjelent könyv
    - leghosszabb című könyv
    - legtöbb 5 betűnél hosszabb szót tartalmazó könyv

    A statisztika valahogy így nézzen ki:
    statistics.json
    {
        "longest_book": {"page_size": 200, "title": "Dracula},
        "shortest_book": {"page_size": 100, "title": "valamilyen_konyv"},
        "oldest_book": {"release_date": 1811, "title": "konyv neve"},
        "longest_title": {"title": "name", "length": 34},
        "legtobb_5_karakteres_szo": {"words_num": 450, "title": "konyv neve"}
    }

Ha kérdésetek van keressetek nyugodtan.

"""

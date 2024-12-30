
You want to update your list to include the new stations (from the mapping) and remove the station codes. Here’s the updated code with these changes:

Updated Code
python
코드 복사
station_names_korean = [
    "수서",
    "동탄",
    "평택지제",
    "곡성",
    "공주",
    "광주송정",
    "구례구",
    "김천(구미)",
    "나주",
    "남원",
    "대전",
    "동대구",
    "마산",
    "목포",
    "밀양",
    "부산",
    "서대구",
    "순천",
    "신경주",
    "여수EXPO",
    "여천",
    "오송",
    "울산(통도사)",
    "익산",
    "전주",
    "정읍",
    "진영",
    "진주",
    "창원",
    "창원중앙",
    "천안아산",
    "포항",
]

station_names_english = [
    "Suseo",
    "Dongtan",
    "Pyeongtaek-Jije",
    "Gokseong",
    "Gongju",
    "Gwangju-Songjeong",
    "Gurye-Gu",
    "Gimcheon-Gumi",
    "Naju",
    "Namwon",
    "Daejeon",
    "Dongdaegu",
    "Masan",
    "Mokpo",
    "Miryang",
    "Busan",
    "Seodaegu",
    "Suncheon",
    "Singyeongju",
    "Yeosu-Expo",
    "Yeocheon",
    "Osong",
    "Ulsan (Tongdosa)",
    "Iksan",
    "Jeonju",
    "Jeongeup",
    "Jinyeong",
    "Jinju",
    "Changwon",
    "Changwon-Jungang",
    "Cheonan-Asan",
    "Pohang",
]

station_names = {"kor": station_names_korean, "en": station_names_english}


def convert_station_name(station_name, lang="en"):
    if lang == "en":
        # get index of station_name in station_names_english
        index = station_names_english.index(station_name)
        return station_names_korean[index]
    elif lang == "tc":
        index = station_names_korean.index(station_name)
        return station_names_english[index]
    else:
        return station_name

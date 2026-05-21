courses = [
    {"name": "이호테우", "distance": 3, "level": "easy", "environment": "ocean"},
    {"name": "삼양해변", "distance": 5, "level": "medium", "environment": "ocean"},
    {"name": "한라수목원", "distance": 2, "level": "easy", "environment": "forest"}
]
user_level = "easy"
user_environment = "ocean"
print("추천 러닝코스")
for course in courses:
    score = 0
    if course["level"] == user_level:
        score += 50
    if course["environment"] == user_environment:
        score += 30
    if score >= 50:
        print(f"{course['name']} / 추천 점수: {score}")

from flask import Flask, jsonify
import scrap
import token

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def cat():
    return '<h1>Voilà la liste des catégories: </h1><br>' \
           'agriculture_produce, beer_wine, beverages_liquor, candy_chocolate, bakery_pastry, coffee_tea, lunch_catering, grocery_stores_markets, asian_grocery_stores <br>' \
           'fruits_vegetables, food_production, smoking_tobacco, meat_seafood_eggs, pet_stores, cats_dogs, horses_riding, animal_parks_zoo, animal_health, pet_services <br>' \
           'insurance, banking_money, accounting_tax, real_estate, investments_wealth, credit_debt_services, wellness_spa, personal_care, cosmetics_makeup, salons_clinics <br>' \
           'hair_care_styling, tattoos_piercings, yoga_meditation, architects_engineers, contractors_consultants, factory_equipment, manufacturing, industrial_supplies, garden_landscaping <br>' \
           'building_materials, tools_equipment, chemicals_plastic, construction_services, production_services, language_learning, colleges_universities, music_theater_classes <br>' \
           'school_high_school, specials_schools, vocational_training, courses_classes, education_services, appliances_electronics, audio_visual, internet_software, computers_phones <br>' \
           'repair_services, clubbing_nightlife, adult_entertainment, childrens_entertainment, gaming, gambling, events_venues, wedding_party, museums_exibits, music_movies, theater_opera <br>' \
           'outdoor_activities, art_handicraft, astrology_numerology, fishing_hunting, needlework_knitting, hobbies, music_instruments, painting_paper, metal_stone_glass_work, home_improvements <br>'\
           'decoration_interior, energy_heating, garden_pond, home_goods_stores, furniture_stores, cultural_goods, bathroom_kitchen, home_garden_services, fabric_stationary, books_magazines, media_information <br>' \
           'photography, video_sound, takeaway, bars_cafes, chinese_korean_cuisine, southeast_asian_cuisine, european_cuisine, japanese_cuisine, mediterranean_cuisine, general_restaurants, vegetarian_diet <br>' \
           'physical_aids, clinics, diagnostics_testing, doctors_surgeons, health_equipment, hospital_emergency, pregnancy_children, medical_specialists, pharmacy_medicine, mental_health, dental_services <br>' \
           'therapy_senior_health, vision_hearing, energy_power, oil_fuel, water_utilities, craftsman, moving_storage, house_sitting_security, plumbing_sanitation, cleaning_service_providers, repair_service_providers <br>' \
           'house_services, administration_services, associations_centers, wholesale, import_export, print_graphic_design, research_development, it_communication, office_space_supplies, hr_recruiting, shipping_logistics <br>' \
           'sales_marketing, lawyers_attorneys, libraries_archives, government_department, municipal_department, customs_toll, law_enforcement, legal_service_providers, registration_services, employment_career <br>' \
           'kids_family, funeral_memorial, waste_management, military_veteran, nature_environment, professional_organizations, shelters_homes, public_services_welfare, housing_associations <br>' \
           'accessories, jewelry_watches, malls_marketplaces, costume_wedding, clothing_rental_repair, clothing_underwear, martial_arts_wrestling, dancing_gymnastics, equipment_associations <br>' \
           'fitness_weight_lifting, golf_ultimate, ball_games, swimming_water_sports, shooting_target_sports, outdoor_winter_sports, extreme_sports, tennis_racquet_sports, activities_tours <br>' \
           'travel_agencies, airlines_air_travel, accomodations_lodging, hotels, airports_parking, other_vehicles_trailers, vehical_rental, motorcycle_powersports, auto_parts_wheels, vehicle_repair_fuel <br>' \
           'taxis_public_transport, air_water_transport, bicycles, cars_trucks'


@app.route('/<choice>/<location>')
def nlp(choice, location):
    comments = scrap.scraping(choice, location)

    predict = token.prediction(comments)

    json = jsonify(predict)

    return json


app.run()

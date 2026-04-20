import sqlite3

conn = sqlite3.connect("plant_diseases.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS remedies")

cursor.execute("""
CREATE TABLE remedies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_name TEXT,
    disease_name TEXT,
    full_tag TEXT UNIQUE,
    cause TEXT,
    remedy TEXT,
    organic_medicine TEXT
)
""")

entries = [
    ("Capsicum", "Bacterial Spot", "Capsicum Bacterial Spot",
     "Bacterial spot is caused by Xanthomonas campestris, a pathogen that thrives in warm, humid conditions. It spreads rapidly through splashing water, contaminated tools, and infected seeds. Symptoms include small, dark, water-soaked lesions on leaves and fruits, which can enlarge and cause premature fruit drop. The disease weakens the plant and reduces marketable yield.",
     "Start with disease-free seeds and resistant varieties. Avoid overhead irrigation to reduce leaf wetness. Sanitize tools and hands before handling plants. Apply copper-based bactericides during early signs of infection. Practice crop rotation and remove infected debris after harvest.",
     "Cow dung slurry, turmeric extract spray, ginger-garlic paste"),

    ("Capsicum", "Healthy", "Capsicum Healthy",
     "Healthy capsicum plants exhibit strong, upright stems, vibrant green leaves, and firm, glossy fruits. There are no signs of wilting, lesions, or pest damage. Optimal health is maintained through balanced nutrition, proper spacing, and regular monitoring.",
     "Ensure consistent watering at the base, apply compost and vermicompost, and monitor for aphids or mites. Use mulch to retain soil moisture and suppress weeds. Prune lower leaves to improve airflow and reduce disease risk.",
     "Vermiwash foliar spray, cow urine tonic, panchagavya"),

    ("Grape", "Esca", "Grape Esca",
     "Esca is a chronic grapevine trunk disease caused by a complex of fungi including Phaeomoniella chlamydospora and Fomitiporia mediterranea. It leads to internal wood decay, leaf tiger-striping, and sudden vine collapse. The disease is favored by pruning wounds and poor vineyard hygiene.",
     "Avoid pruning during wet conditions and disinfect tools between cuts. Remove and burn infected vines. Improve soil health with organic amendments and avoid excessive nitrogen. Monitor for early symptoms and apply biological control agents if available.",
     "Wood vinegar application, biochar amendment, garlic paste on pruning wounds"),

    ("Grape", "Healthy", "Grape Healthy",
     "Healthy grapevines have uniform leaf coloration, strong tendrils, and consistent fruit clusters. There are no signs of leaf blight, trunk decay, or pest infestation. Proper canopy management and soil care are key to maintaining vigor.",
     "Maintain balanced fertilization using compost and micronutrients. Prune regularly to improve airflow and light penetration. Use drip irrigation to avoid leaf wetness. Monitor for fungal diseases and pests like mealybugs.",
     "Seaweed extract foliar spray, compost tea, neem cake"),

    ("Grape", "Leaf Blight", "Grape Leaf Blight",
     "Leaf blight in grapes is commonly caused by Pseudocercospora vitis or similar fungal pathogens. It begins as small brown spots that expand and cause leaf necrosis and drop. This reduces photosynthesis and weakens the vine, especially during fruit development.",
     "Prune infected leaves and improve vineyard airflow. Apply sulfur-based fungicides early in the season. Avoid excessive nitrogen which promotes soft tissue. Disinfect pruning tools and avoid working in wet foliage.",
     "Milk spray, cinnamon extract, diluted clove oil"),

    ("Potato", "Early Blight", "Potato Early Blight",
     "Early blight is caused by Alternaria solani, affecting older leaves first. It produces dark concentric rings surrounded by yellow halos. Severe infection leads to defoliation, reduced tuber size, and poor yield. It thrives in warm, humid conditions and spreads via wind and rain.",
     "Use certified disease-free seed. Apply preventive fungicides like mancozeb or chlorothalonil. Remove infected leaves and avoid overhead watering. Rotate with non-solanaceous crops and maintain field hygiene.",
     "Baking soda spray, compost tea, horsetail decoction"),

    ("Potato", "Healthy", "Potato Healthy",
     "Healthy potato plants have upright stems, lush green leaves, and no signs of lesions, wilting, or pest damage. Tubers develop uniformly underground with minimal rot or deformities.",
     "Use well-drained soil enriched with organic matter. Hill soil around stems to protect tubers. Apply neem cake and monitor for aphids and beetles. Water early in the day and avoid waterlogging.",
     "Neem oil spray, vermicompost, banana peel extract"),

    ("Tomato", "Late Blight", "Tomato Late Blight",
     "Tomato leaf blight is caused by fungal pathogens like Alternaria and Septoria. It starts as small dark spots on lower leaves, which expand and cause leaf curling, yellowing, and drop. Severe cases affect fruit development and increase vulnerability to secondary infections.",
     "Remove infected leaves promptly. Apply fungicides like copper oxychloride or chlorothalonil. Avoid overhead watering and ensure good spacing. Use resistant varieties and rotate crops to reduce inoculum.",
     "Potassium bicarbonate spray, garlic-chili extract, compost tea"),

    ("Tomato", "Yellow Leaf Curl", "Tomato_Yelloe_leaf_curl",
     "Tomato Yellow Leaf Curl Virus (TYLCV) is transmitted by whiteflies and causes upward leaf curling, yellowing, and stunted growth. It severely affects flowering and fruiting, leading to major yield losses. The virus persists in weeds and alternate hosts.",
     "Use TYLCV-resistant varieties. Control whiteflies with neem oil, sticky traps, and reflective mulches. Remove and destroy infected plants. Avoid planting near weed-infested areas and use row covers during early growth.",
     "Neem oil foliar spray, garlic-chili extract, yellow sticky traps")
]

for entry in entries:
    cursor.execute("""
    INSERT INTO remedies (plant_name, disease_name, full_tag, cause, remedy, organic_medicine)
    VALUES (?, ?, ?, ?, ?, ?)
    """, entry)

conn.commit()
conn.close()

"""3. Develop a Flask app that uses URL parameters to display dynamic content.
"""

from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def  index():
    print("printing...")
    return render_template('index.html')

@app.route('/dynamic')
def dynamic():
    dynamic_content = request.args.get("dc", "default") 

    content_messages = {
        'apples': '''I like apples.
Apples are not just delicious fruits; they are also rich in history, symbolism, and nutritional value. With their crisp texture and sweet-tart flavor, apples have become a staple in cuisines worldwide.

Believed to have originated in Central Asia, apples have been cultivated for thousands of years and have earned a place in various cultural traditions and mythologies. They symbolize knowledge, temptation, and youthfulness in many societies, prominently featured in folklore and religious texts.

Nutritionally, apples pack a powerful punch despite their modest size. They are low in calories but high in fiber, making them an excellent choice for weight management and digestive health. Additionally, they contain a variety of vitamins, minerals, and antioxidants, contributing to overall well-being.

Apples come in numerous varieties, each with its own flavor profile, texture, and best uses. From the sweet and crunchy Gala to the tangy and aromatic Granny Smith, there's an apple for every palate and recipe.

Whether enjoyed fresh as a snack, sliced atop salads, baked into pies, or pressed into cider, apples continue to be a versatile and beloved fruit cherished for their taste, nutritional benefits, and cultural significance.'''
        ,
        'oranges': '''I like oranges.
Oranges are not just a vibrant burst of color but also a delicious and nutritious fruit loved by many around the world. Known for their tangy-sweet flavor and refreshing juiciness, oranges are packed with essential vitamins and minerals, making them a popular choice for a healthy snack.

Rich in vitamin C, oranges are renowned for their immune-boosting properties, helping to ward off colds and infections. Additionally, they contain significant amounts of fiber, which aids digestion and promotes gut health. The vibrant hue of oranges comes from their high concentration of beta-carotene, a powerful antioxidant that supports eye health and overall wellbeing.

Whether enjoyed fresh as a juicy snack, squeezed into a refreshing glass of juice, or incorporated into savory dishes and desserts, oranges add a burst of flavor and a nutritional punch to any meal. So, next time you reach for a snack, consider reaching for an orange to brighten your day and nourish your body.''',
        'bananas': '''I like bananas.
Bananas, the beloved tropical fruit, are not just delicious but also packed with nutrients. 
With their distinctive yellow peel and soft, creamy flesh, bananas are a favorite snack for 
people of all ages. Rich in potassium, bananas are known to support heart health and help 
regulate blood pressure. They are also a good source of vitamin C, vitamin B6, and fiber, 
making them a nutritious addition to any diet. Whether enjoyed on their own, blended into 
smoothies, or sliced onto cereal and yogurt, bananas provide a convenient and tasty way to
 boost your daily fruit intake. So next time you're craving a healthy snack, reach for a 
 banana and enjoy its naturally sweet and satisfying flavor.''',
        'default': 'This is the default content'
    }

    return render_template('dynamic.html',message=content_messages.get(dynamic_content))

if __name__ == '__main__':
    app.run(debug=True)

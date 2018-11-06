"""SELECT meal_ingredients.meal_id,  meal_ingredients.ingredient_id, likes.user_id, likes.user_id, likes.like_value, meals.name, ingredients.name 
      FROM meal_ingredients 
      INNER JOIN meals ON meals.id = meal_ingredients.meal_id
      INNER JOIN ingredients ON ingredients.id = meal_ingredients.ingredient_id 
      LEFT JOIN likes ON likes.recipe_id = meal_ingredients.meal_id
      where not exists (select *
        from likes
        where likes.recipe_id = meal_ingredients.meal_id and likes.user_id = :id
      );"""

"""SELECT likes.like_value, likes.user_id, ingredients.name, meal_ingredients.ingredient_id, meal_ingredients.meal_id
      FROM likes
      INNER JOIN meal_ingredients ON meal_ingredients.meal_id = likes.recipe_id 
      INNER JOIN ingredients ON meal_ingredients.ingredient_id = ingredients.id 
      WHERE likes.user_id = :id;"""
"""
arr = [{"meal": "x", "in": "y"}, {"meal": "x", "in": "z"}]
newarr = {}
for i in range(0, len(arr)-1):
    meal = arr[i]["meal"]
    newarr[meal] = {"meal": meal, "in": [] }
for i in range(0, len(arr)-1):
    meal = arr[i]["meal"]
    ing = arr[i]["in"]
    newarr["meal"]["in"].append(ing)
    """

"""
SELECT likes.like_value, likes.user_id, ingredients.name, meal_ingredients.ingredient_id, meal_ingredients.meal_id
      FROM likes
      INNER JOIN meal_ingredients ON meal_ingredients.meal_id = likes.recipe_id 
      INNER JOIN ingredients ON meal_ingredients.ingredient_id = ingredients.id 
"""
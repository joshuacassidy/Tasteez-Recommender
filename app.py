from flask import Flask, Response, request,render_template
import json
app = Flask(__name__)
import math

@app.route('/', methods=['POST'])
def hello_world():
    likeData = json.loads(request.data)["liked"]
    mealData = json.loads(request.data)["meals"]
    print(mealData)

    # likeData = [{'like_value': '1', 'name': 'Chicken'}, {'like_value': '-1', 'name': 'Beef'}, {'like_value': '1', 'name': 'oil'}, {'like_value': '-1', 'name': 'oil'}, {'like_value': '1', 'name': 'Chicken'}, {'like_value': '-1', 'name': 'Beef'}, {'like_value': '1', 'name': 'Chicken'}, {'like_value': '-1', 'name': 'Beef'}, {'like_value': '1', 'name': 'Potatoes'}]
    likes = [i['name'] for i in likeData if i["like_value"] == "1"]
    dislikes = [i['name'] for i in likeData if i["like_value"] == "-1"]
    likesInterDislikes = [i for i in likes if i not in dislikes] 
    dislikesInterLikes = [i for i in dislikes if i not in likes] 

    intersectionOfNames = likesInterDislikes + dislikesInterLikes

    intersection = [i for i in likeData if i["name"] in intersectionOfNames]
    
    for i in intersection:
        if i['like_value'] == '1':
            i['like_value'] = 3

    
    ingredientsScores = {}
    
    print(intersection)

    for i in intersection:
        if i['name'] in ingredientsScores:
            ingredientsScores[i['name']]['likes']+= int(i["like_value"])
        else:
            ingredientsScores[i['name']] = {'name': i['name'], 'likes': int(i["like_value"])}

    ingredientsScoresFlattened = [i for i in ingredientsScores.values()]
    # print(ingredientsScoresFlattened)
    
    # print(intersection)
    
    for i in ingredientsScoresFlattened:
        if i['likes'] < 0:
            i['likes'] = 1

    print(ingredientsScoresFlattened)
    blah = []
    for meal in mealData:
        ingredients = meal['ingredient']
        itm = {i['name']:i for i in ingredientsScoresFlattened if i['name'] in ingredients}
        # print(itm)
        blah.append(itm)
        iSum = 0
        for i in ingredients:
            if i in itm:
                # print(itm[i]['likes'])
                iSum+= (itm[i]['likes'] - 1) ** 2
            else:
                iSum = iSum + 1
        meal['weight'] = math.sqrt(iSum)
    

    return Response(json.dumps(
        sorted(mealData, key=lambda k: k['weight'], reverse=True)[:max(int(len(mealData)/4), 20)]
        ), mimetype='application/json', status='200')

@app.route('/', methods=['GET'])
def test():
    return Response(json.dumps({'Message': "Hello"}), mimetype='application/json', status='200')

if __name__ == '__main__':
    app.run(debug=True)
# perhaps use kNN but map -1:1 0:50 and 1:100 to make values all positive and ridiculously big to score them all this way we can be pure and use euclidean distance enum pattern oooo
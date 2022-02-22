from crypt import methods
from flask import flash, jsonify,request,Flask
import csv

allmovies=[]
with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]

likemovies=[]
dislikemovies=[]
didnotwatchmovies=[]

app=Flask(__name__)
@app.route("/")
def getdeatils():
    return jsonify({
        "data":allmovies[0],
        "status":"sucess"
    })

@app.route("/likemovies",methods=["POST"])
def likemovies():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    likemovies.append(movie)
    return jsonify({
        "status":"sucess"

    }),201

@app.route("/dislikemovies",method=["POST"])
def dislikemovies():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    dislikemovies.append(movie)
    return jsonify({
        "status":"sucess"
    }),201

@app.route("/didnotwatchmovies",method=["POST"])
def didnotwatchmovies():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    didnotwatchmovies.append(movie)
    return jsonify({
        "status":"sucess"
    }),201


if __name__=="__main__":
    app.run()
    
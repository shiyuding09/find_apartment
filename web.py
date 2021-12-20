import json

from flask import Flask, render_template, url_for, request, redirect
import json

with open("static/data/poi.json","r") as f:
    poi=json.load(f)

with open("static/data/apt_coord_price_poi.json","r") as f:
    apt_list=json.load(f)

with open("static/data/tree.txt","r") as f:
    tree=tuple(eval(f.read()))

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('home.html',apt_list=apt_list)



@app.route("/get_point/<num>",methods=['GET'])
def poi_plot(num):
    num=int(num)
    bar_list={"xAxis":{"type":'category',"data":["gym","restaurant","store"]},"yAxis":{"type":'value'},"series":[{"data":[poi['gym'][num],poi['restaurant'][num],poi['store'][num]],"type":"bar"}]}
    return json.dumps(bar_list)


@app.route("/get_question/<str1>",methods=['GET'])
def get_question(str1):
    array_list=json.loads(str1)
    array_list.append(0)
    temp_tree=tree
    for i in array_list:
        temp_tree=temp_tree[i]
    if isinstance(temp_tree,str):
        return temp_tree,200
    if isinstance(temp_tree,int):
        array_list.pop(-1)
        for i in array_list:
            temp_tree = temp_tree[i]
        apt_selected_list=[apt_list['num'][i] for i in temp_tree]
        list_total=list(range(315))
        apt_selected_list=list(set(list_total).difference(set(apt_selected_list)))
        apt_selected_list={"num":apt_selected_list}
        return json.dumps(apt_selected_list),300



if __name__=='__main__':
    app.run(port=8080,debug=True)








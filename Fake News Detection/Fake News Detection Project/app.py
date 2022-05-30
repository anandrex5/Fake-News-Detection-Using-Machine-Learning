from flask import Flask, escape, request, render_template
import pickle



vector = pickle.load(open("vectorizer.pk1", 'rb'))


model = pickle.load(open("finalized_model.pk1", 'rb'))


app  = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction',methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

       
        predict = model.predict(vector.transform([news]))
        print(predict)

        return render_template("predection.html",prediction_text="News headline is -> {}".format(predict))



    else:
        return render_template("predection.html")







if __name__=='__main__':
    app.run()
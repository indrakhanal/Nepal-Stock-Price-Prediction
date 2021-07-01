from flask import Flask, render_template, request
import pickle
import os
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def save_script():
    file_data = []
    text_file = open('script.txt',"r")
    for word in text_file.read().split():
        a=word.strip(",'")
        file_data.append(a)
    text_file.close()
    file_data.sort()
    global data
    data = file_data
    return render_template("ipl.html", context=file_data)


def return_list():
    return data


def frontend_data():
    if request.method == 'GET':
        return render_template('ipl.html')
    else:
        script = request.form.get('script')
        try:
            open =int(request.form.get('open'))
            high = int(request.form.get('high'))
            low = int(request.form.get('low'))
            print(type(open), high, low, 'debugggg')
        except:
            message = 'All Value Should fill up'
            return render_template('ipl.html', message=message)
        datas = return_list()
        dict_script = dict.fromkeys(datas, 0)
        if script in dict_script:
            new_dic = {script: 1}
            dict_script.update(new_dic)
        new_value_list = list(dict_script.values())
        value_of_script= []

        value_of_script.append(open)
        value_of_script.append(high)
        value_of_script.append(low)
        final_all_data_list = value_of_script+new_value_list
        return final_all_data_list


@app.route('/score/', methods=['POST', 'GET'])
def load_model_to_redict():
    try:
        final_pridect_data = [frontend_data()]
        with open('final_modal.pkl', 'rb') as f:
            model = pickle.load(f)
            final_predict = model.predict(final_pridect_data)
            output = int(final_predict)
        return render_template("result.html", message=output)
    except:
        message="All Value Should Fill Up"
        return render_template("result.html", error=message)


if __name__ == "__main__":
     # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
